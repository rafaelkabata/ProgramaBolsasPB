import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from awsglue.context import GlueContext
from awsglue.job import Job

# Obtenção dos parâmetros do job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
output_path = args['S3_TARGET_PATH']

# Definição do esquema e leitura do arquivo CSV
schema = """
id STRING,
tituloPincipal STRING,
tituloOriginal STRING,
anoLancamento INT,
tempoMinutos INT,
genero STRING,
notaMedia DOUBLE,
numeroVotos INT,
generoArtista STRING,
personagem STRING,
nomeArtista STRING,
anoNascimento INT,
anoFalecimento INT,
profissao STRING,
titulosMaisConhecidos STRING
"""

df = spark.read.option("encoding", "UTF-8") \
    .csv(source_file, schema=schema, sep="|", header=True)

df.printSchema()
print("Total de registros:", df.count())

# Remoção de colunas indesejadas
colunas_remover = ['generoArtista', 'anoNascimento', 'anoFalecimento', 'profissao', 'titulosMaisConhecidos']
df = df.drop(*colunas_remover)
df = df.withColumnRenamed('tituloPincipal', 'tituloPrincipal')

# Filtragem dos gêneros desejados (action e adventure)
df_filtrado = df.filter(F.col('genero').like('%Action%') | F.col('genero').like('%Adventure%'))

df_filtrado.printSchema()
print("Registros após filtragem:", df_filtrado.count())
print("IDs distintos:", df_filtrado.select('id').distinct().count())

# Remoção de duplicatas e valores nulos
df_limpado = df_filtrado.dropDuplicates().dropna()
print("Registros após limpeza:", df_limpado.count())

# Substituição de '\N' por valores nulos na coluna 'personagem'
df_limpado = df_limpado.withColumn('personagem', F.when(F.col('personagem') == '\\N', None).otherwise(F.col('personagem')))

# Filtragem por número de votos
df_final = df_limpado.filter(F.col("numeroVotos") >= 30)

# Verificação de inconsistências
total_ids = df_final.select('id').distinct().count()
print("IDs distintos após filtragem de votos:", total_ids)
total_filmes = df_final.select('id', 'tituloPrincipal', 'tituloOriginal', 'anoLancamento', 'tempoMinutos', 'genero', 'notaMedia', 'numeroVotos').distinct().count()
print("Total de filmes distintos:", total_filmes)

# Checagem final dos dados
print("Registros finais:", df_final.count())
df_final.printSchema()
df_final.describe().show()
df_final.show()

# Gravação do resultado final no formato Parquet
df_final.write.parquet(output_path)

job.commit()