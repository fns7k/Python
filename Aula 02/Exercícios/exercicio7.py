#Crie um programa que peça para o usuário digitar o nome do aluno e duas de suas notas
#O programa deve exibir o nome do aluno e sua média de nota


nome= str(input('Digite o seu nome: '))       #Solicitar o nome do usuário
nota1= int(input('Digite a sua primeira nota: '))       #Solicitar a primeira nota do usuário
nota2= int(input('Digite a sua segunda nota: '))       #Solicitar a segunda nota do usuário
print(40*'-')
print(f'A média das notas do aluno {nome} é {(nota1+nota2)/2}')        #Mostrar o resultado no terminal