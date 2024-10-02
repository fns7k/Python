# Importando biblioteca padrão de sistema
import sys
# Importando biblioteca PyQt6 com seus elementos
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

# Inicializa a aplicação
app = QApplication(sys.argv)
janela = QWidget()  # Cria uma nova janela
janela.resize(400, 600)  # Define o tamanho da janela
janela.setWindowTitle("Exemplo Interface")  # Define o título da janela

# Carrega o estilo CSS a partir do arquivo
with open("Aula 10/style.css", "r") as file:
    app.setStyleSheet(file.read())  # Aplica o estilo lido na aplicação

# Criando e estilizando um rótulo de título
lblNome = QLabel("Exemplo Tela", janela)  # Rótulo para o título
lblNome.move(160, 30)  # Define a posição do rótulo
lblNome.setStyleSheet("font-size: 15px")  # Define o tamanho da fonte

# Criando e posicionando rótulo para o login
lblLogin = QLabel("Login", janela)  # Rótulo para campo de login
lblLogin.move(50, 80)  # Define a posição do rótulo

# Criando campo de entrada para o login
txtLogin = QLineEdit("", janela)  # Campo de texto para o login
txtLogin.setGeometry(150, 80, 200, 20)  # Define a posição e o tamanho do campo de texto

# Criando e posicionando rótulo para a senha
lblSenha = QLabel("Senha", janela)  # Rótulo para campo de senha
lblSenha.move(50, 150)  # Define a posição do rótulo

# Criando campo de entrada para a senha
txtSenha = QLineEdit("", janela)  # Campo de texto para a senha
txtSenha.setGeometry(150, 150, 200, 20)  # Define a posição e o tamanho do campo de texto
# txtSenha.setStyleSheet("")  # Aqui você pode adicionar estilo para o campo de senha, se necessário

# Criando e estilizando o botão de entrada
btnEntrar = QPushButton("Entrar", janela)  # Botão para realizar o login
btnEntrar.setGeometry(50, 230, 300, 50)  # Define a posição e o tamanho do botão
btnEntrar.setStyleSheet("background-color: white; font-size: 20px")  # Define o estilo do botão

# txt --> se refere a caixas de texto
# btn --> se refere a botões
# lbl --> se refere a rótulos (labels)

# Exibe a janela
janela.show()
# Inicia o loop de eventos da aplicação
app.exec()
