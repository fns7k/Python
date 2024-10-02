# Exercício 2
# Faça um programa em Python que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem como o exemplo abaixo.



def escreva(texto):  # Define a função 'escreva' que recebe o parâmetro 'texto'.
    tamanho = len(texto) + 4  # Calcula o tamanho da linha, que é o comprimento do texto mais 4 para adicionar margens.
    print("~" * tamanho)  # Imprime uma linha de '~' com o comprimento calculado.
    print(f"  {texto}")  # Imprime o texto centralizado, com 2 espaços antes.
    print("~" * tamanho)  # Imprime outra linha de '~' com o mesmo comprimento.

texto = input("Digite um texto: ")  # Solicita ao usuário que insira um texto.

escreva(texto)  # Chama a função 'escreva' com o texto fornecido pelo usuário.
