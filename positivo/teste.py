import pyautogui
import function as f


f.ShowWindow("Perfect World: Oasis - Rate Baixa")
pyautogui.sleep(1)

while(True):

    cordBotao = f.LocateButtonAvatar()
    cordBotaoGrav = f.LocateButtonGravar()

    pyautogui.rightClick(cordBotao[0]-275,cordBotao[1]+30)
    pyautogui.click(cordBotaoGrav)
    pyautogui.moveTo(cordBotao[0]-275,cordBotao[1]+30)
    pyautogui.sleep(1.5)

    Defesa = list(pyautogui.locateAllOnScreen(r'image\Ndef.png', confidence=0.9))
    Ataque = list(pyautogui.locateAllOnScreen(r'image\Natq.png', confidence=0.9))

    print('Def: ' + str(len(Defesa)))
    print('Atq: ' + str(len(Ataque)))

    # if len(inteligencia) >= 1:
    #     pyautogui.alert('Conseguimos um anel com '+ str(len(inteligencia)) +'  add de INTELIGENCIA.\n','I.A do John', 'OK')
    #     exit()

    if len(Defesa)  > 0:
        pyautogui.alert('Conseguimos um anel com '+ str(len(Defesa)) +' add de DEFESA.\n','I.A do John', 'OK')
        exit()

    if len(Ataque) > 2:
        pyautogui.alert('Conseguimos um anel com '+ str(len(Ataque)) +' add de ATAQUE.\n','I.A do John', 'OK')
        exit()