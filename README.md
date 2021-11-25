Para instalar os módulos necessários para executar o projeto, execute o comando pip install -r requirements.txt

Para executar a rota, digite os comandos no CMD: set FLASK_APP=routes e depois flask run ou no Powershell: $env:FLASK_APP = "routes" e por fim flask run

Após iniciar o servidor, a rota a ser consumida é a /informacoesNotebooks, é uma rota do tipo GET, que retorna um JSON contendo um array com as informações dos notebooks e seus preços, ordenados do menor para o maior preço.
