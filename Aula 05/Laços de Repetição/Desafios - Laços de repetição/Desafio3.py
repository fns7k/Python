# Desenvolva um programa que leia seis números inteiros
# Mostre a soma dos desses números.


soma = 0        #Inicializa a variável 'soma' com o valor 0

for _ in range(6):      #Loop que itera 6 vezes
    numero = int(input("Digite um número inteiro: "))       #Solicita ao usuário que digite um número inteiro
    soma += numero      #Adiciona o número à variável 'soma'

print(40*'-')       #Imprime uma linha tracejada para separar
print(f"A soma dos números é: {soma}")      #Imprime a soma total dos números inseridos
