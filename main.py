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
        ('csv', '*.csv'),
    )

    filename = filedialog.askopenfilename(
        title='Open a files',
        initialdir='./',
        filetypes=filetypes)
    
    return filename

def create_files_splitted(id_profile, files):
    mkdir('relatorios')   
    try:
        file_number = 0
        for file in files:
            create_csv_file(id_profile, file, file_number)
            # To enumerate the files when selected files > 1
            file_number += 1
    except Exception as e:
        print(e)
        showinfo(
            title="Error",
            message="Error to create files. \n{}".format(e)
        )
    finally:
        label_processes['text'] = '''Processo finalizado!'''


def show_files_selected(list_files):
    list_files_selected = [file.split('/')[-1] for file in list_files]
    label_files_selected['text'] = '''Arquivos selecionados:\n{}\n'''.format(str(list_files_selected))


if __name__ == "__main__":
  
    root = Tk()
    root.title("Gerar Relatorios IMEIS")
    root.configure(background="#333533")
    label_color_background = "#333533"
    label_color_fg = "#9381ff"
    button_color_background = "#fff"
    button_color_foreground = "#9381ff"
    button_activebackground = "#9381ff"

    # Button to select files
    label_selector = Label(
        root,
        text='''
            Selecione todas as planilhas que deseja gerar relatórios no botão select file. 
            ''',
        background=label_color_background,
        fg=label_color_fg,
        font=("roboto", 14, "bold")
    )
    label_selector.grid(row=0, column=3, padx=10, pady=10)

    label_info = Label(
        root,
        text='''
            OBS:\n  
            1 - Somente arquivos .csv\n
            2 - Após clicar em gerar sera criado uma pasta com nome relatórios que contem os arquivos de saida.\n
            3 - Se já houver uma pasta com mesmo nome, esta sera apagada.\n
            4 - Clique no botão Show Files se deejar visualizar os arquivos selecionados.
            ''',
        background=label_color_background,
        fg=label_color_fg,
        font=("roboto", 8)
    )
    label_info.grid(row=1, column=3)

    files = []
    open_button = Button(
        root,
        text='Select File',
        command=lambda: files.append(select_files()),
        bg=button_color_background,
        activebackground=button_activebackground,
        fg=button_color_foreground,
        border=0,
        font=("roboto", 12, "bold"),
        activeforeground=button_color_background,   
    )
    open_button.grid(row=2, column=2, padx=10, pady=10)

    show_button = Button(
        root,
        text='show files',
        command=lambda: show_files_selected(files),
        bg=button_color_background,
        fg=button_color_foreground,
        activebackground=button_activebackground,
        border=0,
        font=("roboto", 12, "bold"),
        activeforeground=button_color_background
    )
    show_button.grid(row=2, column=4, padx=10, pady=10)

    # Files selected
    label_files_selected = Label(
        root,
        text="", 
        background=label_color_background, 
        fg=label_color_fg,
        font=("roboto", 10)
    )
    label_files_selected.grid(row=3, column=3, padx=10, pady=10)

    # Field with the id profile
    label_id = Label(
        root,
        text="ID do Profile:",
        background=label_color_background,
        fg=label_color_fg,
        font=("roboto", 12, "bold")
    )
    label_id.grid(row=4, column=3, padx=10, pady=10)

    id_profile = StringVar()
    field_id_profile = Entry(root, textvariable=id_profile, border=0)
    field_id_profile.grid(row=5, column=3, padx=10, pady=10)

    # Button for creating the files
    button_create_files = Button(
        root, 
        text="Gerar Relatorios",
        command=lambda: create_files_splitted(id_profile.get(), files),
        bg=button_color_background,
        fg=button_color_foreground,
        activebackground=button_activebackground,
        border=0,
        font=("roboto", 12, "bold"),
        activeforeground=button_color_background
    )
    button_create_files.grid(row=6, column=3, padx=10, pady=10)

    label_processes = Label(
        root,
        text="",
        background=label_color_background,
        fg=label_color_fg,
        font=("roboto", 14, "bold")
    )
    label_processes.grid(row=7, column=3, padx=10, pady=10)


    root.mainloop()

