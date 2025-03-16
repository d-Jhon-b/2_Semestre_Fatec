#importar todas as funções e variáveis do arquivo Operacoes.py
# import Operacoes
# resultado = Operacoes.somar(1,2)

# print(resultado)
#importar apenas uma ou mais de uma função ou variável do arquivo Operacoes.py
# from Operacoes import somar, multiplicar, idade
# print(somar(1,2))
# print(multiplicar(1,2))
# print(idade)

    ##Aplicando eliminação de itens (modularização)
# import lista_de_palavras as listaPalavras 
# import blackList
# from limparDados import limpar_dados

# lista = listaPalavras.palavras
# remove = blackList.blackList
# limpar_dados(lista, remove)


# print(limpar_dados(lista, remove))

    ##Estrutura de pacotes

#modularização com arquivos de diretorios externos
#modulos são arquivos python que podem ser importados em outros arquivos python
from calculadora import dividir, multiplicar, somar, subtrair
print(somar(10,2))