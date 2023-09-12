# MVP

Estre projeto se trata do  MVP da Disciplina **Desenvolvimento Back-end Avançado** PUC-rio EAD.

O projeto se trata de uma lista de materia escolar, possuindo uma API externa mostrando alguns produtos
e com uma API e um bando de dados.

------

# Como executar
 
 Primeiro é necessário ativar o ambiente virtual, no terminal do Visual Studio Code  digite
 o que está a baixo para criar o ambiente virtual:
 
 ```
  python -m venv venv
 ```
  
 Após a criação do ambiente virtual digite o que está a baixo para ativá-lo:
  
 ```
  venv/Scripts/Activate
 ```
 
 Depois que estiver com o ambiente virtual atiado, baixe o arquivo requirements.txt com o seguinte comando:
 
  ```
  pip install -r requirements.txt
 ```
 
 Se não consegguir com o comando acima, baixe todas manualmente com o comando 
  
 ```
 pip install 'nome da lib abaixo'
 ```
 ```
aniso8601
attrs
click
Flask
Flask-Cors
flask-openapi3
flask-restx
Flask-SQLAlchemy
greenlet
gunicorn
importlib-metadata
itsdangerous
Jinja2
jsonschema
MarkupSafe
nose2
pydantic
pyrsistent
pytz
six
SQLAlchemy
SQLAlchemy-Utils
typing_extensions
Werkzeug
zipp
Flask
sqlalchemy
sqlalchemy.orm
flask-openapi3
flask-restful
flask-swagger-ui
flask-swagger-ui

```
Depois que fizer os passos acima, rode o app.py e acesse no browser:

```
http://127.0.0.1:5000
```
# Como executar o docker
Para executar o projeto localmente usando o Docker, siga estas etapas:

**Certifique-se de ter o Docker instalado:**

   Certifique-se de que o Docker esteja instalado em sua máquina. Se você ainda não o possui instalado, siga as instruções em [Docker Installation Guide](https://docs.docker.com/get-docker/) para instalar o Docker.

   **Construa a Imagem Docker:**

    Abra um terminal no diretório raiz do projeto e execute o seguinte comando para construir a imagem Docker:

    ```
        docker build -t nome_da_sua_imagem:tag .
    ```
    Execute o container docker:

    ```
        docker run -p 5000:5000 nome_da_sua_imagem:tag
    ```
    Acesse a sua aplicação:

    ```
        http://localhost:5000
    ```






