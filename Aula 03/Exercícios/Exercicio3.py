#Crie um programa em Python que peça para o usuário três notas de um aluno
#Logo após, o programa deve exibir a média do aluno e informar se o mesmo está reprovado ou aprovado. 
#Para ser aprovado, a média deve ser maior que 5.

print(40*'-')       #Imprimir 40 "-"
n1= int(input('Digite a primeira nota: '))      #Solicitar a primeira nota para o usuário
n2= int(input('Digite a segunda nota: '))       #Solicitar a segunda nota para o usuário
n3= int(input('Digite a terceira nota: '))      #Solicitar a terceira nota para o usuário

print(40*'-')       #Imprimir 40 "-"

if ((n1+n2+n3)/3)>5:        #Se a média das 3 notas for maior que 5:
    print(f'O aluno foi aprovado com a média equivalente a "{(n1+n2+n3)/3}" ')      #Mostrar no terminal
else:       #Se a média for menor que 5:
    print(f'O aluno foi reprovado com a média equivalente a "{(n1+n2+n3)/3}" ')     #Mostrar no terminal
