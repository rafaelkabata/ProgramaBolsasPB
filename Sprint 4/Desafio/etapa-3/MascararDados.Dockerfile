# Use a imagem base do Python 3.8 slim
FROM python:3.8-slim

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie todo o conteúdo do diretório de construção para o diretório /app dentro do contêiner
COPY . /app

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "hash_calculator.py"]
