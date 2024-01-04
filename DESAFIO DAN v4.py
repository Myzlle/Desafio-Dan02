from datetime import datetime

# Função para validar CPF
def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

# Função para validar a data de nascimento
def validar_data_nascimento(data_nascimento):
    try:
        return datetime.strptime(data_nascimento, "%d/%m/%Y")
    except ValueError:
        return None

# Função para exibir as opções disponíveis
def exibir_opcoes(opcoes):
    for i, (item, preco) in enumerate(opcoes.items(), start=1):
        print(f"{i}. {item}: R$ {preco:.2f}")

# Função para selecionar um item e adicionar ao carrinho
def selecionar_item(carrinho, itens):
    while True:
        numero_item = int(input("Digite o número do item desejado (0 para sair): "))
        
        if numero_item == 0:
            break

        if 1 <= numero_item <= len(itens):
            item_selecionado = list(itens.keys())[numero_item - 1]
            carrinho.append((item_selecionado, itens[item_selecionado], 1))
            print(f'{item_selecionado} adicionado ao carrinho.')
            
            mais_item = input("Deseja selecionar mais itens? (S/N): ").upper()
            if mais_item != 'S':
                break
        else:
            print(f'Número inválido. Digite um número entre 1 e {len(itens)}.')

# Função para selecionar bebidas alcoólicas
def selecionar_bebidas(carrinho, bebidas_alcoolicas):
    print("\n=== Lista de Bebidas Alcoólicas ===")
    exibir_opcoes(bebidas_alcoolicas)

    while True:
        numero_bebida = int(input("Digite o número da bebida desejada (0 para sair): "))
        
        if numero_bebida == 0:
            break

        if 1 <= numero_bebida <= len(bebidas_alcoolicas):
            bebida_selecionada = list(bebidas_alcoolicas.keys())[numero_bebida - 1]
            carrinho.append((bebida_selecionada, bebidas_alcoolicas[bebida_selecionada], 1))
            print(f'{bebida_selecionada} adicionada ao carrinho.')
            
            mais_bebida = input("Deseja selecionar mais bebidas? (S/N): ").upper()
            if mais_bebida != 'S':
                break
        else:
            print(f'Número inválido. Digite um número entre 1 e {len(bebidas_alcoolicas)}.')

# Função para selecionar frutas
def selecionar_frutas(produtos):
    print("\n=== Lista de Frutas ===")
    carrinho_frutas = []

    for i, (fruta, preco) in enumerate(zip(produtos[::2], produtos[1::2]), start=1):
        print(f"{i}. {fruta}: R$ {preco:.2f}")

    while True:
        numero_fruta = int(input("Digite o número da fruta desejada (0 para sair): "))

        if numero_fruta == 0:
            break

        if 1 <= numero_fruta <= len(produtos) // 2:
            fruta_selecionada = produtos[(numero_fruta - 1) * 2]
            preco_fruta = produtos[numero_fruta * 2 - 1]
            quantidade_fruta = int(input(f"Digite a quantidade de {fruta_selecionada} desejada: "))
            carrinho_frutas.append((fruta_selecionada, preco_fruta, quantidade_fruta))
            print(f'{quantidade_fruta} {fruta_selecionada} adicionada(s) ao carrinho.')

            mais_fruta = input("Deseja selecionar mais frutas? (S/N): ").upper()
            if mais_fruta != 'S':
                break
        else:
            print(f'Número inválido. Digite um número entre 1 e {len(produtos) // 2}.')

    return carrinho_frutas

# Função para exibir o resumo do carrinho
def exibir_resumo_carrinho(carrinho, nome_cliente, lista_cliente):
    if carrinho:
        print("\n=== Resumo do Carrinho ===")
        for item, preco, quantidade in carrinho:
            total_item = preco * quantidade
            print(f"{quantidade} {item} - R$ {preco:.2f} cada - Total: R$ {total_item:.2f}")

        total_carrinho = sum(preco * quantidade for _, preco, quantidade in carrinho)
        print(f"\nTotal a pagar: R$ {total_carrinho:.2f}")

        if nome_cliente in lista_cliente:
            total_carrinho *= 0.9
            print(f"Cliente VIP! Total com desconto: R$ {total_carrinho:.2f}")

        print("\nObrigado por sua compra!")
    else:
        print("Carrinho vazio. Nenhum item selecionado.")

# Função principal
def main():
    # Lista de produtos
    produtos = ('Banana', 1.20, 'Maçã', 2.00, 'Laranja', 4.55, 'Abacaxi', 7.86, 'Melancia', 9.90, 'Morango', 15.99,
                'Uva', 10, 'Pêra', 12, 'Mamão', 5.55, 'Kiwi', 15.66, 'Pêssego', 11.11, 'Ameixa', 13.10, 'Cereja', 25.00,
                'Limão', 3.75, 'Abacate', 7.80, 'Tomate', 4.46, 'Cenoura', 1.99, 'Batata', 5.71, 'Brócolis', 8.99, 'Pão', 2.00)

    # Lista de bebidas alcoólicas
    bebidas_alcoolicas = {
        'Vodka (garrafa 750ml)': 40.0, 'Whisky Escocês (garrafa 750ml)': 50.0, 'Gin (garrafa 750ml)': 35.0,
        'Rum (garrafa 750ml)': 25.0, 'Tequila (garrafa 750ml)': 30.0, 'Vinho Branco (garrafa 750ml)': 15.0,
        'Champagne (garrafa 750ml)': 60.0, 'Cerveja Artesanal (lata 330ml)': 8.0, 'Licor de Café (garrafa 500ml)': 18.0,
        'Absinto (garrafa 750ml)': 55.0
    }

    # Lista de clientes VIP
    lista_cliente = ['BRUNO MARCELO', 'PAULA SIMONE', 'HUGO MOURA', 'ALEXANDRE MOURA', 'LEANDRO MENDOZA',
                     'BEATRIZ GABRIELA', 'MATHEUS GALDINO', 'KEVIN MELO', 'LUIZ CARLOS', 'DANIEL CABRAL']

    # Solicita o nome do cliente
    nome_cliente = str(input('Digite o seu nome: ')).upper()
    carrinho = []

    # Pergunta se o cliente deseja incluir o CPF na nota
    incluir_cpf = input("Deseja incluir o CPF na nota? (S/N): ").upper()

    if incluir_cpf == 'S':
        while True:
            cpf = input("Digite o CPF: ")
            if validar_cpf(cpf):
                break
            else:
                print("CPF inválido. Por favor, digite novamente.")

    # Solicita e valida a data de nascimento
    while True:
        data_nascimento = input("Digite a data de nascimento (no formato DD/MM/AAAA): ")
        data_nascimento_dt = validar_data_nascimento(data_nascimento)

        if data_nascimento_dt:
            break
        else:
            print("Data de nascimento inválida. Por favor, digite novamente.")

    # Calcula a idade do cliente
    hoje = datetime.now()
    idade = hoje.year - data_nascimento_dt.year - ((hoje.month, hoje.day) < (data_nascimento_dt.month, data_nascimento_dt.day))

    # Se o cliente é maior de idade, mostra a lista de bebidas alcoólicas
    if idade >= 18:
        print("Parabéns, você é maior de idade. Aqui está a lista de bebidas alcoólicas:")
        selecionar_bebidas(carrinho, bebidas_alcoolicas)
    else:
        print("Você é menor de idade. A lista de bebidas alcoólicas é inválida para você.")

    # Se o cliente é maior de idade ou já finalizou a seleção de bebidas, permite a seleção de frutas
    if idade >= 18 or not bebidas_alcoolicas:
        carrinho_frutas = selecionar_frutas(produtos)
        carrinho.extend(carrinho_frutas)

    # Exibe o resumo do carrinho
    exibir_resumo_carrinho(carrinho, nome_cliente, lista_cliente)

# Chama a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
