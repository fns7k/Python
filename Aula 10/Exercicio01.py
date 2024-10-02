# Importando biblioteca padrão de sistema
import sys  
# Importando biblioteca PyQt6 com seus elementos
from PyQt6.QtWidgets import *  
from PyQt6.QtGui import *  # O asterisco serve para importar tudo de uma vez só

# Função chamada quando o botão "Entrar" é pressionado
def entrar():
    email = txtLogin.text()  # Obtém o texto do campo de login.
    senha = txtSenha.text()  # Obtém o texto do campo de senha.
    # Aqui você pode adicionar lógica para validar o email e a senha.
    print(f"Email: {email}, Senha: {senha}")  # Exibe o email e a senha no console (para fins de teste).

# Inicializando a aplicação
app = QApplication(sys.argv)
janela = QWidget()  # Cria a janela principal
janela.resize(450, 735)  # Define o tamanho da janela
janela.setWindowTitle("Login Netflix")  # Define o título da janela

# Carregando o estilo CSS
with open("Aula 10/style01.css", "r") as file:  # Abre o arquivo CSS
    app.setStyleSheet(file.read())  # Aplica o estilo da aplicação

# Estilizando labels
lblNome = QLabel("Entrar", janela)  # Cria um rótulo com o texto "Entrar"
lblNome.move(60, 48)  # Define a posição do rótulo
lblNome.setStyleSheet("font-family: Netflix Sans,Helvetica Neue,Segoe UI,Roboto,Ubuntu,sans-serif; "
                      "text-align: left; margin-block-start: 0; margin-block-end: 0; margin: 0; padding: 0; "
                      "color: rgb(255,255,255); font-size: 2rem; font-weight: 700; margin-bottom: 28px; "
                      "font-size: 30px;")  # Aplica o estilo ao rótulo

# Estilizando campos de texto
txtLogin = QLineEdit("", janela)  # Cria um campo de entrada para o login
txtLogin.setGeometry(60, 120, 330, 55)  # Define a posição e o tamanho do campo de texto
txtLogin.setPlaceholderText("Email ou número de celular")  # Define o texto de placeholder

txtSenha = QLineEdit("", janela)  # Cria um campo de entrada para a senha
txtSenha.setGeometry(60, 193, 330, 55)  # Define a posição e o tamanho do campo de texto
txtSenha.setPlaceholderText("Senha")  # Define o texto de placeholder
txtSenha.setEchoMode(QLineEdit.EchoMode.Password)  # Oculta a senha enquanto é digitada

# Estilizando botão
btnEntrar = QPushButton("Entrar", janela)  # Cria um botão com o texto "Entrar"
btnEntrar.setGeometry(60, 264, 330, 39)  # Define a posição e o tamanho do botão
btnEntrar.clicked.connect(entrar)  # Conecta o botão à função 'entrar'

# Exibindo a janela
janela.show()  
sys.exit(app.exec())  # Inicia o loop de eventos da aplicação
