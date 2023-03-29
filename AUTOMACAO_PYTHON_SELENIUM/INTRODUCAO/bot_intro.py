from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlrd
import pandas as pd


print("Iniciando bot \n")

#Lendo do excel
df_dominios = pd.read_excel('AUTOMACAO_PYTHON_SELENIUM\\INTRODUCAO\\dominios.xlsx', sheet_name='Planilha1')
print(df_dominios)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
#chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('AUTOMACAO_PYTHON_SELENIUM\\INTRODUCAO\\chromedriver.exe', chrome_options=chrome_options)
driver.get('https://registro.br/')
driver.maximize_window()

time.sleep(2)

status_disponivel = 'disponível'
status_indisponivel = 'não disponível'

#Criando lista com os dominios para pesquisa
#dominios = ['botcompythoneselenium.com.br','udemy.com','g1.globo.com', 'telecine.com.br', 'julianajsimoes.com.br']

resultados = {'Dominio' : [], 'Status' : []}

for dominio in df_dominios.iloc[:,0]: #Loop na lista de dominios
    buscar_dominio = driver.find_element(By.ID, "is-avail-field") #Buscando o input PESQUISAR DOMINIO por elemento
    buscar_dominio.clear() #limpando o PESQUISAR DOMINIO
    buscar_dominio.send_keys(dominio) #digitando na barra de pesquisa
    buscar_dominio.send_keys(Keys.RETURN) #buscando (enter)

    time.sleep(3)

    status = ''
    resultados_status = driver.find_elements(By.TAG_NAME, "strong")

    for r in resultados_status:
        if r.text == status_disponivel:
            status = status_disponivel
            break
        elif r.text == status_indisponivel:
            status = status_indisponivel
            break
            
    resultados['Dominio'].append(dominio)
    resultados['Status'].append(status)

df_resultados = pd.DataFrame(resultados)
df_resultados.to_excel('AUTOMACAO_PYTHON_SELENIUM\\INTRODUCAO\\resultado.xlsx', index=False)

time.sleep(2)
driver.close()