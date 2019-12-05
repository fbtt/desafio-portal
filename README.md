# Desafio - Data Engineer

### Passos para execução da aplicação:

- Clonar o repositório localmente
- Inserir o arquivo *twitter_credentials.json* (enviado por e-mail) no diretório .../desafio-portal
- Executar dentro do diretório .../desafio-portal os códigos na seguinte ordem:
	- get\_data\_twitter .py
	- treatment\_data\_twitter.py
	- get\_data\_google.py
	- treatment\_data\_google.py

### Funcionamento da aplicação:

- get\_data\_twitter.py: utiliza a API do Twitter para coletar os 1000 últimos tweets que contém a palavra *telemedicina*. Para cada tweet serão coletadas as seguintes informações:
	- Dados do usuário que tweetou.
	- Data e hora que o tweet foi publicado.
	- Conteúdo do tweet
Essas informações são salvas em .../desafio-portal/data/list_twitter_dict_responses.data

- treatment\_data\_twitter.py: abre os dados coletados do Twitter em .../desafio-portal/data/list_twittter_dict_responses.data e faz os seguintes procedimentos:
	- Calcula os usuários que mais twittaram, plota e salva o gráfico em .../desafio-portal/resultados/usuarios_que_mais_twittaram.png
	- Calcula o número de tweets por dia, plota e salva o gráfico em .../desafio-portal/resultados/numero_de_tweets_por_dia.png
	- Calcula o número de tweets por hora, plota e salva o gráfico em .../desafio-portal/resultados/numero_de_tweets_por_hora.png

- get\_data\_google .py: o código acessa as 100 primeiros URLs que o google apresenta ao pesquisar pela palavra *telemedicina* e salva as seguintes informações:
	- Posição de ordenação da URL pelo google
	- Código de status da requisição
	- URL completa do site
	- Conteúdo textual da URL
Essas informações são salvas em .../desafio-portal/data/list_google_dict_responses.data

- treatment\_data\_google.py: abre os dados coletados do Google em .../desafio-portal/data/list_google_dict_responses.data e faz os seguintes procedimentos:
	- Extrai os domínios das URLs
	- Calcula os domínio mais frequentes, plota e salva o gráfico em .../desafio-portal/resultados/dominios_mais_frequentes_google.png
	- Remove as stopwords *e, não, por, a, o, etc* dos conteúdos textuais
	- Calcula as palavras mais frequentes, plota e salva o gráfico em .../desafio-portal/resultados/paravras_mais_frequentes_google.png

### Bibliotecas utilizadas:

- pandas
- nltk
- os
- beautifulsoup
- requests
- twittersearch
- googlesearch
- matplotlib
- seaborn
- pickle
- json
- dateutil

### Contato

Estou à disposição através do e-mail: ferbattisti.eng@gmail.com