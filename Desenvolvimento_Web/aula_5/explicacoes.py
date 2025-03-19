from fastapi import FastAPI 
from typing import Union


        #Forma direta de subir servidor
app = FastAPI()
@app.get("/")
def inicial():
    return {"menssage: ": "Olá, mundo com ZZZsssZ"}

@app.get("/item/{item_id}")
def funcao_com_parametros(item_id:int, q:Union[str, None]=None):
    return {"item_id":item_id, "q":q}

#fastapi dev main.py  (iniciar server)

##Para enviar um valor para a string " q " (atributo opcional) você adiciona na url: /item/id?(objeto, no caso "q") = "(string desejada)"

#Usando http://127.0.0.1:8000/docs, você consegue vizualizar algumas anotações sobre o uso 

        #Maneira Alterna de gerar um server 

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="192.168.56.1", port=8000)