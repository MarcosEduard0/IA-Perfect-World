import pyautogui
import function as f


f.ShowWindow() #Abre a Janela do pw

while(True):

    pyautogui.click(356, 969) #CLica no botao Reproduzir
    pyautogui.moveTo(286, 972)
    pyautogui.sleep(0.5)
    Penetracao = list(pyautogui.locateAllOnScreen(r'image\PenetMagica.png', confidence=0.9))
    if Penetracao == None:
        Penetracao = list(pyautogui.locateAllOnScreen(r'image\PenetMagica2.png', confidence=0.9))

    AtqM = list(pyautogui.locateAllOnScreen(r'image\atqM.png', confidence=0.9))

    Espirito = list(pyautogui.locateAllOnScreen(r'image\espirito.png', confidence=0.9))

    Def = list(pyautogui.locateAllOnScreen(r'image\def.png', confidence=0.9))

    hp = list(pyautogui.locateAllOnScreen(r'image\hp.png', confidence=0.9))

    print('Espirito: ' + str(len(Espirito)) + ' Penetracao: ' + str(len(Penetracao))+ ' AtaM: ' + str(len(AtqM)))
    
    if len(Penetracao) == len(Espirito) == len(AtqM) == 2:
        pyautogui.alert('Conseguimos um astro 2 2 2.\n','I.A do John', 'OK')
        exit()
        
