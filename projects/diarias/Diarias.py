import tkinter as tk
from datetime import datetime
import os
import json

# Nome do arquivo para salvar os dados
APP_NAME = "DiariasPW"
SAVE_FILE = os.path.join(os.getenv("APPDATA"), APP_NAME, "checklist_data.json")


# Certificar-se de que o diretório existe
def ensure_directory():
    directory = os.path.dirname(SAVE_FILE)
    if not os.path.exists(directory):
        os.makedirs(directory)


ensure_directory()


# Função para carregar os dados salvos
def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
            return data
    return {}


# Função para salvar os dados
def save_data(data):
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file)


# Função para resetar os checks diariamente
def reset_daily():
    data = load_data()
    last_reset = data.get("last_reset", "")
    today = datetime.now().strftime("%Y-%m-%d")

    if last_reset != today:
        for item in data.get("items", []):
            item["checked"] = False
        data["last_reset"] = today
        save_data(data)


# Função para adicionar um novo item
def add_item(event=None):
    item_text = entry.get()
    if item_text:
        checklist.append({"text": item_text, "checked": False})
        update_list()
        entry.delete(0, tk.END)


# Função para remover um item
def remove_item(index):
    del checklist[index]
    update_list()


# Função para atualizar a lista visual
def update_list():
    for widget in frame.winfo_children():
        widget.destroy()

    # Criar colunas dinamicamente
    columns = []
    for i in range(0, len(checklist), 10):
        column_frame = tk.Frame(frame)
        column_frame.pack(side="left", padx=10, anchor="n")
        columns.append(column_frame)

    for idx, item in enumerate(checklist):
        column_index = idx // 10
        column_frame = columns[column_index]

        var = tk.BooleanVar(value=item["checked"])

        # Criar uma linha com checkbox e botão de remoção
        item_frame = tk.Frame(column_frame)
        item_frame.pack(anchor="w", pady=2, fill="x")

        checkbox = tk.Checkbutton(
            item_frame,
            text=item["text"],
            variable=var,
            command=lambda i=idx, v=var: toggle_check(i, v),
        )
        checkbox.pack(side="left", padx=5)

        remove_button = tk.Button(
            item_frame,
            text="X",
            command=lambda i=idx: remove_item(i),
            fg="red",
            bg="white",
        )
        remove_button.pack(side="right", padx=5)


# Função para alternar o estado do check
def toggle_check(index, var):
    checklist[index]["checked"] = var.get()


# Função para salvar os dados ao sair
def save_and_exit():
    data = {"last_reset": datetime.now().strftime("%Y-%m-%d"), "items": checklist}
    save_data(data)


# Carregar dados e resetar se necessário
reset_daily()
data = load_data()
checklist = data.get("items", [])

# Configuração da interface gráfica
root = tk.Tk()
root.title("Checklist Diário")

# Configurar tamanho e posição da janela
largura = root.winfo_screenwidth()
altura = root.winfo_screenheight()
root.geometry("%dx%d+%d+%d" % (800, 400, largura / 2 - 400, altura / 2 - 200))
root.resizable(0, 0)  # Limita o tamanho da janela principal

frame = tk.Frame(root)
frame.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

entry = tk.Entry(input_frame)
entry.pack(side="left", padx=5)
entry.bind("<Return>", add_item)  # Adicionar item ao pressionar Enter

add_button = tk.Button(input_frame, text="Adicionar", command=add_item)
add_button.pack(side="left", padx=5)

exit_button = tk.Button(root, text="Salvar", command=save_and_exit)
exit_button.pack(pady=5)

update_list()

root.mainloop()
