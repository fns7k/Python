# DESAFIO 23

# Faça um programa que leia um numero de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.

numero = int(input("Digite um número de 0 a 9999: "))  # Solicita um número ao usuário

unidade = numero % 10  # Obtém a unidade do número
dezena = (numero // 10) % 10  # Obtém a dezena do número
centena = (numero // 100) % 10  # Obtém a centena do número
milhar = (numero // 1000) % 10  # Obtém o milhar do número

print(f"Unidade: {unidade}")  # Imprime a unidade
print(f"Dezena: {dezena}")  # Imprime a dezena
print(f"Centena: {centena}")  # Imprime a centena
print(f"Milhar: {milhar}")  # Imprime o milhar
