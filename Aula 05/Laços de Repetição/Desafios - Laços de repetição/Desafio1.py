# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.



import time     #Importa o módulo time para utilizar a função sleep

for i in range(10, -1, -1):     #Loop de 10 até 0 (inclusive), decrementando de 1 em 1
    print(i)        #Imprime o valor atual de i (número da contagem)
    time.sleep(1)       #Pausa a execução por 1 segundo

print("Estouro de fogos!")  # Imprime a mensagem após a contagem regressiva
