from fastapi import FastAPI
from src.controllers import entregador_controller

app = FastAPI()

app.include_router(entregador_controller.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

