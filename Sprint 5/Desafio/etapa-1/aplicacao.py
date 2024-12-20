import boto3
import os

# Configura o cliente S3
s3_client = boto3.client('s3')

# Nome do novo bucket a ser criado
bucket_name = 'meu-bucket-de-teste-0000' 
file_name = 'imoveis_cadastrados.csv'  

try:
    # Cria o bucket 
    response = s3_client.create_bucket(
        Bucket=bucket_name
    )
    print(f"Bucket '{bucket_name}' criado com sucesso.")

    # Envia um arquivo CSV para o bucket
    file_path = os.path.join(os.getcwd(), file_name)  
    with open(file_path, 'rb') as file:
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file)
    print(f"Arquivo CSV '{file_name}' enviado com sucesso para o bucket '{bucket_name}'.")

    # Consulta de seleção utilizando S3 Select
    select_query = """SELECT UPPER(s.uf), CAST(s.numero_de_cadastros AS FLOAT), CAST(s.area_cadastrada AS FLOAT), UTCNOW()  
    FROM s3object s where s.numero_de_cadastros < 'sum(Cast(s.numero_de_cadastros as float))' 
    and s.numero_de_cadastros > 'avg(Cast(s.numero_de_cadastros as float))'
     and COUNT(NULLIF(s.uf, 'RJ')) or s.uf ='SP' or s.uf ='RJ'"""
 

    # Parâmetros para a consulta S3 Select
    params = {
        'Bucket': bucket_name,
        'Key': file_name,
        'ExpressionType': 'SQL',
        'Expression': select_query,
        'InputSerialization': {'CSV': {'FileHeaderInfo': 'USE'}, 'CompressionType': 'NONE'},
        'OutputSerialization': {'CSV': {}}
    }

    # Executa a consulta S3 Select
    response = s3_client.select_object_content(**params)

    # Processa a resposta da consulta
    for event in response['Payload']:
        if 'Records' in event:
            # Processa e exibir os registros retornados
            records = event['Records']['Payload'].decode('utf-8')
            print(records, end='')  # Utiliza end='' para imprimir sem quebra de linha

except Exception as e:
    print(f"Erro durante a execução do script: {e}")
