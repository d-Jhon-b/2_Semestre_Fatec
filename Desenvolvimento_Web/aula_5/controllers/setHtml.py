from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")
def page_inicial(request: Request):
    return templates.TemplateResponse("index.html",{
        "request": request,
        "title": "pagina inicial",
        "message": "Bem-vindo ao FastAPI com Templates"
    })

