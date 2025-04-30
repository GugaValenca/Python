import random

def jogo():
    escolha = input("Par ou Ímpar? ").strip().lower()
    jogador = int(input("Escolha um número (0 a 10): "))
    pc = random.randint(0, 10)
    total = jogador + pc

    print(f"Você jogou {jogador}, eu joguei {pc}. Total deu {total}.")

    if (total % 2 == 0 and escolha == "par") or (total % 2 != 0 and escolha == "ímpar"):
        print("Acertô, miserávi! Você ganhou!")
    else:
        print("Eita lasqueira, perdeu dessa vez...")

jogo()
