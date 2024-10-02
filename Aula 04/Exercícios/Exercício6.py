#Desenvolva um programa que leia seis números inteiros e
#mostre a soma dos desses números.

soma = 0
for num in range(6):
    numeroUsuario = int(input(f'Digite o {num + 1}º número '))
    soma = soma + numeroUsuario

print(f'A soma dos números digitados é {soma}')