import re

def validar_email(email):
    # Expressão regular arretada pra validar e-mail
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if re.match(padrao, email):
        return True
    else:
        return False

# Testes
print(validar_email("guga@valenca.com"))          # True
print(validar_email("guga.valenca@"))             # False
print(validar_email("beró@sanfona.mel"))          # True
print(validar_email("semarroba.com"))             # False