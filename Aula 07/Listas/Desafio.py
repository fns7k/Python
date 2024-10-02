# Escreva um programa que solicite vários números ao usuário, sendo um de cada vez, possibilitando encerrar a entrada de dados informando zero.
# Armazene os números em uma lista, depois percorra esta lista alimentando outras duas listas, uma com números pares e outra com números ímpares. 
# Ordene e imprima os números em ordem crescente e some os valores e imprima o resultado.



# Inicializando as listas
numeros = []
pares = []
impares = []

# Solicitando os números ao usuário
while True:
    num = int(input("Digite um número (digite 0 para encerrar): "))
    if num == 0:
        break
    numeros.append(num)

# Separando os números pares e ímpares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Ordenando as listas
pares.sort()
impares.sort()

# Imprimindo os números em ordem crescente
print("Números pares em ordem crescente:", pares)
print("Números ímpares em ordem crescente:", impares)

# Somando os valores
soma = sum(numeros)
print("A soma dos valores é:", soma)
