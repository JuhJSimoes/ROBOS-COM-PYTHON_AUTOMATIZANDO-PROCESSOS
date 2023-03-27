import pyautogui

#.screenshot ('my_screenshot.png')
#Grava uma foto da tela e sava no arquivo my_screenshot.png
pyautogui.screenshot ('my_screenshot.png')


#.screenshot(region=(0,0, 300, 400))
#Caso não seja necessario screenshot da tela toda, é possivel passar uma regiao para a screenshot ser tirada.
#Sao quatro inteiros que delimitam a esqueda, topo, largura e altura.
pyautogui.screenshot ('my_screenshot_02.png',region=(0,0,300,400))


