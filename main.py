from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.services.entregador_services import EntregadorService
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")
# Configuração do Jinja2
templates = Jinja2Templates(directory="src/templates")

# Rota para a página inicial
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

# Rota para o formulário de cadastro
@app.get("/cadastro", response_class=HTMLResponse)
async def mostrar_formulario_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

# Rota para processar o cadastro
@app.post("/cadastro", response_class=HTMLResponse)
async def cadastrar_entregador(
    request: Request,
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...)
):
    try:
        EntregadorService.criar_entregador(nome, data_nascimento, cpf, email)
        return templates.TemplateResponse("cadastro.html", {"request": request, "mensagem": "Entregador cadastrado com sucesso!"})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Rota para listar entregadores
@app.get("/listagem", response_class=HTMLResponse)
async def listar_entregadores(request: Request):
    entregadores = EntregadorService.listar_entregadores()
    return templates.TemplateResponse("listagem.html", {"request": request, "entregadores": entregadores})

# Rota para editar um entregador
@app.get("/edicao/{cpf}", response_class=HTMLResponse)
async def mostrar_formulario_edicao(request: Request, cpf: str):
    entregador = EntregadorService.buscar_entregador(cpf)
    if not entregador:
        raise HTTPException(status_code=404, detail="Entregador não encontrado.")
    return templates.TemplateResponse("edicao.html", {"request": request, "entregador": entregador})

@app.post("/edicao/{cpf}", response_class=HTMLResponse)
async def editar_entregador(
    request: Request,
    cpf: str,
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf_atualizado: str = Form(...),
    email: str = Form(...)
):
    try:
        # Atualiza o entregador
        EntregadorService.atualizar_entregador(cpf, nome, data_nascimento, cpf_atualizado, email)
        
        # Busca os dados ATUALIZADOS do entregador (usando o novo CPF, se alterado)
        entregador_atualizado = EntregadorService.buscar_entregador(cpf_atualizado)
        
        # Renderiza o template com os dados atualizados e a mensagem
        return templates.TemplateResponse(
            "edicao.html",
            {
                "request": request,
                "entregador": entregador_atualizado,  # Dados atualizados
                "mensagem": "Entregador atualizado com sucesso!"
            }
        )
    
    except ValueError as e:
        # Em caso de erro, busca o entregador original para mostrar o formulário
        entregador = EntregadorService.buscar_entregador(cpf)
        return templates.TemplateResponse(
            "edicao.html",
            {
                "request": request,
                "entregador": entregador,
                "mensagem": str(e)  # Mensagem de erro
            },
            status_code=400
        )
        

@app.get("/busca", response_class=HTMLResponse)
async def buscar_entregador(request: Request, cpf: str = None):
    if cpf:
        entregador = EntregadorService.buscar_entregador(cpf)
        if not entregador:
            return templates.TemplateResponse("busca.html", {"request": request, "mensagem": "Entregador não encontrado."})
        return templates.TemplateResponse("busca.html", {"request": request, "entregador": entregador})
    return templates.TemplateResponse("busca.html", {"request": request})

