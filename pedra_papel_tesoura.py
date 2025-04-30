import random

historico = {"pedra": 0, "papel": 0, "tesoura": 0}
vencem = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}

def escolha_computador(historico):
    if sum(historico.values()) == 0:
        return random.choice(list(historico.keys()))
    mais_usado = max(historico, key=historico.get)
    # Joga o que ganha da tua jogada preferida
    for jogada, vence in vencem.items():
        if vence == mais_usado:
            return jogada

while True:
    jogador = input("Pedra, papel ou tesoura? (ou 'sair'): ").lower()
    if jogador == 'sair':
        break
    if jogador not in historico:
        print("Oxente, jogada errada, tente de novo!")
        continue

    historico[jogador] += 1
    computador = escolha_computador(historico)

    print(f"Tu jogou {jogador}, o computador jogou {computador}.")

    if jogador == computador:
        print("Empate, cabra esperto!")
    elif vencem[jogador] == computador:
        print("Tu ganhou, danado!")
    else:
        print("Perdeu, visse? O bicho tá aprendendo contigo...")

