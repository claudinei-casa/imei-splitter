#!./venv/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from file import *


def select_files():
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt'),
        ('xls files', '*.xl*'),
        ('csv files', '*.csv'),
    )

    filename = filedialog.askopenfilename(
        title='Open a files',
        initialdir='./',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    
    return filename


def show_files_selected(list_files):
    list_files_selected = [file.split('/')[-1] for file in list_files]
    label_files_selected['text'] = '''Arquivos selecionados:\n{}\n'''.format(str(list_files_selected))


if __name__ == "__main__":
  
    root = Tk()
    root.title("Gerar Relatorios IMEIS")

    # Button for select files to script
    label_selector = Label(root, text="Selecione todas as planilhas que deseja gerar relatórios")
    label_selector.grid(row=0, column=3, padx=10, pady=10)
    files = []
    open_button = Button(
        root,
        text='Select File',
        command=lambda: files.append(select_files())
    )
    open_button.grid(row=1, column=2, padx=10, pady=10)

    # Files selected
    label_files_selected = Label(root, text="")
    label_files_selected.grid(row=2, column=3, padx=10, pady=10)
    show_button = Button(
        root,
        text='show files',
        command=lambda: show_files_selected(files)
    )
    show_button.grid(row=1, column=4, padx=10, pady=10)

    # Field with the id profile
    label_id = Label(root, text="ID do Profile:")
    label_id.grid(row=3, column=3, padx=10, pady=10)
    id_profile = StringVar()
    field_id_profile = Entry(root, textvariable=id_profile)
    field_id_profile.grid(row=4, column=3, padx=10, pady=10)

    # Button for creating the files
    button_create_files = Button(root, text="Gerar Relatorios", command=lambda: create_files(id_profile.get(), files))
    button_create_files.grid(row=5, column=3, padx=10, pady=10)

    root.mainloop()

