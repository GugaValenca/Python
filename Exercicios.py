def ler_numero_valido(prompt):
    while True:
        num = int(input(prompt))
        if num > 0:
            return num
        else:
            print("Número inválido. Por favor, digite um número maior que zero.")

num1 = ler_numero_valido("Digite um número: ")
num2 = ler_numero_valido("Digite outro número: ")
num3 = ler_numero_valido("Digite mais um número: ")

result = num1

if num2 > result:
    result = num2
if num3 > result:
    result = num3

print(f"O maior número é: {result}")