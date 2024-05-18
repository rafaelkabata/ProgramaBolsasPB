# Desafio
[Desafio da Sprint 05](https://github.com/rafaelkabata/ProgramaBolsasPB/tree/main/Sprint%205/Desafio)

<br>
## O objetivo da sprint5 foi a praticar conhecimento de nuvem AWS aprendidos na sprint.

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


