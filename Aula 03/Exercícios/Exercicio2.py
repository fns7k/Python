# Crie um programa em Python que peça para o usuário digitar a idade de uma pessoa. 
# Faça com que o programa verifique e exiba se a pessoa é de maior idade ou não.

print(40*'-')
nome= str(input('Digite seu nome: '))       #Solicitar o nome para o usuário
idade= int(input('Digite sua idade: '))     #Solicitar a idade para o usuário

print(40*'-')
if idade>= 18:      #Se a idade for maior que 18 anos:
    print (f'O usuário "{nome}" é maior de idade')      #Mostrar no terminal
else:       #Se não:
    print(f'O usuário "{nome}" é menor de idade')       #Mostrar no terminal
