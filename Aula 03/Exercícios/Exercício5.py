#Crie um programa em Python que simule um semáforo de trânsito. 
#O programa deve pedir para o usuário informar a cor do semáforo
#Logo após o programa deve exibir a mensagem correspondente a cor digitada.

cor= input('Informe a cor do Semáforo: ')       #Solicitar a cor para o usuário
print(40*'-')       #Imprimir 40 "-"


#converter texto para minúsculo:
cor=cor.lower()

#converter texto para maiúsculo:
cor=cor.upper()

#deixar apenas a primeira letra em maiúsculo:
cor=cor.capitalize()


if cor== 'verde':       #Se a cor do semáforo for verde:
    print('O carro pode avançar')       #Mostrar no terminal

if cor== 'vermelho':        #Se a cor do semáforo for vermelho:
    print('O carro deve ficar parado aguardando o sinal verde')       #Mostrar no terminal

if cor== 'amarelo':         #Se a cor do semáforo for amarelo:
    print('O carro deve parar e aguardar o sinal verde')        #Mostrar no terminal

else:       #Caso não seja nenhuma das 3 cores do semáforo:
    print('Usuário não digitou uma cor de semáforo')        #Mostrar no terminal