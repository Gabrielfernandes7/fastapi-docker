from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Request
from ..configuration.database import get_db
from sqlalchemy.orm import Session

from ..service.pedido_service import (
    criar_pedido, ler_todos_pedidos_service
)

pedido_router = APIRouter(prefix="/bovines", tags=["Pedidos"])

@pedido_router.get("/get-all/")
def get_todos_pedidos_controller(db: Session = Depends(get_db)):
    return ler_todos_pedidos_service(db)


@pedido_router.post("/create")
def post_criar_pedido_controller(pedido:str, descricao:str, db: Session = Depends(get_db)):
    return criar_pedido(pedido, descricao, db)