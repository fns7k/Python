#Criar um programa para entrar com base e altura de um retângulo e imprimir respectivamente o perímetro e a área correspondente

base= int(input('Digite o valor da base do retângulo: '))     #Solicitar o valor da base do retângulo
altura= int(input('Digite o valor da altura do retângulo: '))     #Solicitar o valor do retângulo do retângulo
perimetro= (base*2 + altura*2)      #Calcular o perímetro do retângulo
area= (base*altura)     #Calcular a área do retângulo
print(f'O valor do perímetro é {perimetro} e o valor da área é {area}')     #Mostrar o resultado no terminal


#ou

base= int(input('Digite o valor da base do retângulo: '))       #Solicitar o valor da base do retângulo
altura= int(input('Digite o valor da altura do retângulo: '))       #Solicitar o valor do retângulo do retângulo
print(f'O perímetro do retângulo é {base*2+altura*2} e a área do perímetro é {base*altura}')        #Mostrar o resultado no terminal