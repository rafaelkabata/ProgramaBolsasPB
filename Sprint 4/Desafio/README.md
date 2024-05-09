## Etapa 1

[Etapa 1](https://github.com/rafaelkabata/ProgramaBolsasPB/tree/main/Sprint%204/Desafio/etapa-1)
Construa uma imagem a partir de um arquivo de instrução dockerfile que execute o codigo carguru.py. Após, execute um conteiner a partir desta imagem

para construir o conteiner a partir da imagem criada :
```bash
docker build -t conteiner_carguru
```
Para executar o conteiner
```bash
docker run conteiner_carguru
```

</div>

## Etapa 2 
É possivel reutilizar um conteiner ? Em caso positivo, apresente o comando necessário para iniciar um ou mais containers parados em seu ambiente Docker. Não sendo possível reutilizar justifique sua resposta

Sim, é possível reutilizar os contêineres que estão parados no Docker. Você pode usar o comando docker start <nome_ou_id_do_container> para iniciar um conteiner específico que está parado. Se precisar iniciar vários conteineres ao mesmo tempo, você pode listar os nomes ou IDs deles separados por espaço no mesmo comando. Isso permite reiniciar os conteineres de forma rápida, mantendo todas as configurações que foram definidas anteriormente.

</div>

## Etapa 3
[Etapa 3](https://github.com/rafaelkabata/ProgramaBolsasPB/tree/main/Sprint%204/Desafio/etapa-3) - Agora vamos exercitar a criação de um container que permita receber inputs durante a execução. Abaixo seguem as instruções:
-receber uma String via Input
- Gerar o hash da String por meio do Algoritmo SHA-1
- Imprimir o Hasg em tela, utilizando o método hexdigest
-  Retornar ao passo 1
Criar uma imagem Docker chamada mascarar-dados que execute o scritp Python anteriormente
Iniciar o container a partir da imagem, enviando algumas palavras para mascaramento
Registrar o conteudo do script Python, arquivo Dockerfile e comando de inicialização neste espaco

Para construir o container através da imagem criada utilizamos o seguinte comando:
```bash
docker build -t calculator_hash
```
Para executar o container criado 
```bash
docker build -it calculator_hash
```

a flag -it serve para que o terminal vire interativo e o usuário consiga digitar no terminal

</div>
