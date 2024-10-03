# C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe

import cv2
import pytesseract

def reconhecer(imagem):
    # Chamando o executável de reconhecimento de caracteres (biblioteca)
    pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    #leitura de uma imagem que contém textos
    placa = cv2.imread(imagem, 0)

    # Conveter/capturar textos da imagem
    meusTextos = pytesseract.image_to_string(placa, config='1 eng --oem 3 --psm 12')

    # print(meusTextos)
    return meusTextos



# Enviar uma imagem para a função e exibir os textos reconhecidos
imagem = "livro.jpg"

textosReconhecidos = reconhecer(imagem)
print(textosReconhecidos)