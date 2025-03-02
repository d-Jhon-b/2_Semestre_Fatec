import os

input_option_user = True

while input_option_user:
    input_option_user = input('Deseja ir para qual atividade?\n[1]Atividade 1\n[2]Atividade 2\n[3]Atividade 3\n[4]Atividade 4\n[5]Sair\n')
    os.system('cls')
    if(input_option_user == '1'):
        #Exercício 1: Limpeza e Substituição de Texto
        input_res_user = ''
        while input_res_user != '0':
            input_user = input('Insira uma frase\n')
            stripped_input=input_user.strip()
            print(f"A frase sem espaços adicionais é: \n{(stripped_input).replace(',', '.')}")
            
            input_res_user = input('deseja repetir o processo?\n[1]Sim\n[0]Não\n')
            if(input_res_user == '1'):
                os.system('cls')
                continue
            elif input_res_user == '0':
                os.system('cls')
                break

    elif(input_option_user == '2'):
        #Exercício 2: Contagem de Palavras com Loop for
        input_res_user = ''
        while input_res_user != '0':
            frase = input('insira uma frase: ')
            frase_min = frase.lower()
            frase_split = frase_min.split()

            contador = 0
            print(f'Itens da frase:\n{frase_split}')
            print('Itens que começam com a letra A')
            #loop for para contagem de palavras
            for item in frase_split:
                if((item.find('a'))==0):   
                    contador += 1
                    print(f'{contador}:{item}')
                else:
                    continue
            print(f'{contador} itens encontrados.\n')

            input_res_user = input('deseja repetir o processo?\n[1]Sim\n[0]Não\n')
            if(input_res_user == '1'):
                os.system('cls')
                continue
            elif input_res_user == '0':
                os.system('cls')
                break

    elif(input_option_user == '3'):
        input_res_user = ''
        while input_res_user != '0':
            lista_content = ['camiseta', 'calça', 'cueca','sapato']
            lista_valores = [100, 50, 200, 25]

            carrinho = []
            contador = 0
            option = True
            while option:
                for i in range(len(lista_content)):
                    print(f'item {i} {lista_content[i]} \n valor: {lista_valores[i]}')
                    contador+=1
                input_user= input(f'Qual dos itens acima deseja escolher?\nDigite [SAIR] para finalizar compra\n')
                input_user_lower = input_user.lower()
                os.system('cls')
                if(input_user_lower== '0'):
                    item_carrinho = lista_content[0], lista_valores[0]
                    carrinho.append(item_carrinho)    
                    print(f'lista de itens:\n{carrinho}')  
                elif input_user_lower== '1':
                    item_carrinho = lista_content[1], lista_valores[1]
                    carrinho.append(item_carrinho)    
                    print(carrinho)  

                elif input_user_lower== '2':
                    item_carrinho = lista_content[2], lista_valores[2]
                    carrinho.append(item_carrinho)    
                    print(carrinho)  

                elif input_user_lower== '3':
                    item_carrinho = lista_content[3], lista_valores[3]
                    carrinho.append(item_carrinho)    
                    print(carrinho)  
                    
                elif input_user_lower == 'sair':
                    os.system('cls')
                    print('itens comprados:')
                    valor = 0
                    for produto in range(len(carrinho)):
                        print(carrinho[produto])
                        valor += carrinho[produto][1]
                    print(valor)
                    break
            break
    elif(input_option_user == '4'):
        input_res_user = ''
        while input_res_user != '0':
            lista_content = ['camiseta', 'calça', 'cueca','sapato']
            lista_valores = [100, 50, 200, 25]
            lista_qtde = [10, 10, 10, 10]

            carrinho = []
            contador = 0
            option = True

            valor_conta =1000

            while option:
                for i in range(len(lista_content)):
                    print(f'item {i} {lista_content[i]} valor: {lista_valores[i]}  Quantidade: {lista_qtde[i]}')
                    contador+=1
                input_user= input(f'\nQual dos itens acima deseja escolher?\nDigite [SAIR] para finalizar compra\nDigite [LISTA] para ver a lista de itens\n')
                input_user_lower = input_user.lower()
                os.system('cls')
                if(input_user_lower== '0'):
                    if lista_qtde[0] > 0:
                        item_carrinho = lista_content[0], lista_valores[0]
                        carrinho.append(item_carrinho)    
                        lista_qtde[0]-=1
                    else:
                        print('Quantidade insuficiente: ')

                elif input_user_lower== '1':
                    if lista_qtde[1]>0:
                        item_carrinho = lista_content[1], lista_valores[1]
                        carrinho.append(item_carrinho) 
                        lista_qtde[1]-=1   
                    else:
                        print('Quantidade insuficiente')

                elif input_user_lower== '2':
                    if lista_qtde[2]>0:
                        item_carrinho = lista_content[2], lista_valores[2]
                        carrinho.append(item_carrinho)
                        lista_qtde[2]-=1   
                    else:
                        print('Quantidade insuficiente')

                elif input_user_lower== '3':
                    if lista_qtde[3]>0:
                        item_carrinho = lista_content[3], lista_valores[3]
                        carrinho.append(item_carrinho)  
                        lista_qtde[3]-=1   
                    else:
                        print('Quantidade insuficiente')

                elif input_user_lower == 'lista':
                    os.system('cls')
                    print('itens na lista: ')
                    for item_list in carrinho:
                        print(item_list) 
                    time.sleep(3)

                elif input_user_lower == 'sair':
                    os.system('cls')
                    print('itens comprados:')
                    valor = 0
                    for produto in range(len(carrinho)):
                        print(carrinho[produto])
                        valor += carrinho[produto][1]
                    valor_conta -= valor
                    if valor > valor_conta:
                        print(f'Total das compras: {valor}\nResultado das compras: {valor_conta}\n Ficou devendo XD')
                        option = False
                        break
                    elif valor <= valor_conta:
                        print(f'Total das compras: {valor}\nResultado das compras: {valor_conta}\n Compras feitas com Consciência  ') 
                        option = False
                        break
            break
        break

    elif(input_option_user == '5'):
        input_option_user =False
        