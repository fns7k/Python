#Faça um programa em Python que mostre para o usuário um número entre 1 e 10, logo após, o programa deve calcular e exibir a tabuada do número digitado. 
# O programa deve perguntar e permitir se o usuário quer ver  uma nova tábuada, se sim, fazer o processo novamente, caso contrário, encerra o programa.

print(40*'-')

while True:
    tab = int(input('Digite um número de 1 até 10 para ver a tabuada: '))
    
    for num in range(1,11):
        print(f"{tab} X {num} = {tab * num}")

    resposta = input('Você gostaria de Ver a tábuada de outro número? S ou N ')
    resposta = resposta.upper()
    
    if resposta == 'N':
        print('O programa foi encerrado ')
        break
    
print(40*'-')
    