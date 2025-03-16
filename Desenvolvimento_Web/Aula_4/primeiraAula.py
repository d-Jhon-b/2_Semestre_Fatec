def somar_dois_numros(num1, num2):
    return num1 + num2

def saudacao(nome, saudacao="olá"):
    return f"{saudacao}, {nome}"
# print(saudacao("rodrigo 1"))
# print(saudacao("turma", "boa tarde 2"))


    #         Sobre chamada de parametros


    # quando uma função recebe parametros para sua inicialização, eles podems ser obrigatorios ou não
    # quando um parametro é obrigatorio, ele deve ser passado na chamada da função
    # quando um parametro não é obrigatorio, ele deve ser passado com um valor padrão
    # parametros não obrigatorios devem ser declarados após os obrigatorios

def receber_muitos(n1,n2,n3,n4,n5,n6=0):
    return f"{n1},{n2},{n3},{n4},{n5},{n6}"
# print(receber_muitos(1,2,3,4,5))


    #         Sobre parametros indefinidos
    # O atributo *Args é utilizado para receber um numero indefinido de parametros

def receber_muitos_args(*args):
  return F"{args[0]}{args[1]}{args[2]}"

#     podemos acessar um parametro especifico passando o indice dele na chamada da função
# print(receber_muitos_args(1,2,3,4,5,6,7,8,9,10))

    #         Sobre parametros nomeados
    # O atributo **Kwargs é utilizado para receber um numero indefinido de parametros nomeados

def receber_muitos_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
    return f"{kwargs['nome']} {kwargs['idade']}"
# receber_muitos_kwargs(nome="rodrigo", idade=28, cidade="são paulo")


def externo():
    contador = 0

    def interna():
        nonlocal contador
        #sobre nonlocal
        contador += 1

    interna()
    return contador
# print(externo())

# Funções aninhadas(nested functions) e closures

# password_input = input("Insira o a senha:")
# user_input = input("Insira o nome do usuario:")
def autenticator():
   def validar_credenciais(user_input, password_input):
       return user_input =="admin" and password_input=="1234"
   if validar_credenciais(user_input, password_input):
       return "acesso permitido"
   else:
       return "Acesso negado"
# print(autenticator())

def autenticator(usuario, senha):
   def validar_credenciais(usuario, senha):
       return usuario =="admin" and senha=="1234"
   if validar_credenciais(usuario, senha):
       return "acesso permitido"
   else:
       return "Acesso negado"
# print(autenticator("admin", "1234"))



    #funções logicas
def multiplicacao(*args):
    return args[0] * args[3](args[1], args[2]) 
def somar(num1, num2):
    return num1+num2
some = somar
#print(    multiplicacao(3, 5, 6, some)      )

        #função lambda(funções anonimas)
# quadrado = lambda x: x **2
# print(quadrado(4))

# def verificar_pares(num):
#     return num %2 == 0

# numero_par = lambda num: (num%2) == 0
# print(f"Resultado: {numero_par(16)}") 


