# Revisão de função
def desenvolvimento():
    nomeDesenvolvedor = "Gustavo Andrigo"
    linguagem = "Python"
    print("Desenvolvedor do programa: ", nomeDesenvolvedor)
    print("Linguagem de desenvolvimento: ", linguagem)

def curso():
    nomeCurso = 'Python'
    return nomeCurso

print(f"Informações sobre o programa: ")
desenvolvimento()

nomeCurso = curso()
print("O nome do curso é: ", nomeCurso)