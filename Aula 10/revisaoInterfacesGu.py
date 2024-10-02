# Importando biblioteca padrão de sistema
import sys
# Importando biblioteca PyQt6 com seus elementos
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QFont  # Importa a classe QFont, que pode ser usada para definir fontes (não está sendo utilizada neste trecho)

# Inicializa a aplicação
app = QApplication(sys.argv)
janela = QWidget()  # Cria uma nova janela
janela.resize(400, 600)  # Define o tamanho da janela
janela.setWindowTitle("Exemplo Interface")  # Define o título da janela

# Carrega o estilo CSS a partir do arquivo
with open("Aula 10/styles.css", "r") as file:
    app.setStyleSheet(file.read())  # Aplica o estilo lido na aplicação

# Estilizando rótulos (labels)
lblNome = QLabel("Exemplo Tela", janela)  # Rótulo para o título
lblNome.move(155, 30)  # Define a posição do rótulo na janela

lblLogin = QLabel("Login", janela)  # Rótulo para o campo de login
lblLogin.move(50, 80)  # Define a posição do rótulo na janela

lblSenha = QLabel("Senha", janela)  # Rótulo para o campo de senha
lblSenha.move(50, 150)  # Define a posição do rótulo na janela

# Estilizando campos de texto
txtLogin = QLineEdit("", janela)  # Campo de texto para o login
txtLogin.setGeometry(150, 80, 200, 20)  # Define a posição e o tamanho do campo de texto

txtSenha = QLineEdit("", janela)  # Campo de texto para a senha
txtSenha.setGeometry(150, 150, 200, 20)  # Define a posição e o tamanho do campo de texto

# Estilizando botão
btnEntrar = QPushButton("Entrar", janela)  # Botão para realizar o login
btnEntrar.setGeometry(50, 230, 300, 50)  # Define a posição e o tamanho do botão

# Exibe a janela
janela.show()
# Inicia o loop de eventos da aplicação
app.exec()
