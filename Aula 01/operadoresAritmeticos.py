numero1= 6      #Declarar variavel
numero2= 3      #Declarar variavel

#Operador de Soma
soma= numero1 + numero2     #Declarar Soma
#print(soma)     #Imprimir Soma
print(numero1 , '+' , numero2 , '=' , soma)     #Imprimir Soma

#Operador de Subtração
subtracao= numero1 - numero2        #Declarar Subtração
#print(subtracao)     #Imprimir Subtração
print(numero1 , '-' , numero2 , '=' , subtracao)     #Imprimir Subtração

#Operador de Multiplicação
multiplicacao= numero1 * numero2        #Declarar Multiplicação
#print(multiplicacao)     #Imprimir Multiplicação
print(numero1 , '*' , numero2 , '=' , multiplicacao)     #Imprimir Multiplicação

#Operador de Divisão
divisao= numero1 / numero2        #Declarar Divisão
#print(divisao)     #Imprimir Divisão
print(numero1 , '/' , numero2 , '=' , divisao)     #Imprimir Divisão



#A seguir será feito as operações utilizando valores que o usuário escolher no terminal:

#Operador de Divisão
print('DIVISAO')      #Mostrar que é a Divisão no terminal
usuario= int(input('Digite o valor: '))     #Solicitar o valor base para o usuário
divisor= int(input('Digite um divisor: '))     #Solicitar o valor divisor para o usuário
divisao= usuario / divisor      #Função para dividir os valores que o usuário escolheu
print(usuario , '/' , divisor , '=' , divisao)      #Mostrar o resultado no terminal

#Operador de Multiplicação
print('MULTIPLICACAO')      #Mostrar que é a Multiplicação no terminal
usuario= int(input('Digite o valor: '))     #Solicitar o valor base para o usuário
multiplicador= int(input('Digite um multiplicador: '))     #Solicitar o valor multiplicador para o usuário
multiplicacao= usuario * multiplicador      #Função para multiplicar os valores que o usuário escolheu
print(usuario , '*' , multiplicador , '=' , multiplicacao)      #Mostrar o resultado no terminal

#Operador de Subtração
print('SUBTRACAO')      #Mostrar que é a Subtração no terminal
usuario= int(input('Digite o valor: '))     #Solicitar o valor base para o usuário
sub= int(input('Digite um numero para subtrair: '))     #Solicitar o valor de subtração para o usuário
subtracao= usuario - sub      #Função para subtrair os valores que o usuário escolheu
print(usuario , '-' , sub , '=' , subtracao)      #Mostrar o resultado no terminal

#Operador de Soma
print('SOMA')      #Mostrar que é a Soma no terminal
usuario= int(input('Digite o valor: '))     #Solicitar o valor base para o usuário
somador= int(input('Digite um numero para somar: '))     #Solicitar o valor de adição para o usuário
soma= usuario + somador      #Função para somar os valores que o usuário escolheu
print(usuario , '+' , somador , '=' , soma)      #Mostrar o resultado no terminal
