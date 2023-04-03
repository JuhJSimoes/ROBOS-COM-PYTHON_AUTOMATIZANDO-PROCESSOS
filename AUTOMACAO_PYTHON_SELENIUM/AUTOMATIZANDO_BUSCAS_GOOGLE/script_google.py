from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd


print('\n Inciando robo de busca - GOOGLE \n')

pesquisa = input('Digite que ou quem deseja pesquisar: \n')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome('AUTOMACAO_PYTHON_SELENIUM\\AUTOMATIZANDO_BUSCAS_GOOGLE\\chromedriver.exe', chrome_options = chrome_options) #necessário ter o chromedriver na pasta do robô e a versão precisa ser a mesma do Chrome instalado na máquina.
driver.get('https://www.google.com.br/')
driver.maximize_window()

campo_pesquisar = driver.find_element(By.XPATH, '//input[@aria-label="Pesquisar"]')
time.sleep(2)
campo_pesquisar.send_keys(pesquisa)
campo_pesquisar.send_keys(Keys.ENTER)

status_resultado = driver.find_element(By.XPATH, '//div[@id="result-stats"]').text
print(status_resultado)

num_resultados = int(status_resultado.split('Aproximadamente ')[1].split(' resultados')[0].replace('.', ''))
maximo_paginas = num_resultados/10
print('\n')

pagina_maxima = input("%s páginas encontradas, até qual página deseja ler os resultados?" % (maximo_paginas))
print('\n')

url_pagina = driver.find_element(By.XPATH, '//a[@aria-label="Page 2"]').get_attribute('href')
print(url_pagina)

pagina_atual = 1
start = 10
lista_resultados= []

while pagina_atual <= int(pagina_maxima):
    print(pagina_atual)
    if pagina_atual > 1 :
        url_pagina = url_pagina.replace('start=%s' % start, 'start=%s' % (start+10))
        start += 10      
    
    divs = driver.find_elements(By.XPATH, "//div[@class = 'g Ww4FFb vt6azd tF2Cxc asEBEc']")
    
    for div in divs:
        nome = div.find_element(By.TAG_NAME, 'h3')
        link = div.find_element(By.TAG_NAME, 'a')
        resultado = "%s; %s" % (nome.text, link.get_attribute('href'))
        print(resultado)        
        lista_resultados.append(resultado)
    
    print('\n')
    pagina_atual += 1
    driver.get(url_pagina)


with open('AUTOMACAO_PYTHON_SELENIUM\\AUTOMATIZANDO_BUSCAS_GOOGLE\\resultado.txt', 'w', encoding='utf-8') as arquivo:
    for resultado in lista_resultados:
        arquivo.write('%s \n' % resultado)
    arquivo.close()

print("%s resultados encontrados do Google e salvos no resultado.txt" % len(lista_resultados))




