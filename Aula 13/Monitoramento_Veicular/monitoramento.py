# Importando biblioteca padrão de sistema
import sys
import cv2
# Importando biblioteca PyQt6 com seus elementos
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit



def camera():
        # Criando uma variável para capturar imagens (frames)
    print("Câmera aberta")
    camera = cv2.VideoCapture(1)

    # Loop para percorrer frame a frame, imagem por imagem
    while True:
        sucesso, frame = camera.read()
        cv2.imshow("imagem video", frame)

        if cv2.waitKey(1) & 0xFF == ord("s"):
            break

    camera.release()
    cv2.destroyAllWindows()



app = QApplication(sys.argv)
janela = QWidget()
janela.resize(400,400)
janela.setWindowTitle("Monitoramento Veicular")



# Carregar o arquivo CSS
with open("Aula 12/Monitoramento_Veicular/styles.css", "r") as file:
    css = file.read()
    app.setStyleSheet(css)
    
    

lblNome = QLabel("Monitoramento Veicular", janela)
lblNome.move(110,30)
lblNome.setStyleSheet("font-size: 15px")



lblLogin = QLabel("Nome", janela)
lblLogin.move(50, 80)

txtLogin = QLineEdit("", janela)
txtLogin.setGeometry(150, 80, 200, 20)



lblModelo = QLabel("Modelo", janela)
lblModelo.move(50,130)

txtModelo = QLineEdit("", janela)
txtModelo.setGeometry(150, 130, 200, 20)



lblPlaca = QLabel("Placa", janela)
lblPlaca.move(50,180)

txtPlaca = QLineEdit("", janela)
txtPlaca.setGeometry(150, 180, 200, 20)



lblAno = QLabel("Ano Veículo", janela)
lblAno.move(50,230)

txtAno = QLineEdit("", janela)
txtAno.setGeometry(150, 230, 200, 20)



btnCamera = QPushButton("Abrir Câmera", janela)
btnCamera.setGeometry(50,290,300,50)
btnCamera.clicked.connect(camera)



janela.show()
app.exec()
