# Exercício 1
# Faça um programa em Python que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.



def area(largura, comprimento):  # Define a função 'area' que recebe dois parâmetros: 'largura' e 'comprimento'.
    areaTerreno = largura * comprimento  # Calcula a área do terreno multiplicando a largura pelo comprimento.
    return areaTerreno  # Retorna o valor da área calculada.

largura = float(input("Digite a largura do terreno: "))  # Solicita ao usuário que insira a largura do terreno e converte a entrada para um número decimal (float).
comprimento = float(input("Digite o comprimento do terreno: "))  # Solicita ao usuário que insira o comprimento do terreno e converte a entrada para float.

print("A área do terreno é:", area(largura, comprimento))  # Chama a função 'area' passando os valores de 'largura' e 'comprimento', e imprime o resultado com uma mensagem.
