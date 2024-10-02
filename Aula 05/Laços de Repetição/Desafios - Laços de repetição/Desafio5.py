# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.



maior_peso = float('-inf')      #Inicializa a variável 'maior_peso' com o menor valor possível em ponto flutuante
menor_peso = float('inf')       #Inicializa a variável 'menor_peso' com o maior valor possível em ponto flutuante

for _ in range(5):      #Loop que itera 5 vezes
    peso = float(input("Digite o peso em kg: "))        #Solicita ao usuário que digite o peso em kg
    if peso > maior_peso:       #Verifica se o peso é maior que o 'maior_peso' atual
        maior_peso = peso       #Atualiza o 'maior_peso' se a condição for verdadeira
    if peso < menor_peso:       #Verifica se o peso é menor que o 'menor_peso' atual
        menor_peso = peso       #Atualiza o 'menor_peso' se a condição for verdadeira

print(40*'-')       #Imprime uma linha tracejada para separar
print(f"O maior peso é: {maior_peso} kg")       #Imprime o maior peso
print(f"O menor peso é: {menor_peso} kg")       #Imprime o menor peso
