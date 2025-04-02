from fastapi import APIRouter, Request
from typing import Union
from controllers import user_controller

router = APIRouter()

@router.get("/")
def pagina_inicial(request: Request):
    return user_controller.mostrar_usuarios(request)

@router.post("/cadastrar")
async def cadastrar(request: Request):
    form = await request.form()
    return await user_controller.cadastrar_usuario(request, nome=form["nome"], email=form["email"])


@router.post("/mostrar")
async def MostrarUsers(request: Request):
    return user_controller.mostrar_usuarios(request)

# @router.put("/items/{item_id}")
# async def update_item(item_id: int, item: dict):
#     return {"message": f"Recurso {item_id} atualizado", "item": item}

# @router.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     return {"message": f"Recurso {item_id} removido"}