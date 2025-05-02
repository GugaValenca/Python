def cadastro_pessoas():
    pessoas = []

    for i in range(5):
        nome = input(f"Digite o nome da pessoa {i+1}: ")
        idade = int(input(f"Digite a idade de {nome}: "))
        pessoas.append({'nome': nome, 'idade': idade})

    mais_velho = max(pessoas, key=lambda p: p['idade'])
    mais_novo = min(pessoas, key=lambda p: p['idade'])

    print(f"O mais velho é {mais_velho['nome']} com {mais_velho['idade']} anos.")
    print(f"O mais novo é {mais_novo['nome']} com {mais_novo['idade']} anos.")

cadastro_pessoas()
