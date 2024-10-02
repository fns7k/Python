#perguntar se o aluno gosta do curso de phyton sabadão

while True:
    resposta= input('Você gosta de Python no sbadão? S ou N ')
    resposta = resposta.upper()#converter para maiúsculo
    if resposta == 'S':
        print('Resposta correta!\n Fim do programa...')
        break