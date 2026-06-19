cardapio = {
    "x-bacon": 25.00,
    "x-burger": 20.00,
    "x-egg": 22.00,
    "refrigerante lata": 7.00,
    "água s/ gás": 5.00
}

lista_lanches = list(cardapio.keys())

pedidos = []
comanda = 0

print('=======================')
print('       Lanchonete      ')
print('=======================')
print('Olá, seja bem-vindo à nossa lanchonete!')


while True:
    print('\n1. Ver cardápio')
    print('2. Fazer pedido / Adicionar item')
    print('3. Remover item do pedido')
    print('4. Listar itens do pedido')
    print('5. Valor total do pedido')
    print('6. Cancelar operação\n')
    op = int(input('Digite o número da opção desejada:'))

    if op == 1:
        numero = 0
        for lanche in cardapio:
            preco = cardapio[lanche]
            print(f'{numero}. {lanche}: {cardapio[lanche]}')
            numero += 1
    elif op == 2:
        ped = int(input('Qual o número do item? '))
        lanche_escolhido = lista_lanches[ped]
        preco_do_lanche = cardapio[lanche_escolhido]
        pedidos.append(lanche_escolhido)
        comanda += preco_do_lanche
        print(f'pedidos: {pedidos}')
        print(f'comanda: {comanda}')
    elif op == 3:
        for i in range(len(pedidos)):
            print(i+pedidos[i])
        rem = int(input('Deseja remover qual item? '))
        















# cardapio = [
#     'x-bacon: R$ 25.00',
#     'x-burger: R$ 20.00',
#     'x-egg: R$ 22.00',
#     'refrigerante lata: R$ 7.00',
#     'água s/ gás: R$5.00'
# ]

# pedido = []

# while True:
#     if op == '1':
#         for i, item in enumerate(cardapio):
#             print(f'\n{i}.{item}')
        
#         des = int(input('\nO que deseja pra hoje? (0, 1, 2...) '))
        
#         if des == 0:
#             pedido.append(cardapio[0])
#             print(pedido)
#     elif op == '2':
#         print('Perfeito, o que gostaria?')

#     elif op == '7':
#         print('Operação cancelada. Obrigado por visitar nossa lanchonete!')
#         break