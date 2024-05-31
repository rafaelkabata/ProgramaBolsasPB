import boto3
from datetime import datetime

def create_bucket(bucket_name, region=None):
    s3 = boto3.client('s3')
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f'Bucket {bucket_name} criado.')
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f'Bucket {bucket_name} já existe e é de sua propriedade.')
    except s3.exceptions.BucketAlreadyExists:
        print(f'O bucket {bucket_name} já existe e é de outra pessoa.')
    except Exception as e:
        print(f'Erro ao criar bucket: {e}')

def upload_files_to_s3(bucket_name, files):
    s3 = boto3.client('s3')
    for file, s3_path in files.items():
        try:
            # Para obter a data de upload do arquivo
            upload_date = datetime.now().strftime("%Y/%m/%d")
            # Define o caminho completo no bucket com base na data de upload e no caminho fornecido
            full_s3_path = f'Raw/Local/CSV/{s3_path}/{upload_date}/{file}'
            # Realiza upload do arquivo para o S3
            s3.upload_file(file, bucket_name, full_s3_path)
            print(f'Arquivo {file} enviado para o bucket {bucket_name} em {full_s3_path}')
        except Exception as e:
            print(f'Erro ao enviar o arquivo {file} para o bucket {bucket_name}: {e}')

# Define o nome do bucket S3
bucket_name = 'rafaelkabata-bucket-teste-programa-bolsa001'

# Dicionário de arquivos CSV com seus respectivos caminhos relativos no S3
files = {
    'movies.csv': 'Movies',
    'series.csv': 'Series'
}

# Cria o bucket S3 (se ainda não existir)
create_bucket(bucket_name)

# Upload dos arquivos CSV para o S3
upload_files_to_s3(bucket_name, files)
