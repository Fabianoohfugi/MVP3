from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from model import Base, Comentario

class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)

    
    comentarios = relationship("Comentario")

    def __init__(self, nome: str, quantidade: int, valor: float):
      
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
