from ..configuration.database import Base, engine
from sqlalchemy import Column, Integer, String

class PedidoModel(Base):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String)
    descricao = Column(String)

    def __init__(self, produto, descricao):
        self.produto = produto
        self.descricao = descricao

Base.metadata.create_all(bind = engine)
