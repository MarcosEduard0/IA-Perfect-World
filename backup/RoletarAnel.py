import pyautogui
import utils.function as f
import keyboard
import pytesseract as ocr

tesseract = r'Tesseract-OCR\tesseract.exe'
ocr.pytesseract.tesseract_cmd=tesseract

while True:
    optionAcc = int(pyautogui.password(text='Digite para qual acessório vc deseja pegar o atributo:\n\n1- Aneis\n2- Colares\n3- Ornamentos\n', title='I.A do John', mask=None))
    if optionAcc < 4 and optionAcc > 0:
        break
while True:
    option = int(pyautogui.password(text='Digite qual atributo deseja pegar:\n\n1- Nível de Ataque\n2- Nível de Defesa\n3- Ambos\n', title='I.A do John', mask=None))
    if option < 4 and option > 0:
        break
if option == 1 or option == 3:
    while True:
        QuantAtq = int(pyautogui.password(text='Digite a quantidade de atribiutos de nivel de Ataque \nque vc deseja:\n', title='I.A do John', mask=None))
        if QuantAtq < 3 and QuantAtq > 0:
            break
if option == 2 or option == 3:     
    while True:
        QuantDef = int(pyautogui.password(text='Digite a quantidade de atribiutos de nivel de Defesa \nque vc deseja:\n', title='I.A do John', mask=None))
        if QuantDef < 3 and QuantDef > 0:
            break

f.ShowWindow("Perfect World: Oasis - Rate Baixa")
pyautogui.sleep(1)
BotaoGravar = f.LocateButtonGravar()
slot = 0

if optionAcc == 1:
    LocateAnel3 = list(pyautogui.locateAllOnScreen(r'image\anel3.png', confidence=0.8))
    LocateAnel2 = list(pyautogui.locateAllOnScreen(r'image\anel2.png', confidence=0.8))
    LocateAnel1 = list(pyautogui.locateAllOnScreen(r'image\anel.png', confidence=0.8))
    if LocateAnel3 == [] and LocateAnel2 == [] and LocateAnel1 == []:
        pyautogui.alert('Erro ao localizar os aneis.\n','I.A do John', 'OK')
        exit()
    else:
        LocateAcessorios = LocateAnel1 + LocateAnel2 + LocateAnel3

if optionAcc == 2:
    LocateColar1 = list(pyautogui.locateAllOnScreen(r'image\colar.png', confidence=0.8))
    LocateColar2 = list(pyautogui.locateAllOnScreen(r'image\colar2.png', confidence=0.8))   
    if LocateColar1 == [] and LocateColar2 == []:
            pyautogui.alert('Erro ao localizar os colares.\n','I.A do John', 'OK')
            exit()
    else:
        LocateAcessorios = LocateColar1 + LocateColar2

if optionAcc == 3:
    LocateOrnamento = list(pyautogui.locateAllOnScreen(r'image\ornamento.png', confidence=0.8))
    LocateOrnamento2 = list(pyautogui.locateAllOnScreen(r'image\ornamento2.png', confidence=0.8))
    if LocateOrnamento == [] and LocateOrnamento2 == []:
            pyautogui.alert('Erro ao localizar os ornamentos.\n','I.A do John', 'OK')
            exit()
    else:
        LocateAcessorios =  LocateOrnamento + LocateOrnamento2

TotalAcessorios = len(LocateAcessorios)

while(True):    

    pyautogui.rightClick(LocateAcessorios[slot][0]+15,LocateAcessorios[slot][1]+15) #clica no primeiro slot do inventario
    pyautogui.click(BotaoGravar)
    pyautogui.moveTo(LocateAcessorios[slot][0]+15,LocateAcessorios[slot][1]+15)
    pyautogui.sleep(1.5)
    
    Defesa = list(pyautogui.locateAllOnScreen(r'image\Ndef.png', confidence=0.9))
    Ataque = list(pyautogui.locateAllOnScreen(r'image\Natq.png', confidence=0.9))

    print('Def: ' + str(len(Defesa)))
    print('Atq: ' + str(len(Ataque)))

    if option == 2 or option == 3:
        # pyautogui.alert('Conseguimos um anel com '+ str(len(Defesa)) +' add de DEFESA.\n','I.A do John', 'OK')
        # exit()
        if len(Defesa)  >= QuantDef:
            slot+=1

    if option == 1 or option == 3:
        # pyautogui.alert('Conseguimos um anel com '+ str(len(Ataque)) +' add de ATAQUE.\n','I.A do John', 'OK')
        # exit()
        if len(Ataque) >= QuantAtq:
            slot+=1
    
    if slot > TotalAcessorios:
        pyautogui.alert('Terminei os '+str(TotalAcessorios)+' aneis\n','I.A do John', 'OK')
        exit()
