#Criar um programa que peça para o usuário digitar um número de 1 a 10
#O programa deve exibir a tabuada do número digitado

linha= print(40*'-')        #Fazer uma linha com 40 -
numero= int(input('Digite um número de 1 até 10 para ver a tabuada: '))       #Solicitar o número do usuário
if not 1<= numero <=10:(        #Caso o número não seja entre 1 e 10, tentar novamente
    print('O número deverá ser de 1 a 10, tente novamente')     #Imprimir o texto "O número deverá ser de 1 a 10, tente novamente"
)
if 1<= numero <=10:(        #Caso o número seja entre 1 e 10, segue tabuada
    print(f'Segue tabela do número: {numero}\n {numero}*1= {numero*1}\n {numero}*2= {numero*2}\n {numero}*3= {numero*3}\n {numero}*4= {numero*4}\n {numero}*5= {numero*5}\n {numero}*6= {numero*6}\n {numero}*7= {numero*7}\n {numero}*8= {numero*8}\n {numero}*9= {numero*9}\n {numero}*10= {numero*10}')      #Imprimir tabuada do número escolhido para o usuário
)