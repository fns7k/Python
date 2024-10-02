# Exercício 4
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). 
# A primeira função vai sortear 5 números de 1 a 10 e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.



import random  # Importa o módulo 'random' que contém funções para geração de números aleatórios.

def sorteio():  # Define a função 'sorteio' que não recebe parâmetros.
    numeros = []  # Cria uma lista vazia chamada 'numeros' para armazenar os números sorteados.
    for _ in range(5):  # Executa um loop 5 vezes (para sortear 5 números).
        numeros.append(random.randint(1, 10))  # Gera um número aleatório entre 1 e 10 e o adiciona à lista 'numeros'.
    return numeros  # Retorna a lista de números sorteados.

def somaPar(lista):  # Define a função 'somaPar' que recebe uma lista como parâmetro.
    soma = 0  # Inicializa uma variável 'soma' com valor 0 para acumular a soma dos números pares.
    for num in lista:  # Itera sobre cada número na lista fornecida.
        if num % 2 == 0:  # Verifica se o número é par (divisível por 2).
            soma += num  # Se for par, adiciona o número à variável 'soma'.
    return soma  # Retorna a soma total dos números pares.

# Sorteando os números
numerosSorteados = sorteio()  # Chama a função 'sorteio' e armazena os números sorteados na variável 'numerosSorteados'.

# Calculando a soma dos números pares
soma_pares = somaPar(numerosSorteados)  # Chama a função 'somaPar' com a lista de números sorteados e armazena a soma dos pares na variável 'soma_pares'.

print("Números sorteados:", numerosSorteados)  # Exibe a lista de números sorteados.
print("Soma dos números pares:", soma_pares)  # Exibe a soma dos números pares.

