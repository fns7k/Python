# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro Serie B de Futebol, Na ordem de colocação. 
# Depois mostre:
# A) Apenas os 3 primeiros colocados.
# B) Os últimos 3 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do São Paulo.



# Tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro Série B
tabelaSerieB = ('Santos', 'América-MG', 'Avaí', 'Botafogo SP', 'Brusque', 'CRB', 'Ceará SC', 'Chapecoense', 'Coritiba', 'Goiás','Guarani', 'Ituano', 'Mirassol', 'Novorizontino', 
'Operário', 'Paysandu', 'Ponte Preta', 'Santos', 'Sport Recife', 'Vila Nova')



# A) Apenas os 3 primeiros colocados
print(40*'-')
print("A) Os 3 primeiros colocados:")
for variavel in range(3):
    print(f"{variavel + 1}º lugar: {tabelaSerieB[variavel]}")



# B) Os últimos 3 colocados da tabela
print(f" \n {print(40*'-')} \n B) Os últimos 3 colocados:")
for variavel in range(-3, 0):
    print(f"{len(tabelaSerieB) + variavel + 1}º lugar: {tabelaSerieB[variavel]}")



# C) Uma lista com os times em ordem alfabética
timesOrdemAlfabetica = sorted(tabelaSerieB)
print(f" \n C) Times em ordem alfabética:")
for time in timesOrdemAlfabetica:
    print(time)



# D) Em que posição na tabela está o time do São Paulo
timePesquisado = 'São Paulo'
if timePesquisado in tabelaSerieB:
    saoPauloPosicao = tabelaSerieB.index(timePesquisado) + 1
    print(f" \n {print(40*'-')} \n D) Posição na tabela do São Paulo:", saoPauloPosicao)
else:
    print(f" \n {print(40*'-')} \n D) O Time '{timePesquisado}' não foi encontrado na tabela.")
