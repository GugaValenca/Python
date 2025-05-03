import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 20)
    tentativas = 0

    print('Oxente! Tente adivinhar o número entre 1 e 20!')

    while True:
        chute = int(input('Digite seu palpite: '))
        tentativas += 1

        if chute < numero_secreto:
            print('Eita, foi baixo demais! Tente de novo.')
        elif chute > numero_secreto:
            print('Vish, passou da conta! Tente novamente.')
        else:
            print(f'Arretado! Acertou em {tentativas} tentativa(s). O número era {numero_secreto}.')
            break

# Chamada do jogo
jogo_adivinhacao()
