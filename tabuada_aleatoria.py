import random

numero = random.randint(1, 10)
acertos = 0

print(f"Bora jogar a tabuada do {numero}! Responde aí, cabra da peste!\n")

for i in range(1, 11):
    resposta = int(input(f"{numero} x {i} = "))
    if resposta == numero * i:
        print("Acertou, bichim danado!")
        acertos += 1
    else:
        print(f"Errou, visse? O certo era {numero * i}")

print(f"\nFim de jogo! Tu acertou {acertos} de 10. Arretado demais!")
