# DESAFIO 22

# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome_completo = input("Digite o nome completo: ")  # Solicita o nome completo ao usuário

# Letras maiúsculas
print("Nome em maiúsculas:", nome_completo.upper())  # Imprime o nome em maiúsculas

# Letras minúsculas
print("Nome em minúsculas:", nome_completo.lower())  # Imprime o nome em minúsculas

# Total de letras (sem considerar espaços)
total_letras = len(nome_completo.replace(" ", ""))  # Calcula o total de letras excluindo espaços
print("Total de letras:", total_letras)  # Imprime o total de letras

# Letras no primeiro nome
primeiro_nome = nome_completo.split()[0]  # Obtém o primeiro nome
letras_primeiro_nome = len(primeiro_nome)  # Conta as letras no primeiro nome
print("Letras no primeiro nome:", letras_primeiro_nome)  # Imprime o número de letras no primeiro nome
