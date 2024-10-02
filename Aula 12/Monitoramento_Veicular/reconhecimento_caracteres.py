# C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe

import cv2
import pytesseract

# Chamando o executável de reconhecimento de caracteres (biblioteca)
pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

#leitura de uma imagem que contém textos
placa = cv2.imread(r'<Aula 12>/<Monitoramento_Veicular>/livro.jpg', 0)

# Conveter/capturar textos da imagem
placa = cv2.imread("")
meusTextos = pytesseract.image_to_string(placa, config='1 eng --oem 3 --psm 12')

print(meusTextos)