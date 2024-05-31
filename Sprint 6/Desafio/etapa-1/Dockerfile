# Use uma imagem base oficial do Python
FROM python:3.12-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o script Python para o diretório de trabalho no contêiner
COPY . . 

VOLUME /root/.aws/
# Defina o diretório para armazenar os arquivos CSV
VOLUME /app/data

# Comando para executar o script Python
CMD ["python", "main.py"]
