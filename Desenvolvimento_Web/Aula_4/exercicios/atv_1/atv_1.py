def contagem_palavras(user_input, dicionario_palavras):
    user_input_lower = user_input.lower()
    user_input_split = user_input_lower.split()
    for palavra in user_input_split:
        dicionario_palavras[palavra] = dicionario_palavras.get(palavra,0) + 1
    resultado_ordenado = []
    for palavra, contagem in dicionario_palavras.items():
        resultado_ordenado.append(f"{palavra}: {contagem}")

    return "\n".join(resultado_ordenado)

   