# Crie um programa que leia o idade de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.



menoridade = 0      #Inicializa a variável 'menoridade' com o valor 0
maioridade = 0      #Inicializa a variável 'maioridade' com o valor 0

for _ in range(7):      #Loop que itera 7 vezes
    idade = int(input("Digite a idade: "))      #Solicita ao usuário que digite a idade
    if idade < 18:      #Verifica se a idade é menor que 18
        menoridade += 1     #Incrementa a contagem de menoridade
    else:
        maioridade += 1     #Incrementa a contagem de maioridade se a idade não for menor que 18

print(40*'-')       #Imprime uma linha tracejada para separar
print(f"Pessoas menores de idade: {menoridade}")        #Imprime o número de pessoas menores de idade
print(f"Pessoas maiores de idade: {maioridade}")        #Imprime o número de pessoas maiores de idade
