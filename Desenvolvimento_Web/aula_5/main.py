from fastapi import FastAPI
from routes.paths import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(router, host="192.168.56.1", port=200)