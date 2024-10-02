#usuario e senha

usuario= 'root'     #Declarando o usuário
senha= 1234     #Declarando a senha

print(40*'-')       #Imprimir 40 "-"
usuarioDigitado= input('Digite o nome de usuário: ')        #Pedir o usuário para o utilizador no terminal
senhaDigitada= int(input('Digite a sua senha: '))        #Pedir a senha para o utilizador no terminal
if usuarioDigitado== usuario:       #Utilizando o 'se' (condição), se o usuariodigitado foi igual ao usuário escrito pelo utilizador:
    print(40*'-')       #Imprimir 40 "-"
    print('Usuário Correto')        #Imprimir no terminal que o usuário foi correto
    if senhaDigitada== senha:       #Utilizando o 'se' (condição), se o senhadigitada foi igual a senha escrita pelo utilizador:
        print(40*'-')       #Imprimir 40 "-"
        print('Senha Correta')
    else:       #Utilizando o 'se não' (condição), imprimir que a senha foi incorreta
        print('Senha Incorreta')
else:       #Utilizando o 'se não' (condição), imprimir que o usuário foi incorreto
    print(40*'-')       #Imprimir 40 "-"
    print ('Usuario Incorreto')