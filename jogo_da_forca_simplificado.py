def jogo_forca(palavra):
    letras_certas = set()
    tentativas = 6
    palavra = palavra.lower()

    while tentativas > 0:
        exibida = [letra if letra in letras_certas else '_' for letra in palavra]
        print(' '.join(exibida))

        if '_' not in exibida:
            print("Parabéns, cabra esperto! Acertou a palavra!")
            return
        
        palpite = input("Digite uma letra: ").lower()
        
        if palpite in palavra:
            letras_certas.add(palpite)
        else:
            tentativas -= 1
            print(f"Errou, visse? Restam {tentativas} tentativas.")

    print(f"Perdeu! A palavra era: {palavra}")

# Teste
# jogo_forca("macaxeira")