#Crie um programa em Python que peça para o usuário digitar dois números
#Logo após, o programa deve exibir qual o maior e qual o menor número digitado.

n1= int(input('Digite o primeiro número: '))        #Solicitar o primeiro número para o usuário
n2= int(input('Digite o segundo número: '))         #Solicitar o segundo número para o usuário

if n1>n2:       #Se o número1 for maior que o número2:
    print(f'O número "{n1}" é maior que o número "{n2}"')       #Mostrar no terminal
else:       #Se o número2 for maior que o número1:
    print(f'O número "{n2}" é maior que o número "{n1}"')       #Mostrar no terminal

if n1==n2:      #Se o número1 for igual ao número2:
    print(f'O número "{n1}" é igual ao número "{n2}"')      #Mostrar no terminal