# DESAFIO 02
# Crie um programa em Python onde 4 jogadores joguem um dado e tenham resultado aleatórios. Guarde esses resultados em um dicionário. 
# No final, exiba o nome e o numero daquele que tirou o maior numero (vencedor).



import random

# Definindo os nomes dos jogadores
jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4']


# Dicionário para armazenar os resultados dos jogadores
resultados = {}


# Simulando o lançamento do dado para cada jogador e armazenando os resultados
for player in jogadores:
    resultadoDado = random.randint(1, 6)  # Lança um dado de 6 faces
    resultados[player] = resultadoDado


# Encontrando o jogador com o maior número
vencedor = max(resultados, key=resultados.get)      # Forma achada na internet usando a função MAX do Python para achar o jogador com o maior número 


# Exibindo os resultados
print("Resultados dos jogadores:")

for jogador, resultado in resultados.items():
    print(f"{jogador}: {resultado}")

print(f"\nO vencedor é: {vencedor} com o número {resultados[vencedor]}.")
