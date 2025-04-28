import random
import string

print("🔐 Gerador de Senhas Nordestinas 🔐")

quant_letras = int(input("Quantas letras tu quer na senha? "))
quant_numeros = int(input("Quantos números tu quer? "))
quant_simbolos = int(input("Quantos símbolos tu quer? "))

# Escolhendo aleatoriamente
letras = random.choices(string.ascii_letters, k=quant_letras)
numeros = random.choices(string.digits, k=quant_numeros)
simbolos = random.choices(string.punctuation, k=quant_simbolos)

# Misturando tudim
senha_lista = letras + numeros + simbolos
random.shuffle(senha_lista)

# Transformando em uma string só
senha_final = ''.join(senha_lista)

print(f"Sua senha arretada é: {senha_final}")
