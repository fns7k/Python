# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram o números pares.




valores = tuple(int(input("Digite um valor: ")) for _ in range(4))
# A) Quantas vezes apareceu o valor 9
quantidadeNove = valores.count(9)
print("A) O valor 9 apareceu", quantidadeNove, "vezes.")
# B) Em que posição foi digitado o primeiro valor 3
posicaoTres = valores.index(3) + 1 if 3 in valores else "O valor 3 não foi digitado."
print("B) O primeiro valor 3 foi digitado na posição:", posicaoTres)
# C) Quais foram os números pares
numerosPares = [num for num in valores if num % 2 == 0]
print("C) Números pares digitados:", numerosPares)