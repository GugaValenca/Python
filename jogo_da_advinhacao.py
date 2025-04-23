import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Adivinha o número entre 1 e 100!")

while True:
    chute = int(input("Teu chute: "))
    tentativas += 1

    if chute < numero_secreto:
        print("É mais!")
    elif chute > numero_secreto:
        print("É menos!")
    else:
        print(f"Acertasse, cabra esperto! O número era {numero_secreto}.")
        print(f"Tu precisou de {tentativas} tentativa(s).")
        break