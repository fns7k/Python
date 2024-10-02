# Criar um programa que leia um número inteiro e imprimir seu sucessor e antecessor

usuario= int(input('Digite o número inteiro: '))     #Solicitar o valor base para o usuário
sucessor= usuario + str(1)     #Calcular o sucessor do usuário
antecessor= usuario - str(1)      #Calcular o antecessor do usuário
print(f'O sucessor do número {usuario} é {sucessor}, e o antecessor é {antecessor}')      #Mostrar o resultado no terminal