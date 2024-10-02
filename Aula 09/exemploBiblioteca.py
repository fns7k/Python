# Open cv
# pip install opencv-python
# Instala o pacote OpenCV, necessário para trabalhar com processamento de imagens.

import cv2  # Importa o módulo OpenCV, que oferece funções para manipulação de imagens e vídeos.

# Abrir uma imagem
imagem = cv2.imread("aranha.jpg")  # Lê a imagem "aranha.jpg" e armazena o conteúdo da imagem na variável 'imagem'.
cv2.imshow('janela', imagem)  # Exibe a imagem em uma janela nomeada 'janela'.

cv2.waitKey(0)  # Aguarda até que uma tecla seja pressionada para fechar a janela.
cv2.destroyAllWindows()  # Fecha todas as janelas abertas pelo OpenCV.
