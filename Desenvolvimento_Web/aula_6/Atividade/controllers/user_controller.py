from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import user_model



user_model.criar_tabela()

def mostrar_usuarios(request: Request):
    templates = Jinja2Templates(directory="templates")
    usuarios = user_model.listar_usuarios()
    return templates.TemplateResponse("index.html", {"request": request, "usuarios":usuarios })

# def exibir_dados_formulario(request: Request, nome: str, email: str):
#     templates = Jinja2Templates(directory="templates")
#     return templates.TemplateResponse("exibir_dados.html", {"request": request, "nome": nome, "email": email})

# def mostrar_edicao(request: Request, user_id):
#     templates = Jinja2Templates(directory="templates")
#     usuario = user_model.buscar_usuario_por_id(user_id)
#     usuarios = user_model.listar_usuarios()
#     return templates.TemplateResponse("editar",{"request:": request,"usuario": usuario, "usuarios": usuarios})

async def cadastrar_usuario(request: Request, nome:str = Form(...), email: str = Form(...)):
    user_model.inserir_usuario(nome, email)
    return RedirectResponse("/", status_code=201)

async def excluir_usuario(user_id: int):
    user_model.excluir_usuario(user_id)
    return RedirectResponse("/", status_code=303)

async def atualizarUsuarios(request: Request, user_id: int, nome:str = Form(...), email:str = Form(...)):
    user_model.atualizar_usuario(user_id, nome, email)
    return RedirectResponse("/", status_code=201)



