import pytesseract as ocr
from PIL import ImageOps, Image
import time
import pyautogui
import winsound  # Importa o módulo para emitir sons
import os
from string import punctuation
import sys
import re

utils_path = os.path.abspath("../")
if utils_path not in sys.path:
    sys.path.append(utils_path)


import utils.function as f


tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ocr.pytesseract.tesseract_cmd=tesseract

def change_red_to_green_rgb(img):
    # Convert image to RGB
    img = img.convert("RGB")
    data = img.getdata()

    new_data = []
    for item in data:
        # Change all pixels that are significantly red to green
        if item[0] > 150 and item[1] < 100 and item[2] < 100:
            # Change red to green
            new_data.append((245, 210, 78))  # amarelo
        else:
            new_data.append(item)

    img.putdata(new_data)
    return img

f.ShowWindow('Perfect World') #Abre a Janela do pw


botao_purificar = f.LocateButton(r'../image/1920x1080/purificacao.png') #Localiza as coordenadas X e Y do botao reproduzir

while(True):

   
    pyautogui.click(botao_purificar[0],botao_purificar[1])
    time.sleep(1.3) #Espera 1.5 segundos para forjar o item

    AreaAdds_X, AreaAdds_Y = {}, {}

    AreaAdds_X[0], AreaAdds_X[1] = int(botao_purificar[0]), int(botao_purificar[0]+190) 
    AreaAdds_Y[0], AreaAdds_Y[1] = int(botao_purificar[1]-265), int(botao_purificar[1]-113)

    imagem = pyautogui.screenshot(r'..\image\screenShot.bmp')
    area = (AreaAdds_X[0], AreaAdds_Y[0], AreaAdds_X[1], AreaAdds_Y[1]) #Defino o tamanho e o local da area a ser corada na imagem
    cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
    # cropped_img.show() #Mostra a imagem cortada

    cropped_img = change_red_to_green_rgb(cropped_img)

    gray_img = cropped_img.convert('L')

    img_op = ImageOps.invert(gray_img) #Inverte as cores para facilitar a leitura dos adds
    # img_op.show()

    txt_adds = ocr.image_to_string(cropped_img) #Extrai o texto da imagem e coloca na variavel

    for add in txt_adds.split('\n'):
        if 'Defesa' in add or 'Defeca' in add:
            print(txt_adds)
            if add.split()[-1].isdigit():
                quant_def = int(add.split()[-1])
                if quant_def > 11 and quant_def != 411 and quant_def != 41:
                    # pyautogui.click(botao_purificar[0]+50,botao_purificar[1])
                    winsound.Beep(2000, 1000)  # Frequência de 1000 Hz por 500 milissegundos
                    pyautogui.alert('Parabéns, conseguimos DEFESA','I.A do John','OK')
                    os.remove(r'image\screenShot.bmp')
                    exit() #fecha o programa

        # if add.startswith('HP '):
        #     print(txt_adds)
        #     if add.split()[-1].isdigit():
        #         valor_numerico = add.split()[-1] if len(add.split()[-1]) == 3 else add.split()[-1][1:]
        #         valor_numerico = int(valor_numerico)
        #         if valor_numerico > 500 :
        #             pyautogui.click(botao_purificar[0]+50,botao_purificar[1])
        #             winsound.Beep(2000, 1000)  # Frequência de 1000 Hz por 500 milissegundos
        #             pyautogui.alert('Parabéns, conseguimos HP','I.A do John','OK')
        #             os.remove(r'image\screenShot.bmp')
        #             exit() #fecha o programa

        # if 'Tempo' in add :
        #     print(txt_adds)
        #     add = add.replace('#%', '8%')
        #     add = add.replace('£%', '8%')
            
        #     numeros = re.search(r'\d+', add).group()
        #     try:
        #         valor_numerico = abs(int(numeros))
        #     except:
        #         print(f"ERRRO: {add}")
        #         exit() #fecha o programa


        #     if valor_numerico > 10 :
        #         pyautogui.click(botao_purificar[0]+50,botao_purificar[1])
        #         winsound.Beep(2000, 1000)  # Frequência de 1000 Hz por 500 milissegundos
        #         pyautogui.alert('Parabéns, conseguimos TEMPO','I.A do John','OK')
        #         os.remove(r'image\screenShot.bmp')
        #         exit() #fecha o programa

        # if add.startswith('Def '):
        #     print(txt_adds)
        #     numeros = re.search(r'\d+', add).group()
        #     try:
        #         valor_numerico = abs(int(numeros))
        #     except:
        #         print(f"ERRRO: {add}")
        #         exit() #fecha o programa


        #     if valor_numerico > 700 :
        #         pyautogui.click(botao_purificar[0]+50,botao_purificar[1])
        #         winsound.Beep(2000, 1000)  # Frequência de 1000 Hz por 500 milissegundos
        #         pyautogui.alert('Parabéns, conseguimos TEMPO','I.A do John','OK')
        #         os.remove(r'image\screenShot.bmp')
        #         exit() #fecha o programa
 

    pyautogui.click(botao_purificar[0]-50,botao_purificar[1]) #Clica em manter o antigo add


