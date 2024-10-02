n1= 5       #Declarar variavel do numero1 
n2= 3       #Declarar variavel do numero2

#Operador de Potência
potencia= n1 ** n2        # '**' Equivale ao 'elevado'
print(potencia)

#Operador Módulo
modulo= n1%n2       #Usado para ver o resto da divisão
print(modulo)

#Operador de Divisão Inteira
divisaoInteira= n1//n2     #Usado para ver a divisão inteira
print(divisaoInteira)


#Operador de Divisão Inteira
print('DIVISAO INTEIRA')      #Mostrar que é a Divisão Inteira no terminal
usuario= int(input('Digite o valor: '))     #Solicitar o valor base para o usuário
divisor= int(input('Digite um divisor: '))     #Solicitar o valor divisor para o usuário
divisao= usuario // divisor      #Função para dividir os valores que o usuário escolheu
print(usuario , '//' , divisor , '=' , divisao)      #Mostrar o resultado no terminal

#Operador de Potencia
print('POTENCIA')      #Mostrar que é a Potencia no terminal
usuario= int(input('Digite o valor: '))     #Solicitar o valor base para o usuário
multiplicador= int(input('Digite o valor da potencia: '))     #Solicitar o valor da potencia para o usuário
multiplicacao= usuario ** multiplicador      #Função para multiplicar os valores que o usuário escolheu
print(f'{usuario}^{multiplicador} = {multiplicacao}')      #Mostrar o resultado no terminal

#Operador de Modulo
print('MODULO')      #Mostrar que é a Modulo no terminal
usuario= int(input('Digite o valor: '))     #Solicitar o valor base para o usuário
sub= int(input('Digite um numero para subtrair: '))     #Solicitar o valor de Modulo para o usuário
subtracao= usuario % sub      #Função para dividir os valores que o usuário escolheu
print(usuario , '%' , sub , '=' , subtracao)      #Mostrar o resultado no terminal
