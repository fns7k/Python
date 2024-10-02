# Exemplo listas

# Criar uma lista com 4 nomes de alunos
alunosPython=['Enzo', 'Raul', 'Jonathan', 'Pedro']  # Cria uma lista chamada 'alunosPython' com 4 nomes de alunos.

# Exibir lista corretamente 
for aluno in alunosPython:  # Itera sobre cada elemento da lista 'alunosPython'.
    print(aluno)  # Imprime o nome de cada aluno.

linha= 12*'#'  # Cria uma string contendo 12 caracteres '#'.

print(linha)  # Imprime a linha com 12 '#'.
for indice in range(len(alunosPython)):  # Itera sobre o índice de cada aluno na lista 'alunosPython'.
    print(alunosPython[indice])  # Imprime o aluno na posição indicada pelo índice.

print(linha)  # Imprime a linha com 12 '#'.
cursosSenai=['Java', 'Python', 'Bancos de Dados', 'JavaScript']  # Cria uma lista chamada 'cursosSenai' com 4 nomes de cursos.
print(cursosSenai[2][4])  # Tenta imprimir o 5º caractere (índice 4) do 3º curso (índice 2) na lista 'cursosSenai', ou seja, "o" de "Bancos de Dados".

print(linha)  # Imprime a linha com 12 '#'.
nomeEscola= 'SENAI'  # Cria uma string chamada 'nomeEscola' com o valor 'SENAI'.
print(nomeEscola[3])  # Imprime o 4º caractere (índice 3) da string 'SENAI', que é 'A'.

print(linha)  # Imprime a linha com 12 '#'.

# Lista de lista
cursoPython=[['aula 1', 'aula 2', 'aula 3', 'aula 4'],['Tipos de dados', 'Condicionais', 'Laços de Repetição', 'Tuplas']]  # Cria uma lista contendo duas sublistas: uma com nomes de aulas e outra com os respectivos conteúdos.

print(f'Na {cursoPython[0][0]} de python: aprendemos {cursoPython[1][0]}')  # Acessa a 1ª aula e o conteúdo correspondente, imprimindo "Na aula 1 de python: aprendemos Tipos de dados".

# Exibir todas as aulas e conteúdo dado
# Crie um laço de repetição para mostrar cada aula e o conteúdo usando o exemplo abaixo
print(12*'#')  # Imprime uma linha de separação com 12 '#'.

cursoPython=[['aula 1', 'aula 2', 'aula 3', 'aula 4'],['Tipos de dados', 'Condicionais', 'Laços de Repetição', 'Tuplas']]  # Recria a lista de listas com aulas e conteúdos.

for ind1 in range(len(cursoPython[0])):  # Itera sobre os índices da primeira sublista (aulas).
    for ind2 in range(len(cursoPython)):  # Itera sobre os índices de ambas as sublistas (aulas e conteúdos).
        print(f'Na {cursoPython[ind2][ind1]} de python: aprendemos {cursoPython[ind2+1][ind1]}')  # Acessa a aula e o conteúdo correspondente usando os índices.
        break  # Sai do segundo laço após imprimir a aula e o conteúdo.
