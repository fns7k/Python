# Desenvolva um programa que leia o idade e sexo de 10 pessoas. 
# No final do programa deve mostrar:
# A média de idade dos homens --> media = somaIdadeHomens / qntHoemns
# A média de idade das mulheres
# A média de idade do grupo



quantidadeHomens = 0        #Inicializa a variável para contar a quantidade de homens
somaIdadeHomens = 0         #Inicializa a variável para somar a idade dos homens
quantidadeMulheres = 0      #Inicializa a variável para contar a quantidade de mulheres
somaIdadeMulheres = 0       #Inicializa a variável para somar a idade das mulheres


for quantidade in range(10):        #Loop que itera 10 vezes
    idade = int(input(f'Digite a idade da {quantidade + 1}º pessoa: '))     #Solicita a idade da pessoa
    sexo = input(f'Digite o sexo da {quantidade + 1}º pessoa: F / M')       #Solicita o sexo da pessoa

    if sexo == 'F':         #Verifica se o sexo é feminino
        quantidadeMulheres = quantidadeMulheres + 1         #Incrementa a quantidade de mulheres
        somaIdadeMulheres = somaIdadeMulheres + idade       #Adiciona a idade da mulher à soma
    elif sexo == 'M':       #Verifica se o sexo é masculino
        quantidadeHomens = quantidadeHomens + 1         #Incrementa a quantidade de homens
        somaIdadeHomens = somaIdadeHomens + idade       #Adiciona a idade do homem à soma
    else:
        print('Sexo da pessoa digitado incorretamente!')        #Exibe uma mensagem se o sexo for digitado incorretamente
        quantidade = quantidade - 1         #Decrementa a quantidade, pois o loop não deve contar essa entrada incorreta


mediaIdadeHomens = somaIdadeHomens / quantidadeHomens               #Calcula a média de idade para homens
mediaIdadeMulheres = somaIdadeMulheres / quantidadeMulheres         #Calcula a média de idade para mulheres
mediaIdadeGrupo = (mediaIdadeHomens + mediaIdadeMulheres) / 2       #Calcula a média de idade para o grupo total

print(f'A média de idade dos homens é {mediaIdadeHomens}')
print(f'A média de idade das mulheres é {mediaIdadeMulheres}')
print(f'A média de idade do grupo é {mediaIdadeGrupo}')
