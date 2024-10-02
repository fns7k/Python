# DESAFIO 24

# Crie um programa que leia o nome de uma cidade e siga se ela começa
# ou não com o nome "Santo".

nome_cidade = input("Digite o nome da cidade: ")  # Solicita o nome da cidade ao usuário

if nome_cidade[:5].lower() == "santo":  # Verifica se os primeiros cinco caracteres, em minúsculas, são "santo"
    print("A cidade começa com 'Santo'.")  # Imprime se a cidade começa com "Santo"
else:
    print("A cidade não começa com 'Santo'.")  # Imprime se a cidade não começa com "Santo"
