import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BotYoutube():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        
        self.webdriver = webdriver.Chrome(chrome_options=chrome_options)
        
    def busca(self, busca, paginas):
        self.webdriver.maximize_window()
        time.sleep(1)
        
        videos = []
        pagina = 1
                
        url = 'https://www.youtube.com/results?search_query=%s' % busca
        self.webdriver.get(url)
        
        while pagina <= paginas:
            titulos = self.webdriver.find_elements(By.XPATH, '//a[@id="video-title" ]' )
            for titulo in titulos:
                if titulo.text not in videos:
                    print("Vídeo encontrado: %s" % titulo.text)
                    videos.append(titulo.text)   
                                    
                    with open('AUTOMACAO_PYTHON_SELENIUM\\AUTOMATIZANDO_BUSCAS_YOUTUBE\\resultado.txt', 'a', encoding='utf-8') as arquivo:
                        for resultado in videos:
                            arquivo.write('Resultado da página - %s: %s \n' % (pagina, resultado))
                    arquivo.close()
                    
            self.proxima_pagina(pagina)
            pagina += 1
            
    
    def proxima_pagina(self, pagina):
        print('\n Mudando para a página %s' % (pagina+1))
        bottom = pagina * 10000
        self.webdriver.execute_script("window.scrollTo(0, %s);" % bottom)
        time.sleep(5)
        
    


bot = BotYoutube()
bot.busca('zen budismo',3)
time.sleep(1)