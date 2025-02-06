# -*- coding: UTF-8 -*-
import tkinter
from tkinter import *
from tkinter import ttk,messagebox,filedialog
from img import img #Import base64 format img
import shutil, errno
import base64,os

 
class Layout(tkinter.Frame):
    def __init__(self):
        self.processBarLen = 1100
        self.win = tkinter.Tk()
        self.origem = StringVar()
        self.destino = StringVar()
        largura = self.win.winfo_screenwidth()
        altura = self.win.winfo_screenheight()
        self.win.geometry("%dx%d+%d+%d" % (590, 180, largura/2 - 650/2, altura/2 - 350/2))
        self.win.title('I.A do John')
        self.win.resizable(0,0) #Limite o tamanho da janela principal para ser imutável
        self.setIcon()
        self.pachLayoutCache()
        self.info = tkinter.Label(text="Selecione a pasta do novo 'PW' e a pasta 'userdata' com seus yokebone salvos", fg='black')
        self.info.grid(column=1, row=0, pady=(20,0), )
        self.create_widgets()
        self.win.mainloop()

    def pachLayoutCache(self):
        try:
            arquivo = open("PatchLayout.txt", "r")
            self.origem.set(arquivo.read())
            arquivo.close()
        except:
            arquivo = open("PatchLayout.txt", "w")
 
    def setIcon(self):
        tmp = open("tmp.ico","wb+")  
        tmp.write(base64.b64decode(img))#Escreve um arquivo temporario
        tmp.close()
        self.win.iconbitmap("tmp.ico") #Coloca o icone
        os.remove("tmp.ico") #Remove o arquivo temporario

    def create_widgets(self):
        self.index = tkinter.Label(text="Perfect World")
        self.index.grid(column=0, row=1, padx=(10,0),pady=(15,10))

        self.index =  tkinter.Entry(width=50, textvariable=self.destino)
        self.index.grid(column=1, row=1, pady=(15,10))

        self.index = tkinter.Button()
        self.index["text"] = "Seleciona"
        self.index["command"] = self.selecionar_pw
        self.index.grid(column=2, row=1, pady=(15,10))

        self.index = tkinter.Label(text="userdata")
        self.index.grid(column=0, row=2, padx=(10,0))

        self.index =  tkinter.Entry(width=50, textvariable=self.origem)
        self.index.grid(column=1, row=2 )

        self.index = tkinter.Button()
        self.index["text"] = "Seleciona"
        self.index["command"] = self.selecionar_layout
        self.index.grid(column=2, row=2)

        self.index = tkinter.Button()
        self.index["text"] = "Confirmar"
        self.index["command"] = self.substituir_layout
        self.index.grid(column=1, row=3, pady=20)

    def selecionar_pw(self):
        self.win.filenamePw =  filedialog.askdirectory()
        self.destino.set(self.win.filenamePw)

    def selecionar_layout(self):
        self.win.filenameLayout =  filedialog.askdirectory()
        self.origem.set(self.win.filenameLayout)
        arquivo = open("tmpLayout.txt", "w")
        arquivo.write(self.origem.get())
        arquivo.close()

    def substituir_layout(self):
        origem = self.origem.get()+'/userdata/systemsettings.ini'
        destino = self.destino.get()+'/element/userdata/systemsettings.ini'
        if self.destino.get() == '' or self.origem.get() == '':
            messagebox.showerror(title='Erro', message='Selecione a pasta do perfect world')
            return
  
        try:
            os.remove(destino)
            print('Arquivo systemsettings.ini removido com sucesso.')
        except OSError as exc:
            pass

        try:
            shutil.copyfile(origem, destino)
            print('Arquivo systemsettings.ini copiada com sucesso.\n')
        except OSError as exc:
            messagebox.showerror(title='Erro', message=exc)
            return

        origem = self.origem.get()+'/userdata/character'
        destino = self.destino.get()+'/element/userdata/character'
       
        try:
            shutil.rmtree(destino)
            print('Pasta character removido com sucesso.')
        except OSError as exc:
            pass

        try:
            shutil.copytree(origem, destino)
            print('Pasta character copiada com sucesso.')
        except OSError as exc: # python >2.5
            messagebox.showerror(title='Erro', message=exc)
            if exc.errno == errno.ENOTDIR:
                shutil.copy(origem, destino)
            else: raise

        MsgBox = messagebox.showinfo(title=None, message="Arquivos copiados com sucesso.")
        if MsgBox == 'ok':
            self.win.destroy()
 
if __name__ == "__main__":
    MainWin = Layout()       