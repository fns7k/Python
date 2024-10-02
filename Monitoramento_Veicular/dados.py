# Salvar informações dos proprietários de veículos

# Cadastramento
def informacoes():
    pessoas = {
        'OTM 2022': ['MARLON', 'NEW CIVIC', 2022],
        'AAA-5551': ['ENZO', 'GOLF', 2021],
        'ERM-5431': ['RAUL', 'ECLIPSE', 2023],
        'XXX-0000': ['JONATHAN', 'LANCER', 2022],
        'HQW-5678': ['GUSTAVO', 'NEW BEATLE', 2023]
    }
    return pessoas

# # Exibir todos os dados do dicionário (um em baixo do outro)
# print([dados for dados in pessoas.values()])
# print('\n')

# # Exibir todas as placas de veiculos (somente as placas)
# print(pessoas.keys())
# print('\n')

# # Exibir todos os proprietários de veículos (somente os proprietários)
# print([dados[0] for dados in pessoas.values()])