import cx_Oracle 
#Apagar comentários: !!!

#import para biblioteca do sql Oracle

"""

    lembre de tirar suas credenciais do banco eu do Futuro !!!

"""

usuario_db = "c##atividadePython" #!!!
senha_db = "962266514" #!!! 
host_db = "localhost" #!!!
porta_db = 1522  # Porta padrão do Oracle : 1521 mas alterado para não atrapalhar o vsCode no run(Teste deu errado, o oracle continua atrapalhando o vsCode. Solução encontrada: "Finalizar as instancias que usam a porta 1521 e 1522 via gerenciador de tarefas. Apagar comentário !!!")
sid = "XE" #!!!

def conectar_Banco(usuario_db, senha_db, host_db, porta, sid):
    try:
        dsn_tns = cx_Oracle.makedsn(host_db, porta_db, sid=sid)
        conexao = cx_Oracle.connect(usuario_db, senha_db, dsn_tns)
        print("Conexão bem-sucedida!")
        return conexao
    except cx_Oracle.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None
    
def executar_consulta(conexao, sql):

    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except cx_Oracle.Error as erro:
        print(f"Erro ao executar a consulta: {erro}")
        return None


def desconectar_banco(conexao):
    if conexao:
        conexao.close()
        print("Conexão encerrada.")

        
conexao = conectar_Banco(usuario_db, senha_db, host_db, porta_db, sid)




#teste

# if conexao:
#     # Exemplo de consulta
#     sql = "SELECT * FROM ENGENHEIRO"
#     resultados = executar_consulta(conexao, sql)

#     if resultados:
#         for linha in resultados:
#             print(linha)



""" Modo antigo para sqlLite
import sqlite3
def conectar():
    return sqlite3.connect("banco.db")
"""

""" Modo novo para sql Oracle/sql developer

"""
