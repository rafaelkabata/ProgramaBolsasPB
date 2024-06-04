# Lab AWS S3
## Objetivo:
## Explorar as capacidades do serviço AWS S3.  Nos passos que seguem, você será guiado pelas configurações necessárias para que um bucket do Amazon S3 funcione como hospedagem de conteúdo estático.



Antes de iniciar o laboratório é preciso realizar login no AWS Management Console, caso não esteja autenticado. Para tal, utilize o endereço https://academy-compass.awsapps.com/start#/, o qual permite acesso integrado com sua conta no Office365.



Etapa 1: Criar um bucket


As instruções a seguir fornecem uma visão geral de como criar seus buckets para hospedagem de conteúdo estático:

No Console, busque pelo serviço S3.

Selecione Create bucket (Criar bucket).

Insira o Bucket name (Nome do bucket) (por exemplo, example.com).

Selecione a região onde você deseja criar o bucket. Escolha US East (N. Virginia) us-east-1.

Para aceitar as configurações padrão e criar o bucket, escolha Create (Criar). <br>

![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/exercicios/1-exbucket.png)



Etapa 2: Habilitar hospedagem de site estático


Depois de criar um bucket, você pode habilitar a hospedagem de site estático nele. Os passos necessários são:



No Console, busque pelo serviço S3.

Na lista Buckets, escolha o nome do bucket para o qual você deseja habilitar a hospedagem de site estático.

Escolha Properties (Propriedades).

Em Static website hosting (Hospedagem estática de sites), escolha Edit (Editar).

Escolha Use this bucket to host a website (Usar este bucket para hospedar um site).

Em Static website hosting (Hospedagem estática de sites), escolha Enable (Ativar).

Em Index Document (Documento de índice), insira o nome do arquivo do documento de índice, que geralmente é index.html.

O nome do documento de índice diferencia letras maiúsculas de minúsculas e deve corresponder exatamente ao nome do arquivo do documento de índice HTML do qual você planeja fazer upload para o bucket do S3. Quando você configura um bucket para hospedagem de site, deve especificar um documento de índice. O Amazon S3 retorna esse documento de índice quando as solicitações são feitas para o domínio raiz ou alguma subpasta.



Para fornecer seu próprio documento de erros personalizado para erros da classe 4XX, em Error document (Documento de erros), insira o nome de arquivo do documento de erros personalizado.

O nome do documento de erro diferencia letras maiúsculas de minúsculas e deve corresponder exatamente ao nome do arquivo do documento de erro HTML do qual você planeja fazer upload para o bucket do S3. Se você não especificar um documento de erro personalizado e ocorrer um erro, o Amazon S3 retornará um documento de erro HTML padrão.



(Opcional) Se você quiser especificar regras avançadas de redirecionamento em Redirection rules (Regras de redirecionamento), use JSON para descrevê-las.

Por exemplo, você pode encaminhar solicitações condicionalmente de acordo com nomes de chave de objeto ou prefixos específicos na solicitação. Para obter mais informações, consulte Configurar regras de redirecionamento para usar redirecionamentos condicionais avançados.



Selecione Save changes.<br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/exercicios/2-exbucket.png)

O Amazon S3 permite a hospedagem estática de sites para seu bucket. Na parte inferior da página, em Static website hosting (Hospedagem estática de sites), você verá o endpoint do site do seu bucket.



Em Static website hosting (Hospedagem de sites estáticos), copie o endpoint informado.

O Endpoint é o endereço do site do Amazon S3 para o bucket.  Informe o endereço na barra de navegação de seu navegador para testar o resultado.
<br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/exercicios/7-exbucket.png)



Etapa 3: editar as configurações do Bloqueio de acesso público


Por padrão, o Amazon S3 bloqueia o acesso público à sua conta e aos seus buckets. Se quiser usar um bucket para hospedar um site estático, use estas etapas para editar as configurações de bloqueio de acesso público.



No Console, busque pelo serviço S3.

Escolha o nome do bucket configurado como um site estático.

Escolha Permissions (Permissões).

Em Block public access (bucket settings) (Bloqueio de acesso público (configurações de bucket), escolha Edit (Editar).

Desmarque Block all public access (Bloquear todo acesso público) e escolha Save changes (Salvar alterações).
<br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/exercicios/3-exbucket.png)

O Amazon S3 desativa as configurações do bloqueio de acesso público para seu bucket. Para criar um site público e estático, você também pode ter que editar as configurações de Bloqueio de acesso público para sua conta antes de adicionar uma política de bucket. Se as configurações da conta para bloquear acesso público estiverem ativadas no momento, você verá uma observação em Block public access (bucket settings) (Bloqueio de acesso público (configurações de bucket)).



Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível


Depois de editar as configurações do bloqueio de acesso público do S3, é possível adicionar uma política de bucket para conceder acesso público de somente leitura ao bucket. Ao conceder um acesso público de leitura, qualquer pessoa na Internet poderá acessar seu bucket.

Em Buckets, escolha o nome do seu bucket.

Escolha Permissions (Permissões).

Em Bucket Policy (Política de bucket), escolha Edit (Editar).

Para conceder acesso público de leitura ao site, copie a política de bucket a seguir e cole-a no Bucket policy editor (Editor de política de bucket).

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::Bucket-Name/*"
            ]
        }
    ]
}
No JSON acima, substitua, na seção Resource, o valor de Bucket-Name para o nome do seu bucket.

Na política de bucket do exemplo anterior, Bucket-Name é um espaço reservado para o nome do bucket. Para usar essa política de bucket com seu próprio bucket, você deve atualizar esse nome para corresponder ao nome do seu bucket.



Selecione Save changes. <br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/exercicios/4-exbucket.png)

Uma mensagem é exibida indicando que a política de bucket foi adicionada com sucesso.

Se você vir um erro que diz Policy has invalid resource, confirme se o nome do bucket na política de bucket corresponde ao nome do seu bucket. Se você receber uma mensagem de erro e não puder salvar a política do bucket, verifique suas configurações de acesso público para confirmar que você permite acesso público ao bucket.



Etapa 5: Configurar um documento de índice


Quando você habilita a hospedagem de sites estáticos para seu bucket, deve informar o nome do documento de índice (por exemplo, index.html). Naturalmente, o arquivo informado deverá estar presente no bucket para que a configuração tenha efeito.



Vamos aos passo para configuração do documento de índice:



Criar um arquivo local (sua máquina) com o nome index.html . O conteúdo do arquivo deverá ser (atente-se para o atributo href do link, pois ele deverá apontar para o arquivo CSV):

<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>Home Page do meu WebSite - Tutorial de S3</title>
</head>
<body>
  <h1>Bem-vindo ao meu website</h1>
  <p>Agora hospedado em Amazon S3!</p>
  <a href="nome do arquivo CSV a ser baixado">Download CSV File</a> 
</body>
</html>
Salvar as alterações.

O nome do documento de índice deve corresponder exatamente ao nome do documento de índice que você inseriu na caixa de diálogo Hospedagem de site estático. O nome do documento de índice diferencia maiúsculas de minúsculas. Por exemplo, se você informou index.html na configuração do bucket, seu documento de índice também deverá ser index.html (e não Index.html, por exemplo).



No Console, busque pelo serviço S3.

Na lista Buckets, selecione o nome do bucket que você configurou hospedagem de conteúdo estático.

Para fazer upload do documento de índice para o bucket, siga um destes procedimentos:

Arraste e solte o arquivo de índice na listagem de buckets do console.

Escolha Upload (Fazer upload) e siga as instruções para escolher e fazer upload do arquivo de índice.

Crie uma pasta chamada dados e, após, faça upload do conteúdo do site (arquivo CSV) para ela.
<br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/exercicios/5-exbucket.png)

Etapa 6: configurar documento de erros


Depois de habilitar a hospedagem de sites estáticos para seu bucket, faça upload para o bucket de um arquivo HTML para notificação de erros.  Veja quais são os passos:



Crie um documento de erro com o nome 404.html.

Salve o arquivo localmente.

O nome do documento de erros diferencia maiúsculas e minúsculas e deve corresponder exatamente ao nome que você insere ao habilitar a hospedagem estática do site. Por exemplo, se você inserir 404.html como o nome do Error document (Documento de erro) na caixa de diálogo Static website hosting (Hospedagem de site estático), o nome de arquivo do documento de erro também deve ser 404.html.



No Console, busque pelo serviço S3.

Na lista Buckets, selecione o nome do bucket que você configurou hospedagem de conteúdo estático.

Para fazer upload do documento de erros para o bucket, siga um destes procedimentos:

Arraste e solte o arquivo de índice na listagem de buckets do console.

Escolha Upload (Fazer upload) e siga as instruções para escolher e fazer upload do arquivo de índice.



Etapa 7: testar o endpoint do site


Depois de configurar a hospedagem de site estático para seu bucket, você pode testá-lo em seu navegador. Para tal, siga os passos a seguir:



No Console, busque pelo serviço S3.

Na lista Buckets, selecione o nome do bucket que você configurou hospedagem de conteúdo estático.

Escolha Properties (Propriedades).

Na parte inferior da página, em Static website hosting (Hospedagem estática de sites), escolha seu Bucket website endpoint (Endpoint de site do Bucket). Seu documento de índice é aberto em uma janela separada do navegador.

Agora você tem um site hospedado no Amazon S3. Esse site está disponível publicamente no endpoint de site do Amazon S3. Você pode também ter um domínio, como example.com, para exibir o conteúdo do site que criou. Neste caso, é preciso executar etapas adicionais.
<br>
![Diagrama](https://github.com/rafaelkabata/ProgramaBolsasPB/blob/main/Sprint%206/exercicios/6-exbucket.png)
