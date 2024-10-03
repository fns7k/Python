# Automação
# Biblioteca Selenium
# Biblioteca webdriver
# Baixar Chrome Driver


# 01 - Baixar Chrome Driver e colocá-lo na mesma pasta do Python

# 02 - Instalar biblioteca Selenium
        # pip install selenium

# 03 - Instalar biblioteca webdriver_manager
        # pip install webdriver_manager
        


# Importar biblioteca Selenium
from selenium import webdriver

# Importar biblioteca webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

# Importando serviço de utilização do navegador
from selenium.webdriver.chrome.service import Service

# Criando um serviço do Chrome
servico = Service(ChromeDriverManager().install())

# Criar uma variável para usar o navegador
navegarGoogle = webdriver.Chrome(service=servico)
navegarSenai = webdriver.Chrome(service=servico)
navegarMercadoLivre = webdriver.Chrome(service=servico)

# Abrindo o site do google
navegarGoogle.get("htpps://www.google.com")


# Abrindo o site do Senai
navegarSenai.get("https://sp.senai.br/cursos?unidade=117")


# Abrindo o site do Mercado Livre
navegarMercadoLivre.get("https://www.mercadolivre.com.br/")
# //*[@id="cb1-edit"]
navegarMercadoLivre.find_element('xpath', '//*[@id="cb1-edit"]').send_keys('notebook')
navegarMercadoLivre.find_element('xpath', '/html/body/header/div/div[2]/form/button').click()
navegarMercadoLivre.find_element('xpath', '//*[@id=":R2m55e6:-trigger"]').click()
navegarMercadoLivre.find_element('xpath', '//*[@id=":R2m55e6:-menu-list-option-price_asc"]').click()

# Pausa no programa
input('digite enter para fechar')