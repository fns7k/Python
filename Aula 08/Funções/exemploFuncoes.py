import exemploFuncoesExternas

def somarDoisNumeros():
    num1 = 34
    num2 = 66

    soma = num1 + num2
    print(f'soma = {soma}')


def subtrairDoisNumeros(n1,n2):
    subtrair= n1 - n2
    print(f'subtracao = {subtrair}')


# Criar mais duas funções:
# Uma funçao para multiplicar os dois números digitados
# Outra função para fazer a divisão dos números digitados 


def multiplicarDoisNumeros(n1,n2):
    multiplicar= n1 * n2
    print(f'multiplicaçao = {multiplicar}')
    

def dividirDoisNumeros(n1,n2):
    dividir= n1 / n2
    print(f'divisao = {dividir}')



numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))


print(f'\n')
somarDoisNumeros()

print(40*'-')
subtrairDoisNumeros(numero1,numero2)

print(40*'-')
multiplicarDoisNumeros(numero1,numero2)

print(40*'-')
dividirDoisNumeros(numero1,numero2)





print(40*'-')
exemploFuncoesExternas.calcularRaiz(numero1)




# Criar uma função externa que calcule o valor do numero2 ao quadrado
print(40*'-')
exemploFuncoesExternas.calcularPotencia(numero2)
