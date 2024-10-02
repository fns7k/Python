# Escreva um programa em Python que solicite vários números ao usuário, sendo um de cada vez, possibilitando encerrar a entrada de dados informando zero.
# Adicione os números em uma lista, crie uma outra lista contendo os números sem repetição e outra contendo os números que se repetem na primeira lista.
# Exemplo de execução:
#     Informe um número (zero para sair): 10
#     Informe um número (zero para sair): 5
#     Informe um número (zero para sair): 4
#     Informe um número (zero para sair): 10
#     Informe um número (zero para sair): 88
#     Informe um número (zero para sair): 4
#     Informe um número (zero para sair): 10
#     Informe um número (zero para sair): 4
#     Informe um número (zero para sair): 8
#     Informe um número (zero para sair): 0
    
#     Números informados: [10,5,4,10,88,4,10,4,8]
#     Números de repetição: [10,5,4,88,8]
#     Somente números que se repetiram: [10,4]



# Solicitação dos números ao usuário
numeros = []        # Cria uma lista vazia para armazenar os números fornecidos pelo usuário
while True:         # Loop para continuar solicitando números até que o usuário informe zero para sair // utilizado quando quer repetir um bloco de código enquanto uma expressão for verdadeira.
    numero = float(input("Informe um número (zero para sair): "))       # Solicita um número ao usuário
    if numero == 0:     # Verifica se o número informado é zero
        break       # Encerra o loop
    numeros.append(numero)      # Adiciona o número à lista de números // O append é para quando você quer adicionar um único item em uma lista.