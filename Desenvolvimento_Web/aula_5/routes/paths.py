from fastapi import APIRouter, Request
from typing import Union
from controllers.controller import hello_world
from controllers.setHtml import page_inicial

router = APIRouter()
@router.get("/view", response_model=None)
async def chamar_template(request: Request):
    return page_inicial(request)

@router.get("/")
def raed_root():
    return hello_world()

   
        
        #Forma direta de subir servidor

# @router.get("/")
# def inicial():
#     return {"menssage: ": "Olá, mundo com ZZZsssZ"}

@router.get("/items/{item_id}")
def funcao_com_parametros(item_id:int, q:Union[str, None]=None):
    return {"item_id":item_id, "q":q}

@router.post("/items")
async def create_item(item:dict):
    return {"message": "Recurso criado", "item":item}

@router.put("/items/{item_id}")
async def update_item(item_id: int, item:dict):
    return {"message": f"Recurso{item_id} atualizado", "item":item}

@router.delete("/items/{item_id}")
async def delete_item(item_id:int):
    return {"message": f"Recuso {item_id} removido"}
#fastapi dev main.py  (iniciar server)