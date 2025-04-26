def analisar_texto(texto):
    palavras = texto.split()
    frases = texto.count('.') + texto.count('!') + texto.count('?')

    # Tirar pontuações das palavras
    palavras_limpa = [palavra.strip('.,!?').lower() for palavra in palavras]
    
    # Contar ocorrências
    contagem = {}
    for palavra in palavras_limpa:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    palavra_mais_comum = max(contagem, key=contagem.get)

    return len(palavras), frases, palavra_mais_comum

# Teste
texto_exemplo = "Beró é massa. Gustavo é arretado! Beró gosta de cuscuz. Cuscuz é bom."
print(analisar_texto(texto_exemplo))