import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

# Função para calcular a expressão matemática
def calcular():
    expressao = inputCalculadora.text()  # Obtém o texto atual da entrada
    try:
        resultado = eval(expressao)  # Avalia a expressão matemática
        inputCalculadora.setText(str(resultado))  # Atualiza a entrada com o resultado
    except Exception as erro:  # Captura qualquer erro que ocorra
        inputCalculadora.setText("Erro")  # Exibe "Erro" na entrada se uma exceção for levantada

# Função para limpar a entrada
def limpar():
    inputCalculadora.setText("0")  # Redefine o texto da entrada para "0"

# Função para inverter o sinal do número atual
def inverterSinal():
    expressao = inputCalculadora.text()  # Obtém o texto atual da entrada
    if expressao[0] == '-':  # Se a expressão começar com "-"
        inputCalculadora.setText(expressao[1:])  # Remove o sinal negativo
    else:
        inputCalculadora.setText('-' + expressao)  # Adiciona um sinal negativo

# Função para adicionar valor à entrada
def adicionarAoInput(valor):
    if inputCalculadora.text() == "0":  # Se a entrada for "0", substitui
        inputCalculadora.setText(valor)
    else:
        inputCalculadora.setText(inputCalculadora.text() + valor)  # Adiciona o valor à entrada

# Inicializa a aplicação
app = QApplication(sys.argv)
janela = QWidget()
janela.resize(400, 520)  # Define o tamanho da janela
janela.setWindowTitle("Calculadora")  # Define o título da janela

tamanhoBotao = 81  # Define o tamanho dos botões

# Lê o conteúdo do arquivo CSS
with open('Aula 11/calculadora/style.css', 'r') as style_file:
    styles = style_file.read()

# Aplica o estilo à janela
janela.setStyleSheet(styles)

# Adiciona o Input
inputCalculadora = QLineEdit('0', janela)  # Cria um campo de entrada inicializado com "0"
inputCalculadora.move(39, 20)  # Move o campo para a posição desejada
inputCalculadora.setReadOnly(True)  # Define o campo como somente leitura
inputCalculadora.resize(322, 65)  # Define o tamanho do campo de entrada
inputCalculadora.setAlignment(Qt.AlignmentFlag.AlignRight)  # Alinha o texto à direita

# Adicionando os botões da calculadora
# 1ª linha
btnAC = QPushButton('AC', janela)
btnAC.setGeometry(39, 90, tamanhoBotao, tamanhoBotao)
btnAC.setObjectName('btnAC')
btnAC.clicked.connect(limpar)  # Conecta o botão 'AC' à função de limpar

btnE = QPushButton('+/-', janela)
btnE.setGeometry(119, 90, tamanhoBotao, tamanhoBotao)
btnE.setObjectName('btnE')
btnE.clicked.connect(inverterSinal)  # Conecta o botão '+/-' à função de inverter sinal

btnP = QPushButton('%', janela)
btnP.setGeometry(199, 90, tamanhoBotao, tamanhoBotao)
btnP.setObjectName('btnP')
btnP.clicked.connect(lambda: adicionarAoInput('%'))  # Conecta o botão '%' à função de adicionar valor

btnB = QPushButton('/', janela)
btnB.setGeometry(280, 90, tamanhoBotao, tamanhoBotao)
btnB.setObjectName('btnB')
btnB.clicked.connect(lambda: adicionarAoInput('/'))  # Conecta o botão '/' à função de adicionar valor

# 2ª linha
btn7 = QPushButton('7', janela)
btn7.setGeometry(39, 170, tamanhoBotao, tamanhoBotao)
btn7.clicked.connect(lambda: adicionarAoInput('7'))  # Conecta o botão '7'

btn8 = QPushButton('8', janela)
btn8.setGeometry(119, 170, tamanhoBotao, tamanhoBotao)
btn8.clicked.connect(lambda: adicionarAoInput('8'))  # Conecta o botão '8'

btn9 = QPushButton('9', janela)
btn9.setGeometry(199, 170, tamanhoBotao, tamanhoBotao)
btn9.clicked.connect(lambda: adicionarAoInput('9'))  # Conecta o botão '9'

btnX = QPushButton('X', janela)
btnX.setGeometry(280, 170, tamanhoBotao, tamanhoBotao)
btnX.clicked.connect(lambda: adicionarAoInput('*'))  # Conecta o botão 'X' à função de adicionar valor

# 3ª linha
btn4 = QPushButton('4', janela)
btn4.setGeometry(39, 250, tamanhoBotao, tamanhoBotao)
btn4.clicked.connect(lambda: adicionarAoInput('4'))  # Conecta o botão '4'

btn5 = QPushButton('5', janela)
btn5.setGeometry(119, 250, tamanhoBotao, tamanhoBotao)
btn5.clicked.connect(lambda: adicionarAoInput('5'))  # Conecta o botão '5'

btn6 = QPushButton('6', janela)
btn6.setGeometry(199, 250, tamanhoBotao, tamanhoBotao)
btn6.clicked.connect(lambda: adicionarAoInput('6'))  # Conecta o botão '6'

btnMe = QPushButton('-', janela)
btnMe.setGeometry(280, 250, tamanhoBotao, tamanhoBotao)
btnMe.clicked.connect(lambda: adicionarAoInput('-'))  # Conecta o botão '-' à função de adicionar valor

# 4ª linha
btn1 = QPushButton('1', janela)
btn1.setGeometry(39, 330, tamanhoBotao, tamanhoBotao)
btn1.clicked.connect(lambda: adicionarAoInput('1'))  # Conecta o botão '1'

btn2 = QPushButton('2', janela)
btn2.setGeometry(119, 330, tamanhoBotao, tamanhoBotao)
btn2.clicked.connect(lambda: adicionarAoInput('2'))  # Conecta o botão '2'

btn3 = QPushButton('3', janela)
btn3.setGeometry(199, 330, tamanhoBotao, tamanhoBotao)
btn3.clicked.connect(lambda: adicionarAoInput('3'))  # Conecta o botão '3'

btnMa = QPushButton('+', janela)
btnMa.setGeometry(280, 330, tamanhoBotao, tamanhoBotao)
btnMa.clicked.connect(lambda: adicionarAoInput('+'))  # Conecta o botão '+' à função de adicionar valor

# 5ª linha
btn0 = QPushButton('0', janela)
btn0.setGeometry(39, 410, tamanhoBotao, tamanhoBotao)
btn0.clicked.connect(lambda: adicionarAoInput('0'))  # Conecta o botão '0'

btnV = QPushButton(',', janela)
btnV.setGeometry(119, 410, tamanhoBotao, tamanhoBotao)
btnV.clicked.connect(lambda: adicionarAoInput('.'))  # Conecta o botão ',' à função de adicionar valor

btnR = QPushButton('√', janela)
btnR.setGeometry(199, 410, tamanhoBotao, tamanhoBotao)
btnR.clicked.connect(lambda: adicionarAoInput('**0.5'))  # Conecta o botão '√' à função de adicionar valor

btnI = QPushButton('=', janela)
btnI.setGeometry(280, 410, tamanhoBotao, tamanhoBotao)
btnI.clicked.connect(calcular)  # Conecta o botão '=' à função de calcular

# Exibe a janela
janela.show()
# Inicia o loop de eventos da aplicação
sys.exit(app.exec())
