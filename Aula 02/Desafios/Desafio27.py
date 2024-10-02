# DESAFIO 27

# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente

nome_completo = input("Digite o nome completo: ")  # Solicita o nome completo ao usuário

# Separando o primeiro e o último nome
primeiro_nome = nome_completo.split()[0]  # Obtém o primeiro nome
ultimo_nome = nome_completo.split()[-1]  # Obtém o último nome

print("Primeiro nome:", primeiro_nome)  # Imprime o primeiro nome
print("Último nome:", ultimo_nome)  # Imprime o último nome
