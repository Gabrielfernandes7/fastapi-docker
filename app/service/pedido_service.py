from typing import Optional
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..model.pedido import PedidoModel
from ..configuration.database import get_db

def criar_pedido(produto: str, descricao: str, db: Session = Depends(get_db)):
    novo_pedido = PedidoModel(produto=produto, descricao=descricao)
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

def ler_todos_pedidos_service(db: Session = Depends(get_db)):
    todo_pedidos = db.query(PedidoModel).all()
    return todo_pedidos
