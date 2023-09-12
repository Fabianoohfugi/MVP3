from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from schemas import ComentarioSchema


class ProdutoSchema(BaseModel):
    
    nome: str = "Caneta"
    quantidade: Optional[int] = 1
    valor: float = 2.50


class ProdutoBuscaSchema(BaseModel):
    
    nome: str = "Teste"


class ListagemProdutosSchema(BaseModel):
    
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    
    id: int = 1
    nome: str = "caneta"
    quantidade: Optional[int] = 10
    valor: float = 2
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class ProdutoDelSchema(BaseModel):
    
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
