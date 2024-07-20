from fastapi import FastAPI

from app.controller.pedido_controller import pedido_router

app = FastAPI(title="API FastAPI Dockerizada")

app.include_router(pedido_router)
