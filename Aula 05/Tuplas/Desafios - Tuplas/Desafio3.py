# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 



import random

# Gerar cinco números aleatórios
numeros_aleatorios = tuple(random.sample(range(1, 101), 5))
print("Cinco números aleatórios em uma tupla:", numeros_aleatorios)