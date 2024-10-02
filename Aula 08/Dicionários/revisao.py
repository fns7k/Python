# Chave e valor 
# Cantor --> musica

dicMusicas = {
    "cidadeNegra":"pensamento",
    "chitaozinho e chororó": "menino da porteira",
    "legiao urbana": "tempo",
    "hungria": "coração de aço",
    "armandinho": "outra vida",
    "linkin park": "numb",
    "chico buarque": "valsinha",
    "pericles": "graveto"
}

# Imprimir de forma correta, aparecer "O cantor 'cidadeNegra' tem a música 'pensamento'", a cada linha porém com todas as acima 
# print(dicMusicas)

    
    
for cantor, musica in dicMusicas.items():
    print(f"O cantor {cantor.lower()} tem uma musica chamada {musica}.")
    


dicMusicas ["Manoel Gomes"] = "Caneta Azul"     # Adicionar cantor e uma música na lista

dicMusicas ["Rihana"] = "brain", "diamonds"     # Adicionar duas músicas na lista

print(40*'-')
for cantor, musica in dicMusicas.items():
    print(f"O cantor {cantor.lower()} tem uma musica chamada {musica}.")