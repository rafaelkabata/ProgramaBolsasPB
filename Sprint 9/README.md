# SOBRE O DESAFIO FINAL
## A quarta parte do desafio final consiste em fazer o refinamento dos dados 

<br>

Foi desenvolvido um modelo dimensional para representar os dados de filmes combinados entre duas bases distintas. Esse tipo de modelagem em um banco de dados OLAP (Processamento Analítico Online) tem como objetivo otimizar a estrutura dos dados, facilitando análises complexas e consultas personalizadas em grandes conjuntos de dados multidimensionais.

Diferente dos modelos relacionais utilizados em bancos de dados transacionais OLTP, onde a normalização dos dados é priorizada, a modelagem dimensional busca proporcionar uma experiência analítica mais eficiente e intuitiva.

O modelo desenvolvido para este projeto foi criado com o intuito de simplificar a extração de informações específicas por dimensão nos dados, permitindo a realização de análises temporais (como datas de lançamento), avaliações de gênero, e outras análises pertinentes. Assim, os usuários podem obter insights valiosos e fazer consultas detalhadas de maneira mais ágil e precisa.

<br>

![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%209/evidencias/Diagrama.jpeg)

<br>

Foi criada uma tabela chamada fact_movie_actor para registrar os relacionamentos entre atores e filmes, conectando as diferentes dimensões envolvidas.

A tabela dim_movie armazena informações descritivas sobre cada filme, incluindo títulos, gêneros e datas de lançamento. Já a tabela dim_actor contém o nome de cada artista e o número de filmes em que ele ou ela participou. A tabela dim_date registra as diferentes datas de lançamento dos filmes, detalhando informações como ano, mês, dia e trimestre.

Por fim, a tabela dim_genre armazena os gêneros principais de cada filme analisado, como Adventure, Action ou Adventure/Action (para filmes que se encaixam nas duas categorias), além de registrar a quantidade de filmes que se enquadra em cada um desses gêneros.

Esta estrutura foi elaborada para facilitar a análise e extração de dados específicos, permitindo uma compreensão mais clara e detalhada das interações e características dos filmes e seus atores, assim como a distribuição de lançamentos ao longo do tempo e a categorização por gênero.

















