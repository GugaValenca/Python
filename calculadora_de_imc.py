peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Sobrepeso.")
else:
    print("Obesidade.")