def media(soma, tamanho_lista):
    return soma/tamanho_lista
    

soma = 0
lista_alunos = [10,8,7,6,9]
tamanho_lista = len(lista_alunos) 
for nota in lista_alunos:
    soma = nota + soma

print(media(soma, tamanho_lista))