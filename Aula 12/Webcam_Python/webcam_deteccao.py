import cv2

# Criando uma variável para capturar imagens (frames)
camera = cv2.VideoCapture(0)

# Carregar o arquivo treinado para detectar faces
cascadeFace = cv2.CascadeClassifier("Aula 12/Webcam_Python/haarcascade_frontalface_default.xml")

# Loop para percorrer frame a frame, imagem por imagem
while True:
    sucesso, frame = camera.read()

    # Convertendo a imagem para tons de cinza
    imagensTonsDeCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Utilizar arquivo de detecção para detectar rostos
    faces = cascadeFace.detectMultiScale(imagensTonsDeCinza, scaleFactor=1.1, minNeighbors=5, minSize=(5,5))

    # Desenhar um retângulo em torno de cada rosto detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibir o frame com os retângulos dos rostos detectados
    cv2.imshow("Detecção de Rosto", frame)

    # Aguardar pela tecla 's' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

# Liberar os recursos da câmera e fechar todas as janelas
camera.release()
cv2.destroyAllWindows()
