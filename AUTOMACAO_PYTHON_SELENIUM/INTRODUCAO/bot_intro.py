from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import pdb

print("Iniciando bot \n")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
#chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('AUTOMACAO_PYTHON_SELENIUM\\INTRODUCAO\\chromedriver.exe', chrome_options=chrome_options)
driver.get('https://registro.br/')
driver.maximize_window()

time.sleep(2)

dominio = 'botcompythoneselenium.com.br'
buscar_dominio = driver.find_element(By.ID, "is-avail-field") #Buscando o input PESQUISAR DOMINIO por elemento
buscar_dominio.clear() #limpando o PESQUISAR DOMINIO
buscar_dominio.send_keys(dominio) #digitando na barra de pesquisa
buscar_dominio.send_keys(Keys.RETURN) #buscando (enter)

time.sleep(3)

resultados = driver.find_elements(By.TAG_NAME, "strong")

for r in resultados:
    if r.text == 'disponível':
        print('\n O domínio: %s está %s' %(dominio, r.text.upper()))
    elif r.text == 'não disponível':
        print('\n O domínio: %s está %s' %(dominio, r.text.upper()))

time.sleep(2)
driver.close()