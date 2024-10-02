# DESAFIO 03
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Sabendo que ele vai se aposentar após 35 anos de colaboração.



# Função para calcular a idade com base no ano de nascimento
def calcularIdade(anoNascimento):
    anoAtual = 2024  
    return anoAtual - anoNascimento


# Função para calcular o ano de aposentadoria
def calcularAposentadoria(anoContratacao):
    return anoContratacao + 35     # 30 anos para mulher e 35 anos para homem.


# Dicionário para armazenar os dados dos funcionários
funcionarios = []

# Loop para cada funcionário
while True:
    nome = input("Digite o nome do funcionário (ou deixe em branco para sair): ")
    
    # Se o nome estiver vazio, sai do loop
    if nome == '':
        break
    
    
    anoNascimento = int(input("Digite o ano de nascimento do funcionário: "))
    carteiraTrabalho = int(input("Digite o número da carteira de trabalho (ou 0 se não tiver): "))
    
    
    # Se tiver carteira de trabalho
    if carteiraTrabalho != 0:
        anoContratacao = int(input("Digite o ano de contratação: "))
        salario = float(input("Digite o salário: "))
        idade = calcularIdade(anoNascimento)
        aposentadoria = calcularAposentadoria(anoContratacao)
        funcionario = {
            'nome': nome,
            'idade': idade,
            'carteiraTrabalho': carteiraTrabalho,
            'anoContratacao': anoContratacao,
            'salario': salario,
            'aposentadoria': aposentadoria
        } 
    else:
        funcionario = {
            'nome': nome,
            'idade': calcularIdade(anoNascimento),
            'carteiraTrabalho': carteiraTrabalho
        }
    
    
    # Adicionando funcionário ao dicionário
    funcionarios.append(funcionario)
    
    
# Exibindo os funcionários cadastrados
print("\n" + "-" * 40)
for funcionario in funcionarios:
    print("\nFuncionário:", funcionario['nome'])
    print("Idade:", funcionario['idade'])
    print("Carteira de trabalho:", funcionario['carteiraTrabalho'])
    
    if funcionario['carteiraTrabalho'] != 0:
        print("Ano de contratação:", funcionario['anoContratacao'])
        print("Salário:", funcionario['salario'])
        print("Ano de aposentadoria:", funcionario['aposentadoria'])
