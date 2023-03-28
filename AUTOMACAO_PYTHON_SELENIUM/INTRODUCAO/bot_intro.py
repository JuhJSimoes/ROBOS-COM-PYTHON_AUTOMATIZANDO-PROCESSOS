from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print("Iniciando bot \n")

driver = webdriver.Chrome('AUTOMACAO_PYTHON_SELENIUM\\INTRODUCAO\\chromedriver')
driver.get('https://registro.br/')
driver.maximize_window()
time.sleep(3)

buscar_dominio = driver.find_element(By.ID, "is-avail-field") #Buscando o input PESQUISAR DOMINIO por elemento
buscar_dominio.clear() #limpando o PESQUISAR DOMINIO
buscar_dominio.send_keys('botsinpython.com.br') #digitando na barra de pesquisa
buscar_dominio.send_keys(Keys.RETURN) #buscando (enter)

resultados = buscar_dominio.find_elements(By.TAG_NAME, 'strong')
print(resultados)

time.sleep(2)
driver.close()