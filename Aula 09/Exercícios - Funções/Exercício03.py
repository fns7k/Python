# Exercício 3
# Faça um programa que tenha uma função chamada maior(), que receba três parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.



def maior(a, b, c):  # Define a função 'maior' que recebe três parâmetros (a, b, c).
    # Verifica se a é maior que b e c
    if a > b and a > c:
        return a
    # Verifica se b é maior que a e c
    elif b > a and b > c:
        return b
    # Caso nenhum dos casos acima seja verdadeiro, então c é o maior
    else:
        return c

# Exemplo de uso da função
num1 = int(input("Digite o primeiro número: "))  # Converte o valor de entrada para inteiro.
num2 = int(input("Digite o segundo número: "))   # Converte o valor de entrada para inteiro.
num3 = int(input("Digite o terceiro número: "))  # Converte o valor de entrada para inteiro.

print(f"O maior número dentre os números {num1}, {num2} e {num3} é:", maior(num1, num2, num3))  # Chama a função 'maior' e imprime o resultado.
