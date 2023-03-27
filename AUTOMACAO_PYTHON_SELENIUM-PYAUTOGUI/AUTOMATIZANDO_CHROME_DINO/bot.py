from PIL import ImageGrab
import pyautogui
import time

print('################ Iniciando o game ################')

def isCollision(data):
    
    for i in range(450,540):
        for j in range(300,336):                        
            if data[i,j] < 100:
                print('Pulou') 
                pyautogui.keyDown('up')   
                return              
    return
      

        
while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    isCollision(data)
        
    """for i in range(450,490):
        for j in range(290,330):
            data[i,j] = 0
            #print(data[i,j])
    time.sleep(3)"""
    """image.show()
    break"""