# DESAFIO 25

# Crie um programa que leia o nome de uma pessoa e diga se ela tem
# "Silva" no nome

nome_pessoa = input("Digite o nome da pessoa: ")  # Solicita o nome da pessoa ao usuário

if "silva" in nome_pessoa.lower():  # Verifica se "silva" está presente no nome (ignorando maiúsculas/minúsculas)
    print("O nome contém 'Silva'.")  # Imprime se o nome contém "Silva"
else:
    print("O nome não contém 'Silva'.")  # Imprime se o nome não contém "Silva"
