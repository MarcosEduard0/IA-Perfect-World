import pytesseract as ocr
import PIL
import time
import pyautogui #Biblioteca automação
import re
import os
import function as f
from string import punctuation

tesseract = r'Tesseract-OCR\tesseract.exe'
ocr.pytesseract.tesseract_cmd=tesseract

def main(): 
    
    while True:
        Quant = int(pyautogui.password(text='Quantos adds de def % você quer?\n', title='I.A do John', mask=None))
        #Quant = int(input("Quantos adds de def % vc quer?\n"))
        if Quant < 1 or Quant > 4:
            pyautogui.alert('Por favor digite um valor entre 1 e 4.\n','I.A do John','OK')
            #print('\nPor favor digite um valor entre 1 e 4.\n\n')
        else:
            break
    
    QuantRolete = int(pyautogui.password(text='Quantas Escultura da Reforja você possui?\n', title='I.A do John', mask=None))

    rolete = int(QuantRolete)/2
    finalizador = 0

    f.ShowWindow() #Abre a Janela do pw

    BotaoReproduzir = f.LocateButton() #Localiza as coordenadas X e Y do botao reproduzir

    AreaAdds_X, AreaAdds_Y = {}, {}

    AreaAdds_X[0], AreaAdds_X[1] = int(BotaoReproduzir[0]+65), int(BotaoReproduzir[0]+180) #calcula a area do adds
    AreaAdds_Y[0], AreaAdds_Y[1] = int(BotaoReproduzir[1]-170), int(BotaoReproduzir[1]-55)

    while(finalizador <= rolete):

        pyautogui.click(BotaoReproduzir[0],BotaoReproduzir[1]) #CLica no botao Reproduzir
        time.sleep(1.5) #Espera 1.5 segundos para forjar o item

        imagem = pyautogui.screenshot(r'image\screenShot.bmp')
        area = (AreaAdds_X[0], AreaAdds_Y[0], AreaAdds_X[1], AreaAdds_Y[1]) #Defino o tamanho e o local da area a ser corada na imagem
        cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
        #cropped_img.show() #Mostra a imagem cortada
        
        img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
        #img_op.show()
        txt_adds = ocr.image_to_string(img_op) #Extrai o texto da imagem e coloca na variavel
        #print(txt_adds)
        
        adds = re.split(r'[^0-9A-Za-z]+',txt_adds) #Separa os palavras em lista
        print(adds)

        TotalNum = adds.count("Dano")
        print('total: ', TotalNum)

        if TotalNum >= Quant:
            pyautogui.click(BotaoReproduzir[0]+155,BotaoReproduzir[1]-15) #CLica em segurar o novo add
            pyautogui.alert('Parabéns, conseguimos uma parte do set com '+ str(TotalNum) +' redução de dano ','I.A do John','OK')
            os.remove(r'image\screenShot.bmp')
            exit() #fecha o programa
        else:
            pyautogui.click(BotaoReproduzir[0]-170,BotaoReproduzir[1]-15) #Clica em manter o antigo add
            time.sleep(1.5)

if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main