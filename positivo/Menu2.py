import tkinter as tk


def cmd_Click(msg):
    print(msg)

def teste():
    if chkValue.get() == True:
        print ('selecionado')

def main():
    

menu = tk.Tk()
menu.title('Primeiro app')

#Impede que a janela deja redimenssionada
menu.resizable(True,True)

#resolução da tela
largura = menu.winfo_screenwidth()
altura = menu.winfo_screenheight()

posx = largura /2  - 500/2
posy = altura/2 - 350/2

#Tamanho da janela e posição que inicia
menu.geometry("%dx%d+%d+%d" % (500, 350, posx, posy))

menu.iconbitmap("image/pw2.ico")

chkValue = tk.BooleanVar() 
chkValue.set(False)

tk.Checkbutton(menu, text='Check Box', var=chkValue).grid(column=0, row=0)

tk.Button(menu, text='mostrar', command= lambda: teste()).grid(column=0, row=1)
tk.Button(menu, text="Printar no cmd", command= lambda: cmd_Click("Oque eu quiser")).grid(column=0, row=2)


tk.Button(menu, text='Sair', command=menu.quit).grid(column=0, row=3)


menu.mainloop()


def 