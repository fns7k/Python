# DESAFIO 26

# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input("Digite uma frase: ")  # Solicita uma frase ao usuário

# Contagem de vezes que a letra 'A' aparece
ocorrencias_a = frase.lower().count('a')  # Conta as ocorrências de 'a' (ignorando maiúsculas/minúsculas)
print("Quantidade de 'A's na frase:", ocorrencias_a)  # Imprime a quantidade de 'a's na frase

# Posição da primeira ocorrência de 'A'
primeira_ocorrencia_a = frase.lower().find('a') + 1  # Encontra a posição da primeira ocorrência de 'a'
print("Posição da primeira ocorrência de 'A':", primeira_ocorrencia_a)  # Imprime a posição da primeira ocorrência de 'a'

# Posição da última ocorrência de 'A'
ultima_ocorrencia_a = frase.lower().rfind('a') + 1  # Encontra a posição da última ocorrência de 'a'
print("Posição da última ocorrência de 'A':", ultima_ocorrencia_a)  # Imprime a posição da última ocorrência de 'a'
