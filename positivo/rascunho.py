import pyautogui

tamanho = 1

local = r'c:\\Users\\Marcos\\Desktop\\pw\\image\\'
amor = '800x600'

local2 = local + str(amor)+r'\pw.png'
print(local2)
print(type(local))

img = pyautogui.locateOnScreen(r'image\800x600\pw.png', confidence=0.9)
img2 = pyautogui.locateOnScreen(local2, confidence=0.9)

print(img)
print(img2)