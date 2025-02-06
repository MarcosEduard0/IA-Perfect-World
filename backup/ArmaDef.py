import pytesseract as ocr
import PIL
import time
import pyautogui #Biblioteca automação
import ctypes  #Janela de aviso
import os
import re
import utils.function as f
from string import punctuation

tesseract = r'Tesseract-OCR\tesseract.exe'
ocr.pytesseract.tesseract_cmd=tesseract

def main(): 
    
    while True:
        Quant = int(input("Quantos adds de Nivel de def vc quer?\n"))
        if Quant < 1 or Quant > 5:
            print('\nPor favor digite um valor entre 1 e 4.\n\n')
        else:
            break
    
    QuantRolete = input("Quantas Escultura da Reforja você possui?\n")

    rolete = int((int(QuantRolete)-30)/3)
    finalizador = 0

    f.ShowWindow() #Abre a Janela do pw

    BotaoReproduzir = f.LocateButton() #Localiza as coordenadas X e Y do botao reproduzir

    AreaAdds_X, AreaAdds_Y = {}, {}
    AreaAdds_X2, AreaAdds_Y2 = {}, {}

    AreaAdds_X[0], AreaAdds_X[1] = int(BotaoReproduzir[0]+105), int(BotaoReproduzir[0]+180) #calcula a area do adds
    AreaAdds_Y[0], AreaAdds_Y[1] = int(BotaoReproduzir[1]-170), int(BotaoReproduzir[1]-55)

    AreaAdds_X2[0], AreaAdds_X2[1] = int(BotaoReproduzir[0]+65), int(BotaoReproduzir[0]+135) #calcula a area do adds
    AreaAdds_Y2[0], AreaAdds_Y2[1] = int(BotaoReproduzir[1]-170), int(BotaoReproduzir[1]-55)

    while(finalizador <= rolete):
        finalizador+=1

        pyautogui.click(BotaoReproduzir[0],BotaoReproduzir[1]) #CLica no botao Reproduzir
        time.sleep(1) #Espera 1.5 segundos para forjar o item

        imagem = pyautogui.screenshot(r'image\screenShot.bmp')
        area = (AreaAdds_X[0], AreaAdds_Y[0], AreaAdds_X[1], AreaAdds_Y[1]) #Defino o tamanho e o local da area a ser corada na imagem
        cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
        #cropped_img.show() #Mostra a imagem cortada
        img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
        #img_op.show()
        txt_adds = ocr.image_to_string(img_op) #Extrai o texto da imagem e coloca na variavel
        #print(txt_adds)
        
        adds = re.split(r'[^0-9A-Za-z]+',txt_adds) #Separa os palavras em lista
        #print(adds)
        
        TotalNumDef = adds.count("Defesa")
        TotalNumAtq = adds.count("Ataque")
        print('Defesa: ' + str(TotalNumDef))
        print('Ataque: ' + str(TotalNumAtq))



        area = (AreaAdds_X2[0], AreaAdds_Y2[0], AreaAdds_X2[1], AreaAdds_Y2[1]) #Defino o tamanho e o local da area a ser corada na imagem
        cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
        #cropped_img.show() #Mostra a imagem cortada
        img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
        txt_adds = ocr.image_to_string(img_op) #Extrai o texto da imagem e coloca na variavel
        
        adds = re.split(r'[^0-9A-Za-z]+',txt_adds) #Separa os palavras em lista
        #print(adds)
        
        TotalCast = adds.count("Tempo")
        print('Tempo: ' + str(TotalCast))
        print('-------------------x------------------------\n')


        if TotalCast >= Quant:
            pyautogui.click(BotaoReproduzir[0]+155,BotaoReproduzir[1]-15) #CLica em segurar o novo add
            pyautogui.alert('Parabéns, conseguimos uma arma com '+ str(TotalCast) +' add de invocação','I.A do John','Obrigado')
            os.remove(r'image\screenShot.bmp')
            exit() #fecha o programa

        else:
            pyautogui.click(BotaoReproduzir[0]-170,BotaoReproduzir[1]-15) #Clica em manter o antigo add
            time.sleep(1.5)

if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main