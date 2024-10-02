# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até dez.
# Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostra-lo por extenso.



# Tupla com números por extenso de 0 a 10
numerosPorExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')


# Solicita ao usuário que digite um número entre 0 e 10
numero = int(input("Digite um número entre 0 e 10: "))


if 0 <= numero <= 10:       #Verifica se o número está entre 0 e 10 (inclusive)
    print(f'O número {numero} por extenso é: {numerosPorExtenso[numero]}')      #Imprime o número por extenso usando a tupla
else:
    print("Número fora do intervalo permitido.")        #Se o número estiver fora do intervalo, imprime uma mensagem adequada










# Resolução do professor:
numeros=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

num=int(input('Digite um numero de 0 a 10'))

if num > 10:
    print('Numero inválido')
else:
    print(f'O numero digitado foi {numeros[num]}')