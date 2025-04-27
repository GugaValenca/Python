def cadastro_produtos():
    produtos = {}
    
    while True:
        nome = input("Digite o nome do produto (ou 'sair' pra terminar): ").lower()
        if nome == 'sair':
            break
        preco = float(input(f"Digite o preço do produto '{nome}': "))
        produtos[nome] = preco

    return produtos

def consultar_produto(produtos):
    nome = input("Digite o nome do produto que deseja consultar: ").lower()
    preco = produtos.get(nome)
    if preco is not None:
        print(f"O preço do produto '{nome}' é R${preco:.2f}")
    else:
        print("Produto não encontrado, visse?")

# Teste
# produtos_cadastrados = cadastro_produtos()
# consultar_produto(produtos_cadastrados)
