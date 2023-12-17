# meu desafio/ dan list v2
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

carrinho = []  
while True:
    numero_inserido = int(input('Digite um número de 01 a 20 para adicionar ao carrinho (0 para finalizar): '))
    
    if numero_inserido == 0:
        break  

    if 1 <= numero_inserido <= 20:
        produtoreferente = produtos[(numero_inserido - 1) * 2]
        carrinho.append((produtoreferente, produtos[numero_inserido * 2 - 1]))
        print(f'{produtoreferente} adicionado ao carrinho.')

    else:
        print('Número inválido. Digite um número entre 01 e 20.')

finalizar = input('Você finalizou suas compras? (S/N): ').upper()
if finalizar == 'S':
    print('\nLISTAGEM DE PREÇOS')
    print('-' * 30)
    total = 0
    for item, preco in carrinho:
        print(f'{item:.<30} R$:{preco:>7.2f}')
        total += preco
    print('-' * 30)
    print(f'Total a pagar: R${total:.2f}')
else:
    print('Compra cancelada.')
