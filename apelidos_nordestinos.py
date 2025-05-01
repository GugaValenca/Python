import random

def gerar_apelido(nome):
    apelidos = ['Cabra da Peste', 'Arretado', 'Oxe', 'Cangaceiro', 'Forrozeiro', 'Bicho Danado', 'Matuto', 'Lampião']
    return f"{nome} {random.choice(apelidos)}"

def main():
    print("😎 Gerador de Apelidos Nordestinos")
    nome = input("Digite seu nome: ")
    print(f"Seu apelido é: {gerar_apelido(nome)}")

if __name__ == "__main__":
    main()
