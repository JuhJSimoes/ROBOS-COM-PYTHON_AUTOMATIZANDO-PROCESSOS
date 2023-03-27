import pyautogui
import time


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('chrome /incognito www.gabrielcasemiro.com.br/atividade_pyautogui \n')

time.sleep(3)

with open('membros.csv') as f:
    next(f)

    for line in f:
        line = line.strip()
        line = line.split(';')
        print('Dados: ', line)
        
        name=line[0]
        pyautogui.click(pyautogui.locateCenterOnScreen('img\\nome.png', confidence=0.8))
        pyautogui.typewrite(name, interval = 0.1)
        
        email=line[2]
        pyautogui.click(pyautogui.locateCenterOnScreen('img\\email.png', confidence=0.8))
        pyautogui.typewrite(email, interval = 0.1)
        
        phone=line[3]
        pyautogui.click(pyautogui.locateCenterOnScreen('img\\telefone.png', confidence=0.8))
        pyautogui.typewrite(phone, interval = 0.1) 
        
        sexo=line[1]        
        pyautogui.click(pyautogui.locateCenterOnScreen('img\\sexo.png', confidence=0.8))
        
        if sexo == 'Feminino':
            pyautogui.click(pyautogui.locateCenterOnScreen('img\\feminino.png', confidence=0.8))
        else:
            pyautogui.click(pyautogui.locateCenterOnScreen('img\\masculino.png', confidence=0.8))
        
        
        pyautogui.screenshot(f"img\\cadastro_{name}.png")   
        time.sleep(3)
        
        
        pyautogui.click(pyautogui.locateCenterOnScreen('img\\botao_enviar.png', confidence=0.8))        
        
        
pyautogui.alert(text = 'Cadastro finalizado com sucesso', title = 'Aviso do sistema', button = 'OK')

        
        
        