import cv2

imagemOriginal = cv2.imread("Aula 12/Webcam_Python/pessoas.jpg")


# Testar
cv2.imshow("Pessoas", imagemOriginal)
cv2.waitKey(0)


# Carregar o arquivo treinado para detectar faces
cascadeFace = cv2.CascadeClassifier("Aula 12/Webcam_Python/haarcascade_frontalface_default.xml")


# Converter a imagem para tons de cinza
imagensTonsDeCinza = cv2.cvtColor(imagemOriginal, cv2.COLOR_BGR2GRAY)


# Teste
cv2.imshow("Tons de cinza", imagensTonsDeCinza)
cv2.waitKey(0)


# Utilizar arquivo de detecção
faces = cascadeFace.detectMultiScale(imagensTonsDeCinza, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))


# Desenhar um retângulo na imagem
for (x,y,w,h) in faces:
    cv2.rectangle(imagemOriginal, (x,y), (x+w, y+h), (0,255,0), 2)
    
    
cv2.imshow("Resultado", imagemOriginal)
cv2.waitKey(0)
cv2.destroyAllWindows()