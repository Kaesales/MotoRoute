from fastapi import FastAPI
from src.controllers import entrega_controller
from src.controllers import entregador_controller
from src.controllers import gerenciador_controller

app = FastAPI()

app.include_router(entregador_controller.router)
app.include_router(gerenciador_controller.router)
app.include_router(entrega_controller.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

