import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from pyspark.sql import Window
from awsglue.context import GlueContext
from awsglue.job import Job

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'TMDB_DATA_PATH', 'IMDB_DATA_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

tmdb_path = args['TMDB_DATA_PATH']
imdb_path = args['IMDB_DATA_PATH']
output_path = args['S3_TARGET_PATH']

# Leitura dos dados do S3
df_tmdb = spark.read.parquet(tmdb_path)
df_imdb = spark.read.parquet(imdb_path)

# Processamento dos dados IMDB
df_imdb = df_imdb.withColumn(
    'id_genre',
    F.when(F.col('genero').contains('Action') & ~F.col('genero').contains('Adventure'), 1)
     .when(F.col('genero').contains('Adventure') & ~F.col('genero').contains('Action'), 2)
     .when(F.col('genero').contains('Action') & F.col('genero').contains('Adventure'), 3)
     .otherwise(None)
)

# Renomear coluna 'id' de df_tmdb para evitar conflitos
df_tmdb = df_tmdb.withColumnRenamed('id', 'tmdb_id')

# Criar uma visão temporária para consultas SQL
df_geral = df_imdb.join(df_tmdb, df_imdb.id == df_tmdb.imdb_id, 'inner')
df_geral.createOrReplaceTempView('db_geral')

# Criar e salvar a tabela de artistas
df_actors = df_imdb.groupBy('nomeArtista').count().withColumnRenamed('nomeArtista', 'name').withColumnRenamed('count', 'num_movies')
df_actors = df_actors.withColumn('id', F.row_number().over(Window.orderBy(F.lit(1))))
df_actors.write.mode('overwrite').parquet(f'{output_path}dim_actor')

# Criar e salvar a tabela de datas
df_dates = df_tmdb.select(F.col('release_date').alias('date')).distinct().orderBy('date')
df_dates = df_dates.withColumn('year', F.year('date')).withColumn('month', F.month('date')).withColumn('day', F.dayofmonth('date'))
df_dates = df_dates.withColumn('quarter', F.when(F.month('date').between(1, 3), 'Q1').when(F.month('date').between(4, 6), 'Q2').when(F.month('date').between(7, 9), 'Q3').otherwise('Q4'))
df_dates = df_dates.withColumn('id', F.row_number().over(Window.orderBy(F.lit(1))))
df_dates.write.mode('overwrite').parquet(f'{output_path}dim_date')

# Criar e salvar a tabela de filmes
df_movies = spark.sql("""
    SELECT DISTINCT
        id,
        tituloPrincipal AS main_title,
        tituloOriginal AS original_title,
        release_date,
        genero AS genres
    FROM db_geral
""")
df_movies.write.mode('overwrite').parquet(f'{output_path}dim_movie')

# Criar e salvar a tabela fato
df_fato = spark.sql("""
    SELECT DISTINCT
        id AS id_movie,
        nomeArtista,
        release_date,
        id_genre,
        runtime,
        revenue,
        budget,
        personagem AS actor_role,
        popularity,
        notaMedia AS imdb_rating,
        vote_average AS tmdb_rating,
        numeroVotos AS imdb_vote_count,
        vote_count AS tmdb_vote_count
    FROM db_geral
""")

df_fato = df_fato.join(df_dates, df_fato.release_date == df_dates.date, 'inner').withColumnRenamed('id', 'id_date')
df_fato = df_fato.join(df_actors, df_fato.nomeArtista == df_actors.name, 'inner').withColumnRenamed('id', 'id_actor')

colunas_indesejadas = ['release_date', 'date', 'year', 'month', 'day', 'quarter', 'nomeArtista', 'name', 'num_movies']
df_fato = df_fato.drop(*colunas_indesejadas)

df_fato.write.partitionBy('id_movie').mode('overwrite').parquet(f'{output_path}fact_movie_actor')

# Criar e salvar a tabela de gêneros
df_genres = df_fato.select('id_movie', 'id_genre').distinct().groupBy('id_genre').count()
df_genres = df_genres.withColumnRenamed('id_genre', 'id').withColumnRenamed('count', 'num_movies')
df_genres = df_genres.withColumn('genre', F.when(F.col('id') == 1, 'Action').when(F.col('id') == 2, 'Adventure').when(F.col('id') == 3, 'Action/Adventure'))
df_genres.write.mode('overwrite').parquet(f'{output_path}dim_genre')

job.commit()