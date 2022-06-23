import tkinter as tk
import os
import shutil, errno
import base64
from tkinter import Label, StringVar, filedialog
from img import img


menu = tk.Tk()
menu.title('I.A do John')
pasta_origem = StringVar()
pasta_destino= StringVar()


# menu.iconbitmap("pw.ico")


#resolução da tela
largura = menu.winfo_screenwidth()
altura = menu.winfo_screenheight()

posx = largura /2  - 650/2
posy = altura/2 - 350/2

#Tamanho da janela e posição que inicia
menu.geometry("%dx%d+%d+%d" % (650, 220, posx, posy))

try:
    arquivo = open("tmpLayout.txt", "r")
    pasta_origem.set(arquivo.read())
    arquivo.close()
except:
    arquivo = open("tmpLayout.txt", "w")


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setIcon()
        self.create_widgets()
        self.info = tk.Label(self ,text="", fg='green')
        self.info.grid(column=1, row=0, pady=10)

    def setIcon(self):
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        menu.iconbitmap("tmp.ico")
        os.remove("tmp.ico")

    def create_widgets(self):
        self.hi_there = tk.Label(self ,text="Perfect World")
        self.hi_there.grid(column=0, row=1, pady=20)

        self.hi_there =  tk.Entry(self,width=70, textvariable=pasta_destino)
        self.hi_there.grid(column=1, row=1, padx=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Seleciona"
        self.hi_there["command"] = self.selecionar_pw
        self.hi_there.grid(column=2, row=1, padx=10)

        self.hi_there = tk.Label(self ,text="Layout")
        self.hi_there.grid(column=0, row=2, padx=10)

        self.hi_there =  tk.Entry(self,width=70, textvariable=pasta_origem)
        self.hi_there.grid(column=1, row=2, padx=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Seleciona"
        self.hi_there["command"] = self.selecionar_layout
        self.hi_there.grid(column=2, row=2, padx=10)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Confirmar"
        self.hi_there["command"] = self.substituir_layout
        self.hi_there.grid(column=1, row=3, pady=20)

    def selecionar_pw(self):
        menu.filenamePw =  filedialog.askdirectory()
        pasta_destino.set(menu.filenamePw)

    def selecionar_layout(self):
        menu.filenameLayout =  filedialog.askdirectory()
        pasta_origem.set(menu.filenameLayout)
        arquivo = open("tmpLayout.txt", "w")
        arquivo.write(pasta_origem.get())
        arquivo.close()

    def substituir_layout(self):
        origem = pasta_origem.get()+'/userdata/systemsettings.ini'
        destino= pasta_destino.get()+'/element/userdata/systemsettings.ini'
  
        try:
            os.remove(destino)
            print('Arquivo systemsettings.ini removido com sucesso.')
        except OSError as exc:
            self.info['text'] = 'Falha!'
            self.info['fg'] = 'red'
            print(exc)

        try:
            shutil.copyfile(origem, destino)
            print('Arquivo systemsettings.ini movido com sucesso.\n')
        except OSError as exc:
            self.info['text'] = 'Falha!'
            self.info['fg'] = 'red'
            print(exc)
            return

        origem = pasta_origem.get()+'/userdata/character'
        destino = pasta_destino.get()+'/element/userdata/character'
       
        try:
            shutil.rmtree(destino)
            print('Pasta character removido com sucesso.')
        except OSError as exc:
            self.info['text'] = 'Falha!'
            self.info['fg'] = 'red'
            print('Erro ao deletar pasta character:' +exc)

        try:
            shutil.copytree(origem, destino)
            print('Pasta character movida com sucesso.')
        except OSError as exc: # python >2.5
            if exc.errno == errno.ENOTDIR:
                shutil.copy(origem, destino)
            else: raise

        self.info['text'] = 'Sucesso!'
        self.info['fg'] = 'green'
        


app = Application(master=menu)
app.mainloop()
