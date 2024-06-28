# Projeto empresa e produtos

Esse projeto tem o intuito de colocar em prática alguns conhecimentos em django, como uso de api para auto completar os endereços de um funcionario cadastrado no sistema, como a ideia de criar um dashboard para a apresentação de indicadores de TI.


## Como colocar o projeto para rodar.

- Clone o projeto.


```bash
 git clone https://github.com/kemuelkesley/empresa_sidebar.git
```
## Abra o terminal do vscode ou powershell e execute esses comandos.


- Crie um ambiente
```bash
  virtualenv env 
```
ou 
````bash
 python -m venv env
````
- Ativando o ambiente no windows:
````bash
env/script/activate
````

- Ativando o ambiente no Linux:
````bash
source/bin/activate
````

- Instalar o requirements.txt/bibliotecas
````bash
pip install -r requirements.txt
````

- Instalar oas migrações (tabelas do banco de dados SQLite) que já vem com o django.
````bash
python manage.py migrate
````

- Instalar oas migrações (tabelas do banco de dados SQLite) que já vem com o django.
````bash
python manage.py migrate
````

- Criando um super usuario.
````bash
python manage.py createsuperuser
````

- Depois de ter criado um usuario, rode o servidor
````bash
python manage.py runserver
````
Ele vai rodar no:
````bash
http://127.0.0.1:8000/
````

- Acessar a area administrativa
````bash
http://127.0.0.1/admin
````

## Criando gênero e função dos trabalhadores da empresa
- Na area administrativa vá em gênero e crie.
- Faça também com as profissões
- Depois de cadastrado, vá para o http://127.0.0.1:8000/
- Cadastre um Funcionario, crie categorias, produtos e etc.
