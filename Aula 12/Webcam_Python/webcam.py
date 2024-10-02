import cv2

# Criando uma variável para capturar imagens (frames)
camera = cv2.VideoCapture(0)

# Loop para percorrer frame a frame, imagem por imagem
while True:
    sucesso, frame = camera.read()
    cv2.imshow("imagem video", frame)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()