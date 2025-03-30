from database.db import conectar


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE usuarios (
    id NUMBER PRIMARY KEY,
    nome VARCHAR2(255) NOT NULL,
    email VARCHAR2(255) NOT NULL
        );
    """)

def inserir_usuario(nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("Insert into usuario (nome, email) values (?, ?)", (nome, email)) # "or" 1 = 1 and delete 
    conn.commit()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("select *from usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def excluir_usuario(user_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("delete from usuarios"           
    "where id = ?", (user_id,))

def buscar_usuario_por_id(user_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("delete *from usuarios where id = ? ", (user_id))
    usuario = cursor.fetchone()
    conn.close() 
    return usuario  

def atualizar_usuario(user_id, nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("update usuarios set nome= ?, email = ? where user_id = ? ",(nome, email, user_id))
    conn.commit()
    conn.close()