#pedir para o usuario digitar dois numeros 
#exibir o maior e o menor

print(40*'-')       #Imprimir 40 "-"
n1= int(input('Digite o primeiro número: '))        #Solicitar o primeiro número para o usuário
n2= int(input('Digite o segundo número: '))        #Solicitar o segundo número para o usuário

#verificando o maior e o menor número:
if n1>n2:       #Se o número2 for maior que o número1:
    print(40*'-')       #Imprimir 40 "-"
    print(f'O número "{n1}" é maior que o número "{n2}"')       #Mostrar no terminal
elif n2>n1:       #Se o número2 for maior que o número1:
    print(40*'-')       #Imprimir 40 "-"
    print(f'O número "{n2}" é maior que o número "{n1}"')       #Mostrar no terminal
else:       #Se nenhum dos dois acima acontecer:
    print(40*'-')       #Imprimir 40 "-"
    print(f'O número "{n1}" é igual ao número "{n2}"')       #Mostrar no terminal