import boto3
import pandas as pd
import requests
from botocore.exceptions import ClientError
import os
import json
from io import StringIO

# Configurar o cliente S3
s3 = boto3.client('s3')

def fetch_movie_details(movie_id):
    try:
        base_url = 'https://api.themoviedb.org/3'
        endpoint = f'{base_url}/movie/{movie_id}'
        params = {'api_key': os.environ['TMDB_ACCESS_TOKEN']}
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            movie_data = response.json()
            filtered_data = {
                'id': movie_data.get('id'),
                'imdb_id': movie_data.get('imdb_id'),
                'title': movie_data.get('title'),
                'release_date': movie_data.get('release_date'),
                'vote_average': movie_data.get('vote_average'),
                'vote_count': movie_data.get('vote_count'),
                'popularity': movie_data.get('popularity'),
                'budget': movie_data.get('budget'),
                'revenue': movie_data.get('revenue'),
                'runtime': movie_data.get('runtime'),
                'genres': [{'id': genre.get('id'), 'name': genre.get('name')} for genre in movie_data.get('genres', [])]
            }
            return filtered_data
        elif response.status_code == 404:
            print(f'Filme com ID {movie_id} não encontrado na API')
            return None
        else:
            print(f'Erro ao buscar detalhes do filme {movie_id}: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Erro de requisição: {e}')
        return None
    except Exception as e:
        print(f'Erro inesperado: {e}')
        return None

def download_csv_from_s3(bucket_name, file_key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        csv_data = response['Body'].read().decode('utf-8')
        return csv_data
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            print(f'Erro: O arquivo {file_key} não existe no bucket {bucket_name}')
        else:
            print(f'Erro ao baixar o arquivo CSV: {e}')
        return None
    except Exception as e:
        print(f'Erro inesperado ao baixar o arquivo CSV: {e}')
        return None

def get_distinct_ids(csv_data):
    try:
        df = pd.read_csv(StringIO(csv_data), sep='|', low_memory=False)
        df['anoLancamento'] = pd.to_datetime(df['anoLancamento'], errors='coerce')
        df = df[df['anoLancamento'].dt.year > 2004]
        df['genero'] = df['genero'].str.lower()
        action_ids = df[df['genero'].str.contains('action')]['id'].unique()
        adventure_ids = df[df['genero'].str.contains('adventure')]['id'].unique()
        action_adventure_ids = df[df['genero'].str.contains('action') & df['genero'].str.contains('adventure')]['id'].unique()
        todos_ids_distintos = list(set(action_ids).union(adventure_ids).union(action_adventure_ids))
        return todos_ids_distintos
    except pd.errors.ParserError as e:
        print(f'Erro ao processar o DataFrame: {e}')
        return None
    except Exception as e:
        print(f'Erro inesperado ao processar o DataFrame: {e}')
        return None

def chunked(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]

def lambda_handler(event, context):
    try:
        # Obter a chave de API do TMDb a partir das variáveis de ambiente
        tmdb_api_key = os.environ['TMDB_ACCESS_TOKEN']

        # Configurações para o S3
        bucket_name = 'rafaelkabata-bucket-teste-programa-bolsa001'
        folder_path = 'Raw/TMDB/JSON/2024/06/15/'
        file_key = 'Raw/Local/CSV/Movies/2024/05/31/movies.csv'

        # Baixar o arquivo CSV do S3
        csv_data = download_csv_from_s3(bucket_name, file_key)

        if csv_data:
            # Obter todas as IDs distintas para filmes de Action, Adventure e Action & Adventure
            distinct_ids = get_distinct_ids(csv_data)

            if distinct_ids:
                print(f'Total de IDs distintos encontrados: {len(distinct_ids)}')

                # Dividir as IDs distintas em chunks de 100 IDs
                id_chunks = list(chunked(distinct_ids, 100))

                total_saved = 0
                total_errors = 0

                # Iterar sobre os chunks de IDs
                for chunk_index, id_chunk in enumerate(id_chunks):
                    movie_details = []

                    # Iterar sobre os IDs no chunk atual
                    for movie_id in id_chunk:
                        movie_data = fetch_movie_details(movie_id)
                        if movie_data:
                            movie_details.append(movie_data)

                    # Salvar o resultado filtrado em um arquivo JSON no S3
                    file_name = f'{folder_path}movies_chunk_{chunk_index + 1}.json'
                    try:
                        # Converter os dados filtrados para JSON
                        json_data = json.dumps(movie_details)

                        # Enviar o arquivo JSON para o S3
                        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_data)

                        total_saved += len(movie_details)
                        print(f'Detalhes dos filmes no chunk {chunk_index + 1} salvos em {file_name}')
                    except ClientError as e:
                        total_errors += len(id_chunk)
                        print(f'Erro ao enviar arquivo para o S3: {e}')
                    except Exception as e:
                        total_errors += len(id_chunk)
                        print(f'Erro inesperado: {e}')

                print(f'Total de IDs salvos: {total_saved}')
                print(f'Total de IDs com erro: {total_errors}')

    except KeyError as e:
        print(f'Erro: Variável de ambiente não configurada - {e}')
    except Exception as e:
        print(f'Erro inesperado no processamento: {e}')

