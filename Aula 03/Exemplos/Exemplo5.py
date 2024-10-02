#Médias utilizando elif
#Pedir duas notas para o usuário
#Se média for maior que 6, aprovado
#Se média for menor de 4, reprovado
#Se média for entre 4 e 5, recuperação

print(40*'-')       #Imprimir 40 "-"
n1= float(input('Digite a primeira nota: '))        #Solicitar a primeira nota para o usuário
n2= float(input('Digite a segunda nota: '))        #Solicitar a segunda nota para o usuário
media= (n1+n2)/2        #Calcular a média das notas

if media>6:     #Se a média for maior que 6:
    print(40*'-')       #Imprimir 40 "-"
    print('Aprovado')       #Mostrar no terminal
elif media<4:     #Se a média for menor que 4:
    print(40*'-')       #Imprimir 40 "-"
    print('Reprovado')       #Mostrar no terminal
else:       #Se nenhum dos dois acima acontecer:
    print(40*'-')       #Imprimir 40 "-"
    print('Fazer recuperação')       #Mostrar no terminal