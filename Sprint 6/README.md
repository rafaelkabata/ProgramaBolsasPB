# SOBRE O DESAFIO FINAL
A Squad 5 ao qual faço parte ficou com o tema de ação e aventura para análise de filmes e séries. Ao análisar as possibilidades existentes no csv de movies e series para ação e aventura, acabei encontrando o título de Indiana Jones. Indiana Jones é um personagem icônico do cinema, criado por George Lucas e interpretado por Harrison Ford. Ele é um arqueólogo aventureiro que se envolve em missões perigosas para encontrar artefatos lendários e enfrentar vilões. A série começou com "Os Caçadores da Arca Perdida" (1981), onde Indiana tenta impedir que os nazistas consigam a Arca da Aliança. Em "Indiana Jones e o Templo da Perdição" (1984), ele busca pedras sagradas na Índia e enfrenta uma seita maléfica. "Indiana Jones e a Última Cruzada" (1989) o vê em uma busca pelo Santo Graal ao lado de seu pai, lutando contra os nazistas. Em "Indiana Jones e o Reino da Caveira de Cristal" (2008), ele enfrenta agentes soviéticos e investiga mistérios envolvendo alienígenas. O mais recente filme, "Indiana Jones e o Chamado do Destino" (2023), apresenta Indy em uma nova jornada cheia de ação e mistério, enfrentando novos desafios e descobrindo novos artefatos. Indiana é conhecido por seu chapéu Fedora, chicote e jeito astuto, combinando inteligência com coragem. Os filmes são adorados por suas cenas de ação, humor e o carisma do personagem principal.

- Em minhas análises, buscarei fazer comparações de bilheteria entre os filmes;
- Análisar as notas médias dos críticos;
- Fazer comparações entre os filmes da década de 80 com os novos filmes;
- Orçamento;

  Essas são apenas algumas idéias para se fazer de análises

<br/>
</div>


# [Desafio](https://github.com/rafaelkabata/ProgramaBolsasPB/tree/main/Sprint%206/Desafio)
### O objetivo da [Sprint 06](https://github.com/rafaelkabata/ProgramaBolsasPB/tree/main/Sprint%206/Desafio) foi praticar a combinação de conhecimentos visto no programa, fazendo um mix de tudo que já foi dito.
<br/>
</div>



![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/evidencias/Desafio.png)
<br/>
</div>

Iniciei o desafio criando um script em Python utilizando a biblioteca Boto3 para acessar a AWS e o S3 e estar criando um Bucket que armazenará os arquivos movies.csv e series.csv.Abaixo podemos observar a criação da função que faz a verificação e a criação do Bucket no S3. <br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/evidencias/CodigoBoto3_1.png)
<br>

Após a criação da função para se criar o Bucket, foi a vez de construir a função que fará o upload dos arquivos para a AWS. Os dados devem ser salvos na camada Raw do Bucket no formato `s3://<Bucket-name>/Raw/Local/CSV/Movies/YYYY/MM/DD/file-name.csv`. Por isso devemos obter a data do upload usando o datetime.now(). Depois ele define o caminho conforme o formato proposto e realiza o upload do arquivo para o S3 na AWS. Também é definido um nome para o Bucket e um dicionário para o script entender quando é o arquivo movies.csv e quando é o arquivo series.csv na hora da criação da pasta. Ao final do script ele roda as duas funções.
<br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/evidencias/CodigoBoto3_2.png)

# Evidencias





