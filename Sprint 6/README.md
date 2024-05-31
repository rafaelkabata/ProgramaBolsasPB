# [Desafio](https://github.com/rafaelkabata/ProgramaBolsasPB/tree/main/Sprint%205/Desafio)
## O objetivo da [Sprint 05](https://github.com/rafaelkabata/ProgramaBolsasPB/tree/main/Sprint%205/Desafio) foi a praticar conhecimento de nuvem AWS aprendidos na sprint.

![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/obj_desafio_1.png)
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/obj_desafio_2.png)
<br/>
</div>

# Evidencias

## Aqui está o passo a passo de como foi construido toda a sprint 5.

O primeiro passo foi a escolha de um arquivo Json ou CSV na [bases de dados publicos do governo](https://dados.gov.br/home) para escolher um arquivo para ser trabalhado durante esta sprint.<br><br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/dados_governo.png)
<br><br>

Como eu também sou Engenheiro Agrônomo, procurei uma base de dados que fosse relacionado com agricultura, onde acabei achando a base de dados do [Cadastro Ambiental Rural](https://dados.gov.br/dados/conjuntos-dados/cadastro-ambiental-rural1). O Cadastro Ambiental Rural (CAR) é um registro eletrônico obrigatório para todos os imóveis rurais no Brasil, instituído pelo Código Florestal de 2012 (Lei n° 12.651/2012). O CAR integra informações ambientais das propriedades rurais, como Áreas de Preservação Permanente (APPs), Reserva Legal (RL), florestas e remanescentes de vegetação nativa, além das áreas de interesse social e utilidade pública.O objetivo principal do CAR é a formação de uma base de dados para controle, monitoramento, planejamento ambiental e econômico, além de combate ao desmatamento. A inscrição no CAR é o primeiro passo para a regularização ambiental das propriedades e posses rurais, sendo essencial para acessar diversas políticas públicas e incentivos econômicos. Eu acabei optando por analisar o arquivo "Imóveis Cadastrados por Unidade Federativa". 
<br>

![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/cadastro_area_rural.png)
<br><br>

Sendo esta a minha base de dados que conta com uf(unidade federativa), numero_de_cadastros(número de cadastros no sistema por unidade federativa) e area_cadastrada(Área cadastrada por unidade federativa) <br> <br>

![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/imoveis_cadastrados_tabela.png)

<br>

Após encontrar o arquivo, o próximo passo foi acessar a [documentação do Select s3](https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/s3-select-sql-reference-select.html) para começar a pensar na query para fazer a consulta via Boto3. A documentação do Amazon S3 Select descreve o uso do comando SQL SELECT para consultar dados diretamente nos objetos S3. Suporta cláusulas padrão como SELECT, FROM, WHERE e LIMIT, mas não permite subconsultas ou junções. Explica como consultar dados em formatos CSV e JSON, detalhando o acesso a atributos e as expressões escalares. Inclui exemplos práticos para ilustrar consultas e tratamento de dados.
<br>


![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/documentacao_aws.png)

<br><br>

Após conhecer os comandos suportados pelo Select S3, criei um Bucket via console e enviei meu csv para poder ter acesso ao terminal para começar a construir minha query de pesquisa que seria passada via terminal posteriormente via código e Boto3. Abaixo está onde consegui construir a query com todos os requisitos propostos pelo desafio. 
- As duas cláusulas de pesquisa que filtra dados com dois operadores lógicos ( AND e OR )
- Duas funções de agregação ( SUM e AVG )
- Uma função Condicional ( NULLIF )
- Uma função de Conversão ( CAST )
- Uma função de data ( UTCNOW() )
- Uma função de String ( UPPER )
  
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/consulta_s3_aws.png)

<br><br>

Após conseguir construir a query, comecei a construir o código para criar um bucket, enviar o csv e fazer a consulta tudo via código e linha de comando. Porém, antes foi necessário configurar o acesso da AWS via aws configure. Não obtive muita dificuldade nesta etapa graças ao nosso instrutor Ari que deu o suporte necessário para a configuração de nossas maquinas através de sua monitoria. Fica aqui o meu agradecimento. Fui construindo o código por etapas, então a primeira etapa foi construir a parte para a criação do Bucket pela linha do comando como demonstrado abaixo. As credenciais de acesso da aws também poderiam ser passadas via código, mas eu optei por configurar o acesso na minha máquina.

![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/codigo_criacao_bucket.png)

<br><br>

Após esta etapa e vendo que tinha conseguido criar o bucket pelo script, comecei a trabalhar para que quando ele criasse o bucket também conseguisse enviar o arquivo csv para o armazenamento e podemos conferir abaixo como ficou esta parte:

![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/enviar_csv_aws.png)

<br><br>

Por fim, após a criação e envio do csv via código, era necessário testar se a query que fiz estava retornando valores pelo script e construir esta consulta, abaixo podemos conferir como ficou esta parte:
<br>


![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/enviar_query_e_retornar_valor_aws.png)

<br><br>

E podemos observar o sucesso do código onde ele retorna que o bucket foi criado, o csv foi enviado e o resultado da query 
<br> 
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/evidencias/resultado_prompt_aws.png)

<br><br>

# Certificados
[Certificado AWS Cloud Quest: Cloud Practitioner](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/certificados/aws-cloud-quest.png) [acesso em](https://www.credly.com/badges/b2d4674c-b441-4fe1-94ed-a94d3b89a51a)

[AWS Skill Builder Course Completion Certificate](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%205/certificados/18719_5_5266074_1716215657_AWS%20Skill%20Builder%20Course%20Completion%20Certificate.pdf)
<br/>
</div>


