import pytesseract as ocr
import PIL
import time
import pyautogui #Biblioteca automação
import ctypes  #Janela de aviso
import re
from string import punctuation
import utils.function as f
ocr.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


f.ShowWindow()
pyautogui.sleep(1)


while(True): #Localiza o npc dentro na nirvana
    PinkBall = pyautogui.locateCenterOnScreen(r'image\npcRosa.png', confidence=0.9)

    if(PinkBall == None):
        OrangeBall = pyautogui.locateCenterOnScreen(r'image\npcLaranja.png', confidence=0.9)

        if OrangeBall == None:
            print('nao achei laranja')
            fechar = pyautogui.locateCenterOnScreen(r'image\fechar.png', confidence=0.9)
            pyautogui.click(fechar[0],fechar[1])
            pyautogui.press('esc')
            exit()
        else:
            pyautogui.moveTo(OrangeBall[0],OrangeBall[1])
            pyautogui.sleep(1)
            pyautogui.click(OrangeBall[0],OrangeBall[1])
            break
    
    else:
        pyautogui.moveTo(PinkBall[0],PinkBall[1])
        pyautogui.sleep(1)
        pyautogui.click(PinkBall[0],PinkBall[1])
        break
    
pyautogui.sleep(10)

while(True):
    entregarQuest = pyautogui.locateCenterOnScreen(r'image\entregar.png', confidence=0.8)

    if(entregarQuest == None):
        PegarQuest = pyautogui.locateCenterOnScreen(r'image\quest.png', confidence=0.8)

        if PegarQuest == None:
            print('não achei npc quest')
            pyautogui.press('esc')
            exit()
        else:            
            while(True):
            
                pyautogui.moveTo(PegarQuest[0],PegarQuest[1]+70)
                pyautogui.sleep(1)

                JanelaQuest = pyautogui.locateCenterOnScreen(r'image\npcQuest.png', confidence=0.8)

                if JanelaQuest == None:
                    pass
                else:
                    exit()
    else:
        entrega = 0
        while(True):
            pyautogui.moveTo(entregarQuest[0],entregarQuest[1]+70)
            pyautogui.sleep(1)

            JanelaQuest = pyautogui.locateCenterOnScreen(r'image\npcQuest.png', confidence=0.8)

            if JanelaQuest == None:
                pass
            else:
                entrega+=1
                pyautogui.sleep(6)
            
            if entrega >=2:
                exit()
        