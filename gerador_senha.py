import string as st
import random

def gerador_senha(len_pass = 8):
    letras = st.ascii_letters
    numeros = st.digits
    especial = st.punctuation
    total = letras + numeros + especial

    password = ""

# Gera uma senha de comprimento len_pass
    for i in range(0, len_pass):
        digito = random.choice(total)
        password += digito

    return password

# Pede ao usuário o número de dígitos da senha
choice_user = input("Quantos digitos na senha? obs: mínimo 8:")

# Verifica se a entrada é um número positivo
if choice_user.isdigit():
    choice_user = int(choice_user)
    if choice_user < 8 or choice_user > 100:
        print("ERRO: A senha deve ter 8 a 100 dígitos")
        quit()
else:
    print("Entrada inválida")
    quit()

# Gera e imprime a senha
res = gerador_senha(choice_user)
print(res)

