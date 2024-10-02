produtos = [['banana', 'abacate'], [3.50, 5.50]]  # Cria uma lista de produtos, onde a primeira sublista contém os nomes dos produtos e a segunda sublista contém os preços correspondentes.

# Qual o preço da banana?
for indice in range(len(produtos[0])):  # Itera sobre o comprimento da primeira sublista (nomes dos produtos).
    if produtos[0][indice] == 'banana':  # Verifica se o produto na posição atual é 'banana'.
        print(f'O preço da banana é: R${produtos[1][indice]}')  # Se for 'banana', imprime o preço correspondente da segunda sublista.
        break  # Interrompe o loop, pois a banana já foi encontrada.
else:
    print('A banana não está disponível na lista de produtos.')  # Se a banana não for encontrada no loop, imprime que não está disponível.

# Qual o preço do abacate?
for ind1 in range(len(produtos[0])):  # Itera sobre o comprimento da primeira sublista (nomes dos produtos).
    if produtos[0][ind1] == 'abacate':  # Verifica se o produto na posição atual é 'abacate'.
        print(f'O preço da abacate é: R${produtos[1][ind1]}')  # Se for 'abacate', imprime o preço correspondente da segunda sublista.
        break  # Interrompe o loop, pois o abacate já foi encontrado.
else:
    print('O abacate não está disponível na lista de produtos.')  # Se o abacate não for encontrado no loop, imprime que não está disponível.

print(40*'-')  # Imprime uma linha de separação com 40 traços.





# Exemplo professor:

tem_banana = False  # Inicializa a variável 'tem_banana' como False (não sabemos ainda se há banana na lista).
tem_abacate = False  # Inicializa a variável 'tem_abacate' como False (não sabemos ainda se há abacate na lista).

if "banana" in produtos[0]:  # Verifica se 'banana' está na primeira sublista (nomes dos produtos).
    tem_banana = True  # Se 'banana' estiver presente, define 'tem_banana' como True.

if "abacate" in produtos[0]:  # Verifica se 'abacate' está na primeira sublista (nomes dos produtos).
    tem_abacate = True  # Se 'abacate' estiver presente, define 'tem_abacate' como True.

if tem_banana == True:  # Se 'tem_banana' for True, ou seja, se houver banana na lista:
    for auxiliar in range(len(produtos[0])):  # Itera sobre o comprimento da primeira sublista.
        if 'banana' == produtos[0][auxiliar]:  # Verifica se o produto atual é 'banana'.
            print(f'O preço da banana é {produtos[1][auxiliar]}')  # Imprime o preço da banana.
else: 
    print('não tem banana')  # Se 'tem_banana' for False, imprime que não há banana.

if tem_abacate == True:  # Se 'tem_abacate' for True, ou seja, se houver abacate na lista:
    for auxiliar in range(len(produtos[0])):  # Itera sobre o comprimento da primeira sublista.
        if 'abacate' == produtos[0][auxiliar]:  # Verifica se o produto atual é 'abacate'.
            print(f'O preço do abacate é {produtos[1][auxiliar]}')  # Imprime o preço do abacate.
else: 
    print('não tem abacate')  # Se 'tem_abacate' for False, imprime que não há abacate.
