def eh_espelhada(palavra):
    letras_validas = set('AHIMOTUVWXY')
    for letra in palavra:
        if letra.upper() not in letras_validas:
            return False
    return palavra.upper() == palavra.upper()[::-1]

# Teste
entrada = input("Digite uma palavra: ")
if eh_espelhada(entrada):
    print("Essa palavra é espelhada! 👏")
else:
    print("Oxente! Essa aí não se espelha nem com reza braba!")
