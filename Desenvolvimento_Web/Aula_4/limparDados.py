def limpar_dados(lista_de_palavras, blacklist):
    for palavra in blacklist:
        while palavra in lista_de_palavras:
            lista_de_palavras.remove(palavra)
    return lista_de_palavras