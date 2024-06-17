Laboratório de AWS Glue
Laboratório de AWS Glue
Introdução
1 - Preparando os dados de origem
2 - Configurando sua conta para utilizar o AWS Glue
3 - Criando a IAM Role para os jobs do AWS Glue
4 - Configurando as permissões no AWS Lake Formation
5 - Criando novo job no AWS Glue
5.1 - Eliminando execuções de jobs
5.2 Sua vez!
6 - Criando novo crawler
Introdução
Processos de ETL (Extract, Transform and Load) estão presentes em todos os projetos de dados. O
cenário costuma ser o mesmo: fontes de dados diversas com datasets de interesse que precisam ser
ingeridos, transformados e armazenados em um ou mais destinos, com formatos diferentes da
origem.
Neste laboratório você será guiado na construção de um processo de ETL simplificado utilizando o
serviço AWS Glue.
1 - Preparando os dados de origem
Faremos uso do arquivo nomes.csv, um dataset que contém os nomes mais comuns de registro de
nascimento dos cartórios americanos entre os anos de 1880 e 2014. Trata-se de um arquivos CSV,
com a estrutura descrita na amostra a seguir.
nome,sexo,total,ano
Jennifer,F,54336,1983
Para nosso laboratório, o arquivo deverá estar em um bucket do S3. Vamos considerar que o path do
arquivo seja s3://{BUCKET}/lab-glue/input/nomes.csv . Lembre-se que o valor {BUCKET} deve ser
substituído por um dos disponíveis em sua conta.
2 - Configurando sua conta para utilizar o AWS Glue
Acesse a página inicial do serviço AWS Glue. Para que possamos utilizar o serviço com as
permissões necessárias, devemos seguir o passo-a-passo disponível a partir da opção Set up roles
and users no card Prepare your account for AWS Glue.
No primeiro passo devemos indicar quais roles e usuários terão acesso ao serviço AWS Glue.
Procure pelo seu usuário em Choose users e o adicione à lista.
No passo seguinte, informe acesso total ao S3 para leitura e escrita
