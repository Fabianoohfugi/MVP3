from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify
from urllib.parse import unquote
import requests
from sqlalchemy.exc import IntegrityError
from model import Session, Produto
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

html_tag = Tag(name="HTML", description="Página do HTML")
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição, visualização, atualização e remoção de produtos à base")

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

@app.get('/external_api_data', tags=[home_tag])
def fetch_external_api_data():
    try:
        
        response = requests.get('https://fakestoreapi.com/products')

        
        if response.status_code == 200:
            
            data = response.json()
            return jsonify(data), 200  

        
        else:
            return {"message": "Failed to fetch external API data"}, response.status_code

    except Exception as e:
        return {"message": "An error occurred while fetching external API data"}, 500

@app.get('/produtos_combinados', tags=[produto_tag], responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos_combinados():
    """Obtém e combina produtos da API externa e da base de dados

    Retorna uma representação combinada dos produtos.
    """
    
    try:
        response = requests.get('https://fakestoreapi.com/products')
        if response.status_code == 200:
            produtos_externos = response.json()
        else:
            produtos_externos = []
    except Exception as e:
        produtos_externos = []

    
    session = Session()
    produtos_db = session.query(Produto).all()

    
    produtos_combinados = []

    for produto_db in produtos_db:
        
        produto_combinado = {
            "nome": produto_db.nome,
            "quantidade": produto_db.quantidade,
            "valor": produto_db.valor
        }
        produtos_combinados.append(produto_combinado)

    
    produtos_combinados.extend(produtos_externos)

    return jsonify(produtos_combinados), 200

@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    produto = Produto(
        nome=form.nome,
        quantidade=form.quantidade,
        valor=form.valor)
    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    try:
        session = Session()
        session.add(produto)
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 400

@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os Produto cadastrados

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    session = Session()
    produtos = session.query(Produto).all()

    if not produtos:
        return {"produtos": []}, 200
    else:
        logger.debug(f"{len(produtos)} produtos encontrados")
        return apresenta_produtos(produtos), 200

@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Deleta um Produto a partir do nome informado

    Retorna uma mensagem de confirmação da remoção.
    """
    produto_nome = unquote(unquote(query.nome))
    logger.debug(f"Deletando dados sobre produto: '{produto_nome}'")

    session = Session()

    
    produto = session.query(Produto).filter(Produto.nome == produto_nome).first()

    if produto:
        
        session.delete(produto)
        session.commit()
        logger.debug(f"Deletado produto: '{produto_nome}'")
        return {"message": "Produto removido", "id": produto_nome}

    
    error_msg = "Produto não encontrado :/"
    logger.warning(f"Erro ao deletar produto: '{produto_nome}', {error_msg}")
    return {"message": error_msg}, 404

@app.put('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def update_produto(query: ProdutoBuscaSchema, form: ProdutoSchema):
    """Atualiza as informações de um Produto existente

    Retorna uma representação atualizada do produto.
    """
    produto_nome = unquote(unquote(query.nome))
    logger.debug(f"Atualizando informações do produto #{produto_nome}")

    session = Session()

    
    produto = session.query(Produto).filter(Produto.nome == produto_nome).first()

    if produto:
        
        produto.nome = form.nome
        produto.quantidade = form.quantidade
        produto.valor = form.valor

        session.commit()

        logger.debug(f"Informações atualizadas para o produto #{produto_nome}")

        return apresenta_produto(produto), 200
    else:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao atualizar produto #'{produto_nome}', {error_msg}")
        return {"message": error_msg}, 404

if __name__ == '__main__':
    app.run(debug=True)
















