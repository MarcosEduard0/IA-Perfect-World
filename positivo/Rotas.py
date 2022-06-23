import pyautogui
import function as f
import keyboard
import pytesseract as ocr

# tesseract = r'Tesseract-OCR\tesseract.exe'
# ocr.pytesseract.tesseract_cmd=tesseract

ocr.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


f.ShowWindow("Perfect World: Oasis - Rate Baixa")
pyautogui.sleep(1)


mineiroFerro = pyautogui.locateCenterOnScreen(r'image\1920x1080\mineiroFerro.png', confidence=0.8)
pyautogui.moveTo(mineiroFerro)
pyautogui.sleep(1)
pyautogui.leftClick(mineiroFerro[0], mineiroFerro[1]+40)
    
