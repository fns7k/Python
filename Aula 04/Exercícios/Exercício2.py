#Faca um programa em Python que peça para o usuário um númerop entre 1 e 10, logo após, o porgrama deve calcular a tábuada do número digitado.


tab= int(input('Digite um número de 1 até 10 para ver a tabuada: '))

for auxiliar in range(1,11):
    print(f'{auxiliar} X {tab} = {auxiliar * tab}')