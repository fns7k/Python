# Desenvolva um programa que leia o idade e sexo de 10 pessoas. 
# No final do programa deve mostrar:
# A média de idade dos homens --> media = somaIdadeHomens / qntHoemns
# A média de idade das mulheres
# A média de idade do grupo

quantidadeHomens = 0
somaIdadeHomens = 0 
quantidadeMulheres = 0 
somaIdadeMulheres = 0

for quantidade in range(10):
    idade= int(input(f'Digite a idade da {quantidade+1}º pessoa: '))
    sexo= input(f'Digite o sexo da {quantidade+1}º pessoa: F / M')
    
    if sexo== 'F': 
        quantidadeMulheres = quantidadeMulheres + 1 
        somaIdadeMulheres = somaIdadeMulheres + idade
    elif sexo== 'M':
        quantidadeHomens = quantidadeHomens + 1
        somaIdadeHomens = somaIdadeHomens + idade
    else:
        print('Sexo da pessoa digitado incorretamente!')
        qnt= qnt-1
        

mediaIdadeHomens = somaIdadeHomens / quantidadeHomens
mediaIdadeMulheres = somaIdadeMulheres / quantidadeMulheres
mediaIdadeGrupo = (mediaIdadeHomens + mediaIdadeMulheres)/2

print(f'A média de idade de homens é {mediaIdadeHomens}')
print(f'A média de idade de homens é {mediaIdadeMulheres}')
print(f'A média de idade de homens é {mediaIdadeGrupo}')
