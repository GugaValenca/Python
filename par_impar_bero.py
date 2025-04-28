import random

print("💥 Bem-vindo ao Jogo do Par ou Ímpar do Beró! 💥")

while True:
    escolha = input("Tu quer ser 'par' ou 'ímpar'? ").strip().lower()
    if escolha not in ['par', 'ímpar', 'impar']:
        print("Ôxe, escolha direito: par ou ímpar, visse?")
        continue

    numero_usuario = int(input("Escolha um número de 0 a 10: "))
    numero_beró = random.randint(0, 10)
    
    print(f"Beró jogou {numero_beró} 🎲")
    
    soma = numero_usuario + numero_beró
    resultado = 'par' if soma % 2 == 0 else 'ímpar'

    print(f"A soma deu {soma}, que é {resultado}!")

    if (resultado == escolha) or (resultado == 'ímpar' and escolha == 'impar'):
        print("✅ Tu ganhou, cabra bom!")
    else:
        print("❌ Beró ganhou dessa vez! Vixe!")

    jogar_novamente = input("Quer jogar de novo? (s/n) ").strip().lower()
    if jogar_novamente != 's':
        print("Valeu, cabra! Até a próxima!")
        break
