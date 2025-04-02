import oracledb
import os
from dotenv import load_dotenv
load_dotenv()
# Substitua pelas suas credenciais e detalhes de conexão do Oracle
usuario_db = os.getenv("USUARIO") 
senha_db = os.getenv("SENHA")
host_db = os.getenv("HOST")
porta_db = os.getenv("PORTA")
sid = os.getenv("SID")   # Ou service_name, dependendo da sua configuração


def conectarBanco():
    try:
        conn = oracledb.connect(user=usuario_db, password=senha_db, host=host_db, port=porta_db, sid=sid)
        print("conexão realizada!")
        return conn
    except oracledb.Error as e:
        error, = e.args
        print(f"Erro ao conectar ao banco de dados Oracle: {e}")
        return None
    
