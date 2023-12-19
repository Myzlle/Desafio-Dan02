# meu desafio/ dan list v2

# Definição dos produtos com seus nomes e preços
produtos = ('Banana', 1.20,
            'Maçã', 2.00,
            'Laranja', 4.55,
            'Abacaxi', 7.86,
            'Melancia', 9.90,
            'Morango', 15.99,
            'Uva', 10,
            'Pêra', 12,
            'Mamão', 5.55,
            'Kiwi', 15.66,
            'Pêssego', 11.11,
            'Ameixa', 13.10,
            'Cereja', 25.00,
            'Limão', 3.75,
            'Abacate', 7.80,
            'Tomate', 4.46,
            'Cenoura', 1.99,
            'Batata', 5.71,
            'Brócolis', 8.99,
            'Pão', 2.00)

# Armazenamento dos clientes que irão ganhar os 10%
lista_cliente = ['BRUNO MARCELO', 'PAULA SIMONE', 'HUGO MOURA', 'ALEXANDRE MOURA', 'LEANDRO MENDOZA',
                 'BEATRIZ GABRIELA', 'MATHEUS GALDINO', 'KEVIN MELO', 'LUIZ CARLOS', 'DANIEL CABRAL']

# Solicita o nome do cliente
nome_cliente = str(input('Digite o seu nome:    ')).upper()

# Váriável null
carrinho = []  

while True:
    # Início do programa
    numero_inserido = int(input('Digite um número de 01 a 20 para adicionar ao carrinho (0 para finalizar): '))

    # Verifica se o número inserido é 0 para encerrar o loop
    if numero_inserido == 0:
        break  

    # Verifica se o número está dentro do intervalo válido
    if 1 <= numero_inserido <= 20:
        produtoreferente = produtos[(numero_inserido - 1) * 2]
        carrinho.append((produtoreferente, produtos[numero_inserido * 2 - 1]))
        print(f'{produtoreferente} adicionado ao carrinho.')

    else:
        print('Número inválido. Digite um número entre 01 e 20.')

# Pergunta se o cliente finalizou suas compras
finalizar = input('Você finalizou suas compras? (S/N): ').upper()

if finalizar == 'S':
    # Verifica se o cliente é VIP
    if nome_cliente in lista_cliente:
        print('\nLISTAGEM DE PREÇOS')
        print('-' * 30)
        total = 0

        # Imprime os itens e preços do carrinho com desconto de 10%
        for item, preco in carrinho:
            print(f'{item:.<30} R$:{preco:>7.2f}')
            total += preco
            print('-' * 30)

        # Imprime o total a pagar com desconto para clientes VIP
        print(f'Total a pagar: R${total * 0.9 :.2f}')
        print(f'Valor Total Das Suas é R$: {total}, Porém Por Ser Um ::CLIENTE VIP:: Seu Valor Será R$: {total * 0.9:.2f}')
    else:
        # Imprime os itens e preços do carrinho sem desconto
        print('\nLISTAGEM DE PREÇOS')
        print('-' * 30)
        total = 0
        for item, preco in carrinho:
            print(f'{item:.<30} R$:{preco:>7.2f}')
            total += preco
            print('-' * 30)
    
        # Imprime o total a pagar sem desconto para clientes não VIP
        print(f'Total a pagar: R${total:.2f}')
         
else:
    # Informa que a compra foi cancelada
    print('Compra cancelada.')
