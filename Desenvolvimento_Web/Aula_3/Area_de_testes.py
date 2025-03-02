import os
import time
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
        elif valor < valor_conta:
            print(f'Total das compras: {valor}\nResultado das compras: {valor_conta}\n Compras feitas com Consciência  ')
        break

                 