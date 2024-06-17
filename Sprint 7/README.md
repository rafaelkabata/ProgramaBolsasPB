# SOBRE O DESAFIO FINAL
## A segunda parte do desafio final consiste em enviar mais dados brutos para o S3 através da API do [The Movies DataBase](https://developer.themoviedb.org/docs/getting-started)

<br>

## Questões a serem respondidas
Na Sprint passada eu estava com idéia de estudar a trilogia de Indiana Jones, porém nesta Sprint acabei mudando de idéia.
Selecionei para trazer para esta sprint e para as futuras as análises de filmes que contenham ação e aventura em seu genêro lançadas a partir do ano de 2004. Algumas questões que penso em estudar são :
<br>

- Filmes de maiores bilheterias por ano. <br>

- Relação de bilheteria e filmes. <br>

- Quantidade de lançamentos de filmes ao longo desses 20 anos e o aumento ou diminuição do orçamento. <br>

- comparação entre orçamento e filmes. <br>

- atores que tiveram as melhores avaliações x quanto ganharam por filme . <br>

- comparar a nota média entre ação e aventura. <br>

## API DA TMDB
A API que utilizei do TMDB foi a API [Movie-Details](https://developer.themoviedb.org/reference/movie-details) ao qual extrai diversas informações de acordo com o id ao qual está requisitando. <br> 
O input utilizado para buscar os id's foi o movies.csv, que mandamos na sprint passada para o S3. No Script foi feito uma filtragem para que ele pegasse no csv apenas filmes que continham em genêro ação (action) e aventura (adventure). Também coloquei um outro filtro no meu script para que ele me trouxesse apenas id's a partir do ano de 2004 pois minha análise focará nos filmes de ação e aventura das duas últimas décadas. Foram encontrados 16.758 id's desses genêros considerando o meu filtro ser a partir de 2004 dentre os 244.243 id's distintos que existiam no csv. Usei um outro filtro para a API me trazer apenas informações ao qual eu achava relevante trazer sendo estes : id,'imdb_id', 'title', 'release_date', 'vote_average','vote_count','popularity', 'budget', 'revenue', 'runtime','genres'.
<br>
<br>
## Processando dados
Após o processamento da API foram encontrados 12.389 id's e armazenados no Bucket do S3 em arquivos no formato json onde cada Json contém o registro de 100 id's. <br>
Para a API funcionar, ela necessita ser armazenada em uma váriavel de ambiente da AWS, para não ficar contida no código da Lambda, então ela foi armazenada usando a [AWS KMS](https://aws.amazon.com/pt/kms/) para permanecer em repouso e ser usada apenas quando o script estiver sendo rodado. <br>
Também foi necessário configurar uma camada para o script na Lambda. Em adicionar camada a aws fornece uma layer pronta para rodar o Pandas e o Requests chamada AWSSDKPandas-Python312. 













