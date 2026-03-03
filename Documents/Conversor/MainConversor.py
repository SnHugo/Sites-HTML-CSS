import subprocess
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def selecionar_arquivos():
    arquivos = filedialog.askopenfilenames(
        title="Selecione arquivos MP4",
        filetypes=[("Arquivos MP4", "*.mp4")]
    )
    lista_arquivos.delete(0, tk.END)
    for arquivo in arquivos:
        lista_arquivos.insert(tk.END, arquivo)

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    entrada_pasta.delete(0, tk.END)
    entrada_pasta.insert(0, pasta)

def converter():
    arquivos = lista_arquivos.get(0, tk.END)
    pasta_saida = entrada_pasta.get()
    formato = combo_formato.get()

    if not arquivos:
        messagebox.showerror("Erro", "Nenhum arquivo selecionado.")
        return

    if not pasta_saida:
        messagebox.showerror("Erro", "Selecione uma pasta de saída.")
        return

    for arquivo in arquivos:
        nome_base = os.path.splitext(os.path.basename(arquivo))[0]
        arquivo_saida = os.path.join(pasta_saida, f"{nome_base}.{formato}")

        comando = [
            "ffmpeg",
            "-i", arquivo,
            "-vn",
            arquivo_saida
        ]

        subprocess.run(comando)

    messagebox.showinfo("Sucesso", "Conversão concluída!")

janela = tk.Tk()
janela.title("Conversor MP4 para Áudio")
janela.geometry("500x400")

btn_selecionar = tk.Button(janela, text="Selecionar Arquivos", command=selecionar_arquivos)
btn_selecionar.pack(pady=10)

lista_arquivos = tk.Listbox(janela, width=60, height=8)
lista_arquivos.pack()

btn_pasta = tk.Button(janela, text="Selecionar Pasta de Saída", command=selecionar_pasta)
btn_pasta.pack(pady=10)

entrada_pasta = tk.Entry(janela, width=60)
entrada_pasta.pack()

tk.Label(janela, text="Formato de saída:").pack(pady=5)

combo_formato = ttk.Combobox(janela, values=["mp3", "wav", "flac", "aac"])
combo_formato.current(0)
combo_formato.pack()

btn_converter = tk.Button(janela, text="Converter", command=converter)
btn_converter.pack(pady=20)

janela.mainloop()