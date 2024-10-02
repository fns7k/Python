# DESAFIO 01
# Escreva um programa em python que:
# Leia duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. 
# A entrada de dados deve terminar quando for lida uma string vazia como nome.
# No final exibir os nomes dos alunos com suas respectivas notas.



# Inicializa um dicionário para armazenar as notas dos alunos
notasAlunos = {}


# Loop infinito para ler as notas dos alunos
while True:
    nomeAluno = input("Digite o nome do aluno (ou deixe em branco para sair): ")
    
    # Se o nome estiver vazio, sai do loop
    if nomeAluno == '':
        break
    
    # Lê as duas notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Armazena as notas no dicionário
    notasAlunos[nomeAluno] = [nota1, nota2]


# Exibe os nomes dos alunos com suas respectivas notas
print("\nNotas dos alunos:")
for aluno, notas in notasAlunos.items():
    print(f"{aluno}: {notas[0]}, {notas[1]}")
