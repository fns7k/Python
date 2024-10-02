#Crie um programa em Python que peça a temperatura em graus Celsius e o programa deve exibir em Fahrenheit.

print(40*'-')       #Imprimir 40 "-"
c= int(input('Digite os graus em Celsius: '))       #Solicitar a temperatura Celsius
f= (c*1.8)+32       #Fazer o cálculo e tonar os graus Celsius em Fahrenheit
print(40*'-')       #Imprimir 40 "-"
print(f'A temperatura em Celsius citada é {c}, em Fahrenheit é {f}.')       #Mostrar o resultado no Terminal
