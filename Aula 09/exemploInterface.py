import sys  # Importa o módulo 'sys', que permite acessar parâmetros e funcionalidades do sistema.
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit  # Importa classes necessárias para criar a interface gráfica.

app = QApplication(sys.argv)  # Inicializa a aplicação PyQt, necessária para o funcionamento da interface.
janela = QWidget()  # Cria uma janela base.
janela.resize(400, 600)  # Define o tamanho da janela para 400x600 pixels.
janela.setWindowTitle('Minha Janela')  # Define o título da janela.

# Adiciona um rótulo de título à janela.
titulo = QLabel('Primeira Janela', janela)  # Cria um QLabel com o texto 'Primeira Janela' na janela.
titulo.move(155, 20)  # Move o título para as coordenadas (155, 20) na janela.

# Adiciona um rótulo para o campo de nome.
lblNome = QLabel('nome', janela)  # Cria um QLabel com o texto 'nome' na janela.
lblNome.move(50, 100)  # Move o rótulo para as coordenadas (50, 100).

# Cria um campo de entrada de texto (para o nome).
txtNome = QLineEdit('', janela)  # Cria um QLineEdit (campo de texto) vazio na janela.
txtNome.setGeometry(100, 100, 200, 50)  # Define a posição e o tamanho do campo de entrada.

# Adiciona um botão de enviar.
btnEnviar = QPushButton('Enviar', janela)  # Cria um botão com o texto 'Enviar' na janela.
btnEnviar.setGeometry(100, 150, 100, 50)  # Define a posição e o tamanho do botão.

# Exibe a janela.
janela.show()  # Mostra a janela na tela.
app.exec()  # Executa o loop de eventos da aplicação.
