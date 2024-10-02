import revisaoFuncoes  # Importa o módulo 'revisaoFuncoes' que contém funções definidas para cálculo.

# Solicita ao usuário um número para calcular sua raiz quadrada.
numero = int(input('Digite um número para saber sua raiz quadrada: '))

# Chama a função 'raizQuadrada' do módulo 'revisaoFuncoes' para calcular a raiz quadrada.
calculoRaiz = revisaoFuncoes.raizQuadrada(numero)

# Exibe o resultado da raiz quadrada.
print(f'A raiz do número {numero} é {calculoRaiz}')

print(40*'-')  # Imprime uma linha separadora.

# Solicita ao usuário duas notas para calcular a média.
primeiraNota = int(input('\nDigite a 1ª nota do aluno: '))
segundaNota = int(input('Digite a 2ª nota do aluno:'))

# Chama a função 'mediaNotas' do módulo 'revisaoFuncoes' para calcular a média das notas.
mediaNota = revisaoFuncoes.mediaNotas(primeiraNota, segundaNota)

print(40*'-')  # Imprime outra linha separadora.

# Exibe o resultado da média das notas.
print(f'A média de nota do aluno é: {mediaNota}')
