import pyautogui #Biblioteca automação
import win32gui, win32con
import time
import datetime

#Centro do Botao Produzir = 255,360

def ShowWindow(nome):
    hwnd = win32gui.FindWindow(None, nome)
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    time.sleep(1)

def LocateButton():

    BotaoReproduzir = pyautogui.locateCenterOnScreen(r'image\botaoReproduzirOn.png', confidence=0.9)

    if(BotaoReproduzir == None):
        BotaoReproduzir = pyautogui.locateCenterOnScreen(r'image\botaoReproduzirOff.png', confidence=0.9)
        if(BotaoReproduzir == None):
            pyautogui.alert('Erro ao localizar o botão reproduzir, verifique se você abriu a janela de Reprodução de Equipamento.\n'
                            'Se você ja esta com a janela aberta, coloque a câmera do personagem em uma posição mais limpa (ex. olhando para o Céu),'
                            ' ou a janela em outra coordenada.\n','I.A do John', 'OK')
            input("Presione Enter para fechar....")
            exit()

    return BotaoReproduzir

def LocateButtonAvatar():

    BotaoAvatar = pyautogui.locateCenterOnScreen(r'image\botaoAvatar.png', confidence=0.8)
    if(BotaoAvatar == None):
        pyautogui.alert('Erro ao localizar o botão de avatares.\n','I.A do John', 'OK')
        exit()

    return BotaoAvatar

def LocateButtonGravar():

    BotaoGravar = pyautogui.locateCenterOnScreen(r'image\botaoGravar.png', confidence=0.8)
    if(BotaoGravar == None):
        BotaoGravar = pyautogui.locateCenterOnScreen(r'image\botaoGravar1.png', confidence=0.8)
        if(BotaoGravar == None):
            pyautogui.alert('Erro ao localizar o botão de gravura.\n','I.A do John', 'OK')
            exit()

    return BotaoGravar

def LocateTaskBarPw():

    pw = pyautogui.locateCenterOnScreen(r'image\pw.png', confidence=0.9)

    if(pw == None):
        pyautogui.alert('Erro ao localizar o Perfect World na barra de tarefas.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()
            
    return pw

def LocateWindowPw():

    window = list(pyautogui.locateAllOnScreen(r'image\pw2.png', confidence=0.9))
    if(window == None):
        pyautogui.alert('Erro ao localizar as janelas do Perfect World.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()

    return window

def LocateOptionVender():

    OptionVender = pyautogui.locateCenterOnScreen(r'image\vender.png', confidence=0.9)

    if(OptionVender == None):
        pyautogui.alert('Erro ao localizar a opção Vender.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()
            
    return OptionVender

def LocateCupom():

    cupom = pyautogui.locateCenterOnScreen(r'image\cupom.png', confidence=0.9)

    if(cupom == None):
        pyautogui.alert('Erro ao localizar os cupons no seu inventário.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()
            
    return cupom

def LocateCoin():

    coin = pyautogui.locateCenterOnScreen(r'image\coin.png', confidence=0.9)

    if(coin == None):
        pyautogui.alert('Erro ao localizar derrubar moedas no seu inventário.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()
            
    return coin

def LocateButtonMax():

    buttonMax = pyautogui.locateCenterOnScreen(r'image\botaoMax.png', confidence=0.9)

    if(buttonMax == None):
        pyautogui.alert('Erro ao localizar o botão "Máximo" no soltar moedas.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()
            
    return buttonMax

def LocateButtonOk():

    buttonOk = pyautogui.locateCenterOnScreen(r'image\botaoOk.png', confidence=0.9)

    if(buttonOk == None):
        pyautogui.alert('Erro ao localizar o botão "Máximo" no soltar moedas.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()
            
    return buttonOk

def LocateFechar():

    fechar = pyautogui.locateCenterOnScreen(r'image\fechar.png', confidence=0.9)

    if(fechar == None):
        pyautogui.alert('Erro ao localizar o botão "fechar" no inventário.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()
            
    return fechar

def LocatePegar():

    pegar = pyautogui.locateCenterOnScreen(r'image\pegar.png', confidence=0.9)

    if(pegar == None):
        pegar = pyautogui.locateCenterOnScreen(r'image\ganancia.png', confidence=0.9)
        if pegar == None:
            pyautogui.alert('Erro ao localizar o botão "Pegar itens e Ganância" na barra. Verifique se lembrou de coloca-las\n','I.A do John', 'OK')
            input("Presione Enter para fechar....")
            exit()
    return pegar

def LocateButtonVender():

    button = pyautogui.locateCenterOnScreen(r'image\botaoVender.png', confidence=0.9)

    if(button == None):
        button = pyautogui.locateCenterOnScreen(r'image\botaoVender.png', confidence=0.9)
        if button == None:
            pyautogui.alert('Erro ao localizar o botão Vender.\n','I.A do John', 'OK')
            input("Presione Enter para fechar....")
            exit()
    return button

def LocateButtonReforja():

    button = pyautogui.locateCenterOnScreen(r'image\botaoReforja.png', confidence=0.9)

    if(button == None):
        button = pyautogui.locateCenterOnScreen(r'image\botaoReforja.png', confidence=0.9)
        if button == None:
            pyautogui.alert('Erro ao localizar o botão Reforja.\n','I.A do John', 'OK')
            input("Presione Enter para fechar....")
            exit()
            
    return button

def LocateSetPosition():

    posicao = pyautogui.locateCenterOnScreen(r'image\SlotPosition.png', confidence=0.9)

    if(posicao == None):
        pyautogui.alert('Erro ao localizar a posição do equipamento.\n','I.A do John', 'OK')
        input("Presione Enter para fechar....")
        exit()
            
    return posicao

def LocateAddPosition():

    posicao = list(pyautogui.locateAllOnScreen(r'image\LocateAdd.png', confidence=0.9))

    if(posicao == []):
        posicao = list(pyautogui.locateAllOnScreen(r'image\LocateAdd2.png', confidence=0.9))
        if(posicao == []):
            pyautogui.alert('Erro ao localizar a posição dos atributos do set.\n','I.A do John', 'OK')
            input("Presione Enter para fechar....")
            exit()
        else:
            return posicao
    else:
        return posicao

def TempoGasto(SegTotal):
    hora = int(SegTotal /3600)
    minutos = int((SegTotal-hora*3600)/60)
    segundos = int(SegTotal-hora*3600-minutos*60)
    
    return datetime.time(hora, minutos, segundos)

def HorarioAtual():
    now = datetime.datetime.now()
    horario = datetime.time(now.hour, now.minute, now.second)

    return horario