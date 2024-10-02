carros= ('Gol', 'Uno', 'Fiesta', 'Palio', 'Celta', 'Kombi')


# for aux in range(5):

# Método para capturar o tamanho de um elemento --> len
tamanhoTupla= len(carros)
print(tamanhoTupla)

# Exibindo corretamente a Tupla
for aux in range(tamanhoTupla):
    print (carros[aux])


# Verificar se tem uma Kombi
temKombi = 'Kombi' in carros

if temKombi:
    print("A tupla contém uma Kombi.")
else:
    print("A tupla não contém uma Kombi.")
    
    
    

# Verificar se tem uma Kombi - Forma 1 (Professor):
verificar = False
for aux in range(tamanhoTupla):
    if carros[aux] == 'Kombi':
        verificar = True
if verificar == True:
    print('tem Kombi')
else:
    print('Não tem Kombi')
    
    
    

# Verificar se tem uma Kombi - Forma 2 (Professor):
if 'Kombi' in carros:
    print('Tem Kombi')
    
    
    

# Verificar se tem uma Kombi - Forma 3 (Professor):
if 'Kombi' not in carros:
    print('Não tem kombi')