# Função de Verificação de Número Primo

# Criar uma função que receba um número e retorne True se o número for primo, e False se não for.
def verificar_num_primo(num):
    if num <= 1:
        return False
    flag = True
    for i in range(2, int(num/2)+1):
        if ((num%i)==0):
            flag = False
    return flag

# input_user= input("Insira um valor")
# print(verificar_num_primo(int(input_user)))



#Função Recursiva para Somar uma Lista
#Criar uma função recursiva que calcule a soma de todos os elementos de uma lista.
def calcular_sum_lista(lista):
    sum = 0
    for item in lista:
        sum += item 
    return sum

lista = [10,5,6,7,9,10,20,50]
# print(calcular_sum_lista(lista))


# Função para Contagem de Palavras
# Escrever uma função que receba uma string e conte o número de palavras.

def contar_palavras(frase):
    cont = 0
    cont_palavras = frase.split()
    for i in range(len(cont_palavras)):
        cont += 1
    return cont

# user_input = input("Insira a string de palavras: ")
# print(f"O numero de palavras contidas na frase são: {contar_palavras(user_input)}")


def receber_muitos_args(*args, **kwargs):
    # estava repetindo a "frase Argumentos posicionais, não nomeados:" 2 vezes XD 
    if args: #checa se existem argumentos posicionais.
        print("Argumentos posicionais, não nomeados: ")
        for arg in args:
            print(f"- {arg}")

    #Aqui também XD
    elif kwargs:
        print("Argumentos nomeados: ")
        for chave, valor in kwargs.items():
            print(f"chave: {chave} \r valor: {valor}")

receber_muitos_args("Informação 1", 123, True, 2, 34, "Jhon")
receber_muitos_args(valorA = "teste", valorB = "value", valorC = "value2",  animal1 = "lhama", animal2 = "leão" )

