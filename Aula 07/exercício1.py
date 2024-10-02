# Escreva um programa que solicite vários números ao usuário, sendo um de cada vez, possibilitando encerrar a entrada de dados informando zero. 
# Adicione os números informados em uma lista
# Ao final do programa, imprima a soma de todos os números, a multiplicação de todos os números, o maior e o menor número informado.


# Exemplo de execução:
# Informe um número (zero para sair): 10
# Informe um número (zero para sair): 5
# Informe um número (zero para sair): 20
# Informe um número (zero para sair): 0



# Solicitação dos números ao usuário
numeros = []        # Cria uma lista vazia para armazenar os números fornecidos pelo usuário
while True:         # Loop para continuar solicitando números até que o usuário informe zero para sair // utilizado quando quer repetir um bloco de código enquanto uma expressão for verdadeira.
    numero = float(input("Informe um número (zero para sair): "))       # Solicita um número ao usuário
    if numero == 0:     # Verifica se o número informado é zero
        break       # Encerra o loop
    numeros.append(numero)      # Adiciona o número à lista de números // O append é para quando você quer adicionar um único item em uma lista.



# Calcular soma
def Soma(lista):        # Define uma função para calcular a soma de uma lista de números // Definir Soma
    return sum(lista)       # Retorna a soma de todos os elementos da lista fornecida // Operação de Soma para lista



# Função para calcular a multiplicação de uma lista
def Multiplicacao(lista):       # Define uma função para calcular a multiplicação de uma lista de números
    resultado = 1       # Inicializa o resultado como 1, pois a multiplicação por 1 não altera o valor
    for num in lista:       # Percorre cada número na lista
        resultado *= num        # Multiplica o resultado pelo número atual // Equivalente a fazer x = x * valor
    return resultado        # Retorna o resultado da multiplicação



# Verifica se a lista não está vazia
if numeros:
    # Calcula a soma, multiplicação, maior e menor número
    soma = Soma(numeros)        # Calcula a soma dos números na lista
    multiplicacao = Multiplicacao(numeros)          # Calcula a multiplicação dos números na lista
    maior = max(numeros)        # Encontra o maior número na lista
    menor = min(numeros)        # Encontra o menor número na lista


    # Imprime os resultados
    print(40*'-')       # Imprime uma linha de separação
    print(f"Números informados: {numeros}")         # Imprime os números fornecidos pelo usuário
    print(20*'-')       # Imprime uma linha de separação
    print(f"Soma de todos os números: {soma}")          # Imprime a soma dos números
    print(f"Multiplicação de todos os números: {multiplicacao}")        # Imprime a multiplicação dos números
    print(f"Maior número informado: {maior}")        # Imprime o maior número
    print(f"Menor número informado: {menor}")        # Imprime o menor número
else:  # Se a lista estiver vazia
    print("Nenhum número foi informado.")         # Informa que nenhum número foi fornecido pelo usuário








# Exemplo do professor :
lista = []

while True:
    num= int(input('Digite um numero'))
    lista.append(num)
    
    opcao= int(input('Deseja encerrar o programa? digite 0 para sair'))
    if opcao == 0:
        break

print(lista)