import tkinter as tk
import pyautogui
import utils.function as f
import keyboard



def nome(msg):
    if (chkAtq.get()):
        chkAtq.set(False)
        print(msg)
    else:
        chkAtq.set(True)
        print(chkAtq.get())
    

def main():
    if chkDef.get() == False and chkAtq.get() == False:
        pyautogui.alert('Selecione um dos atributos.\n','I.A do John', 'OK')
        return 0
    if chkAtq.get() == True:
        QuantAtq = int(pyautogui.password(text='Digite a quantidade de nivel de Ataque que vc deseja:\n', title='I.A do John', mask=None))
         
    if chkDef.get() == True:
        QuantDef = int(pyautogui.password(text='Digite a quantidade de nivel de Defesa que vc deseja:\n', title='I.A do John', mask=None))


    f.ShowWindow('www.pwrevolution.com.br')
    pyautogui.sleep(0.5)
    BotaoGravar = f.LocateButtonGravar()
    slot = 0
    #Pega localizações dos Aneis
    LocateAnel1 = list(pyautogui.locateAllOnScreen(r'image\anel.png', confidence=0.8))
    LocateAnel2 = list(pyautogui.locateAllOnScreen(r'image\anel2.png', confidence=0.8))
    LocateAnel3 = list(pyautogui.locateAllOnScreen(r'image\anel3.png', confidence=0.8))
    #Pega localizações dos ornamentos
    LocateColar1 = list(pyautogui.locateAllOnScreen(r'image\colar.png', confidence=0.8))
    LocateColar2 = list(pyautogui.locateAllOnScreen(r'image\colar2.png', confidence=0.8))
    LocateOrnamento = list(pyautogui.locateAllOnScreen(r'image\ornamento.png', confidence=0.8))
    LocateOrnamento2 = list(pyautogui.locateAllOnScreen(r'image\ornamento2.png', confidence=0.8))

    LocateAnel = LocateAnel1 + LocateAnel2 + LocateAnel3
    LocateOrnamento = LocateColar1 + LocateColar2 + LocateOrnamento + LocateOrnamento2
    LocateAcessorios = LocateAnel + LocateOrnamento

    TotalAcessorios = len(LocateAcessorios)

    quit = 1

    while(quit):    
        quit = not(keyboard.is_pressed('q'))
        pyautogui.rightClick(LocateAcessorios[slot][0]+15,LocateAcessorios[slot][1]+15) #clica no primeiro slot do inventario
        pyautogui.click(BotaoGravar)
        pyautogui.moveTo(LocateAcessorios[slot][0]+15,LocateAcessorios[slot][1]+15)
        pyautogui.sleep(1.5)
        
        Defesa = list(pyautogui.locateAllOnScreen(r'image\Ndef.png', confidence=0.9))
        Ataque = list(pyautogui.locateAllOnScreen(r'image\Natq.png', confidence=0.9))

        print('Def: ' + str(len(Defesa)))
        print('Atq: ' + str(len(Ataque)))


        if chkDef.get() == True:
            # pyautogui.alert('Conseguimos um anel com '+ str(len(Defesa)) +' add de DEFESA.\n','I.A do John', 'OK')
            # exit()
            if len(Defesa)  >= QuantDef:
                slot+=1

        if chkAtq.get() == True:
            # pyautogui.alert('Conseguimos um anel com '+ str(len(Ataque)) +' add de ATAQUE.\n','I.A do John', 'OK')
            # exit()
            if len(Ataque) >= QuantAtq:
                slot+=1
        
        if slot >= TotalAcessorios:
            pyautogui.alert('Terminei os '+str(TotalAcessorios)+' aneis\n','I.A do John', 'OK')
            exit()
    
    if quit == 0:
        f.ShowWindow('I.A do John')
    

menu = tk.Tk()
menu.title('I.A do John')

#Impede que a janela deja redimenssionada
menu.resizable(True,True)

#resolução da tela
largura = menu.winfo_screenwidth()
altura = menu.winfo_screenheight()

posx = (largura /2)  - (500/2)
posy = (altura/2) - (350/2)

#Tamanho da janela e posição que inicia
menu.geometry('%dx%d+%d+%d' % (500, 350, posx, posy))


menu.iconbitmap("image/pw2.ico")

chkAtq = tk.BooleanVar() 
#chkAtq.set(False)
chkDef = tk.BooleanVar() 

tk.Checkbutton(menu, text='Nivel de Ataque', var=chkAtq).grid(column=0, row=0, sticky=tk.W+tk.N)
tk.Checkbutton(menu, text='Nivel de Defesa', var=chkDef).grid(column=1, row=0, sticky=tk.W+tk.S)

logo = tk.PhotoImage(file=r'image\anel.png')
labelLogo = tk.Label(menu, image=logo)
labelLogo.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

tk.Button(menu, text="Iniciar", command= lambda: main()).grid(column=0, row=1)
tk.Button(menu, text="Trocar", command= lambda: nome('oi')).grid(column=1, row=2)


tk.Button(menu, text='Sair', command=menu.quit).grid(column=0, row=2)

menu.mainloop()

