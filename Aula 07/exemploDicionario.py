# Tupla ()
# Lista []
# Dicionário {}

carros= {
    'uno': 'vermelho',
    'gol': 'branco',
    'celta': 'prata',
    'corsa': 'azul',
    'palio': 'verde'
}
# Adicionar item
carros['celta']='amarelo'
print(carros)
# Exibir somente os modelos dos veiculos 
print(carros.keys())

# carros2={
#     'uno':['verde', '4 portas']
# }

# Exibir as cores dos carros
print(carros.values())

# Exibir o dicionário inteiro
print(carros.items())
