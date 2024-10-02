# Exemplo listas


# Criar uma lista com 4 nomes de alunos
alunosPython=['Enzo', 'Raul', 'Jonathan', 'Pedro']


# Exibir lista corretamente 
for aluno in alunosPython:
    print(aluno)
    
    
    
linha= 12*'#'    
    
    
print(linha)
for indice in range(len(alunosPython)):
    print(alunosPython[indice])
    
    
print(linha)
cursosSenai=['Java', 'Python', 'Bancos de Dados', 'JavaScript']
print(cursosSenai[2][4])


print(linha)
nomeEscola= 'SENAI'
print(nomeEscola[3])


print(linha)


# Lista de lista
cursoPython=[['aula 1', 'aula 2', 'aula 3', 'aula 4'],['Tipos de dados', 'Condicionais', 'Laços de Repetição', 'Tuplas']]

print(f'Na {cursoPython[0][0]} de python: aprendemos {cursoPython[1][0]}')



# Exibir todas as aulas e conteúdo dado
# crie um laço de repetição para mostrar cada aula e o conteudo usando o exemplo abaixo
print(12*'#')

cursoPython=[['aula 1', 'aula 2', 'aula 3', 'aula 4'],['Tipos de dados', 'Condicionais', 'Laços de Repetição', 'Tuplas']]

for ind1 in range(len(cursoPython[0])):
    for ind2 in range(len(cursoPython)):
        print(f'Na {cursoPython[ind2][ind1]} de python: aprendemos {cursoPython[ind2+1][ind1]}')
        break
