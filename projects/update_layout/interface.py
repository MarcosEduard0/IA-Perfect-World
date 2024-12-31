# -*- coding: UTF-8 -*-
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from img import img
import shutil, os, base64
from datetime import datetime


class Layout(tkinter.Frame):
    def __init__(self):
        self.win = tkinter.Tk()
        self.fold_pw = StringVar()
        largura = self.win.winfo_screenwidth()
        altura = self.win.winfo_screenheight()
        self.win.geometry(
            "%dx%d+%d+%d" % (500, 150, largura / 2 - 500 / 2, altura / 2 - 150 / 2)
        )
        self.win.title("I.A do John")
        self.win.resizable(0, 0)  # Limita o tamanho da janela principal
        self.setIcon()
        self.list_folders()
        self.create_widgets()
        self.win.mainloop()

    def setIcon(self):
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img))  # Escreve um arquivo temporário
        tmp.close()
        self.win.iconbitmap("tmp.ico")  # Coloca o ícone
        os.remove("tmp.ico")  # Remove o arquivo temporário

    def list_folders(self):
        root_dir = os.getcwd()  # Obtém o diretório de execução
        folders = [f for f in os.listdir(root_dir) if os.path.isdir(f)]

        # Verificando e removendo a pasta "LayOut&ProgramsPW"
        if "LayOut&ProgramsPW" in folders:
            folders.remove("LayOut&ProgramsPW")

        if not folders:
            messagebox.showerror("Erro", "Nenhuma pasta encontrada no diretório atual.")
            self.win.destroy()
            return

        # Ordena as pastas pela data de modificação (mais recente primeiro)
        folders = sorted(
            folders,
            key=lambda x: os.path.getmtime(x),
            reverse=True,
        )

        # Define a pasta mais recente como padrão
        if folders:
            self.most_recent_folder = folders[0]
            self.fold_pw.set(self.most_recent_folder)

        # Atualizando a lista
        self.folders = [f for f in folders]

    def create_widgets(self):
        # Título informativo
        Label(
            self.win,
            text="Selecione a pasta do Perfect World para a operação:",
            font=("Arial", 10, "bold"),
            fg="black",
            pady=10,
        ).grid(column=0, row=0, columnspan=2, sticky=W, padx=10)

        # Dropdown para seleção de pasta de origem
        Label(self.win, text="Pasta do Perfect World:", font=("Arial", 10)).grid(
            column=0, row=1, sticky=E, padx=(10, 5), pady=5
        )
        dropdown = ttk.Combobox(
            self.win, textvariable=self.fold_pw, values=self.folders, width=40
        )
        dropdown.grid(column=1, row=1, sticky=W, pady=5)
        dropdown.set(self.fold_pw.get())  # Define a pasta padrão

        # Botão de confirmação
        confirm_button = Button(
            self.win,
            text="Confirmar",
            command=self.substituir_layout,
            bg="green",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15,
        )
        confirm_button.grid(column=0, row=2, columnspan=2, pady=15)

    def substituir_layout(self):
        origem = os.path.abspath("LayOut&ProgramsPW\\element")
        destino = os.path.join(self.fold_pw.get(), "element")
        try:
            # Copia arquivos individualmente, sobrescrevendo os existentes
            for root, dirs, files in os.walk(origem):
                # Calcula o caminho relativo para preservar a estrutura de pastas
                rel_path = os.path.relpath(root, origem)
                dest_path = os.path.join(destino, rel_path)

                # Verifica se o caminho de destino é "character" ou "Layout"
                if "character" in dest_path or "Layout" in dest_path:
                    if os.path.exists(dest_path):
                        shutil.rmtree(dest_path)  # Remove o diretório completamente

                    os.makedirs(dest_path)  # Recria o diretório vazio

                # Cria subpastas, se necessário
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)

                # Copia os arquivos
                for file in files:
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(dest_path, file)
                    shutil.copy2(src_file, dest_file)  # Copia preservando metadados
                    print(
                        f"Arquivo '{dest_file.split("element/")[-1]}' copiado com sucesso."
                    )

            messagebox.showinfo(
                title="Sucesso", message="Arquivos copiados com sucesso."
            )
        except Exception as exc:
            messagebox.showerror(title="Erro", message=str(exc))

        self.win.destroy()


if __name__ == "__main__":
    MainWin = Layout()
