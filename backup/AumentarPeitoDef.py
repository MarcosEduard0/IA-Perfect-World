import pytesseract as ocr
import PIL
import time
import pyautogui #Biblioteca automação
import ctypes  #Janela de aviso
import re
import os
from string import punctuation
import utils.function as f
ocr.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pyautogui.alert(text='Antes de começar, você precisa seguir algumas regras.\n\n'+
                        '1. Você so pode estar com dois Perfect World abertos, o que vai ficar roletando e o que vai ficar mandando moedas.\n\n'+
                        '2. A primeira janela do perfect world deverá ser a conta que ficará roletando, e a segunda janela deverá ser a conta das moedas.\n\n'+
                        '3. A conta de moedas deverá esta com o inventário zerado, ou seja, sem moedas, somente com cupom perfeito.\n\n'+
                        '4. A conta de moedas deverá esta com a opção de "Slots Extras" do inventário ativado.\n\n'+
                        '5. Para melhor reconhecimento do adds, a conta de reforja, deverá esta com a câmera apontada '+
                        'para um paisagem mais limpa (ex. Céu)\n\n'+
                        '6. A conta de moedas deverá esta com a câmera em primeira pessoa, e olhando de frente para o NPC, de modo que o NPC fique no CENTRO da sua tela. isso é crucial.\n\n'+
                        '7. Não esqueça de deixar a ação de catar itens na barra de habilidades e que esteja VISÍVEL.\n\n', title='I.A do John', button='Já preparei tudo, pode continuar.')



def main():
    cupons = int(pyautogui.password(text='Digite a quantidade de Cupons Perfeitos que você possui:\n', title='I.A do John', mask=None))

    moeda = int(pyautogui.password(text='Digite a quantidade de moeda que você possui:\n', title='I.A do John', mask=None))

    QuantRolete = int(pyautogui.password(text='Digite a quantidade de reliquia que você possui:\n', title='I.A do John', mask=None))

    ValorRolete = 1500000
    QuantVezes = int(int(moeda)/ValorRolete)
    CorrectCoin = QuantVezes * ValorRolete

    TotalDrop = moeda - CorrectCoin
    TotalRolete = int(QuantRolete/10)

    if int(moeda) % ValorRolete != 0:
        DropCoin(TotalDrop)

    f.ShowWindow()
    finalizador = 0
    contador = 0
    #parte = 1
    #total = 0
    while(finalizador <= TotalRolete): #Faça enquanto tiver reliquia no bag
        finalizador+=1
        contador+=1
        if contador > QuantVezes: #Se atingir o maximo de moedas, irar pegar mais moedas
            cupons = PegarMoeda(cupons)
            contador = 1
            QuantVezes = 1000


        pyautogui.click(139, 996) #CLica no botao Reproduzir
        time.sleep(2) #Espera 2 segundos para forjar o item
        #pyautogui.click(446,980) #CLica no botao de pegar o novo add
        pyautogui.moveTo(175, 785) #Move o mouse para cima do item
        time.sleep(1.5)
        
        imagem = pyautogui.screenshot(r'image\screenShot.bmp')
        area = (522, 485, 580, 570) #Defino o tamanho e o local da area a ser corada na imagem
        cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
        #cropped_img.show() #Mostra a imagem cortada
        
        img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
        #img_op.show()
        adds = ocr.image_to_string(img_op) # Coloca o texto na variavel adds
        #print(adds)
        
        teste = re.split(r'[^0-9A-Za-z]+',adds)
        print(teste)

        nove = adds.count("9")
        dez = adds.count("10") + adds.count("40")
        print('9%: ', nove)
        print('10%: ', dez)

        if dez >= 4:
            pyautogui.alert('Parabéns, conseguimos uma parte do set com 4 add de def','I.A do John','Obrigado')
            os.remove(r'image\screenShot.bmp')
            exit()
        if dez >=3 and nove >= 1:
            pyautogui.alert('Parabéns, conseguimos uma parte do set com 4 add de def','I.A do John','Obrigado')
            os.remove(r'image\screenShot.bmp')
            exit()




def PegarMoeda(cupons):

    if cupons < 150:
        exit()

    TaskBarPw = f.LocateTaskBarPw()
     
    npc = pyautogui.size()
      
    pyautogui.click(TaskBarPw[0],TaskBarPw[1])#clica no element
    time.sleep(1)
    WindowsPw = f.LocateWindowPw()
    pyautogui.click(WindowsPw[1][0],WindowsPw[1][1])#clica no outro pessonagem
    time.sleep(2)
    pyautogui.doubleClick(npc[0]/2,npc[1]/2) #clica no Npc
    time.sleep(2)
    optionVender = f.LocateOptionVender()
    pyautogui.click(optionVender[0],optionVender[1])#clica em vender
    time.sleep(1)
    cupom = f.LocateCupom()
    pyautogui.rightClick(cupom[0], cupom[1])#clica com direito no cupom
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.write('150')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    buttonVender = f.LocateButtonVender()
    pyautogui.click(buttonVender[0],buttonVender[1])#Clica em vender
    time.sleep(1)
    pyautogui.press('y')
    time.sleep(1)
    pyautogui.press('y')
    time.sleep(1)
    fechar = f.LocateFechar()
    pyautogui.click(fechar[0],fechar[1])#Clica em fechar
    time.sleep(1)
    pyautogui.press('b')
    time.sleep(1)
    coin = f.LocateCoin()
    pyautogui.click(coin[0], coin[1])#Clica em derrubar moeda
    time.sleep(1)
    buttonMax = f.LocateButtonMax()
    pyautogui.click(buttonMax[0], buttonMax[1])#Clica em maximo
    time.sleep(1)
    buttonOK = f.LocateButtonOk()
    pyautogui.click(buttonOK[0], buttonOK[1])#Clica em OK
    time.sleep(1)
    pegar = f.LocatePegar()
    pyautogui.doubleClick(pegar[0], pegar[1]) #clica em pegar moeda
    time.sleep(1)
    pyautogui.doubleClick(pegar[0], pegar[1]) #clica em pegar moeda
    time.sleep(1)
    pyautogui.click(coin[0], coin[1])#Clica em derrubar moeda
    time.sleep(1)
    pyautogui.click(buttonMax[0], buttonMax[1])#Clica em maximo
    time.sleep(1)
    pyautogui.click(buttonOK[0], buttonOK[1])#Clica em OK
    time.sleep(1)
    pyautogui.click(pegar[0], pegar[1]) #clica em pegar moeda
    time.sleep(1)
    pyautogui.click(pegar[0], pegar[1]) #clica em pegar moeda
    time.sleep(1)
    pyautogui.press('b')
    time.sleep(2)
    pyautogui.click(TaskBarPw[0],TaskBarPw[1])#clica no element
    time.sleep(1)
    pyautogui.click(WindowsPw[0][0],WindowsPw[0][1])#clica no outro pessonagem
    time.sleep(2)

    return cupons - 150

def DropCoin(moeda):
    PosCoin = f.LocateCoin()

    pyautogui.click(PosCoin[0], PosCoin[1])
    time.sleep(0.5)
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.write(moeda)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)



if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main