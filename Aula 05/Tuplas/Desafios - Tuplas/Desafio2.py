# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro Serie B de Futebol, Na ordem de colocação. 
# Depois mostre:
# A) Apenas os 3 primeiros colocados.
# B) Os últimos 3 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do São Paulo.



# Tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro Série B
tabelaCampeonatoPaulista = ('Palmeiras', 'Santos', 'Bragantino', 'São Paulo', 'Novorizontino', 'São Bernado', 'Ponte Preta', 'Inter de Limeira', 'Água Santa', 'Corinthians','Botafogo SP', 
'Portuguesa', 'Guarani', 'Ituano', 'Santo André')



# A) Apenas os 3 primeiros colocados
print(40*'-')
print(f" \n A) Os 3 primeiros colocados são:")
for primeiros in range(3):
    print(f"{primeiros + 1}º lugar: {tabelaCampeonatoPaulista[primeiros]}")



# B) Os últimos 3 colocados da tabela
print(40*'-')
ultimosColocados = tabelaCampeonatoPaulista[-3:]
print("B) Os últimos 3 colocados: ", ultimosColocados)




# C) Uma lista com os times em ordem alfabética
print(40*'-')
timesOrdemAlfabetica = sorted(tabelaCampeonatoPaulista)
print(f" \n C) Times em ordem alfabética:")
for time in timesOrdemAlfabetica:
    print(time)




# D) Posição na tabela do time do São Paulo
print(40*'-')
posicao_sao_paulo = tabelaCampeonatoPaulista.index('São Paulo') + 1
print("D) Posição do São Paulo na tabela: ", posicao_sao_paulo)