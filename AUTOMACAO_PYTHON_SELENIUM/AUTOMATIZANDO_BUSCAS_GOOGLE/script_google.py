from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


print('\n Inciando robo de busca - GOOGLE \n')

#pesquisa = input('Digite que ou quem deseja pesquisar: \n')
pesquisa = 'pitty'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome('AUTOMACAO_PYTHON_SELENIUM\\AUTOMATIZANDO_BUSCAS_GOOGLE\\chromedriver.exe', chrome_options = chrome_options) #necessário ter o chromedriver na pasta do robô e a versão precisa ser a mesma do Chrome instalado na máquina.
driver.get('https://www.google.com.br/')
driver.maximize_window()

campo_pesquisar = driver.find_element(By.XPATH, '//input[@aria-label="Pesquisar"]')
campo_pesquisar.send_keys(pesquisa)
campo_pesquisar.send_keys(Keys.ENTER)

status_resultado = driver.find_element(By.XPATH, '//div[@id="result-stats"]')
print(status_resultado.text)






