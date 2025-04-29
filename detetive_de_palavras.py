def analisar_texto(texto):
    # Remove pontuações e padroniza
    import string
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palavras = texto_limpo.split()

    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    mais_repetida = max(contagem, key=contagem.get)
    print(f"Palavra mais repetida: '{mais_repetida}' ({contagem[mais_repetida]} vezes)")
    print(f"Total de palavras únicas: {len(contagem)}")

texto = input("Digite um texto para investigação: ")
analisar_texto(texto)
