#!./venv/bin/python
# -*- coding: utf-8 -*-
import xlrd3
import os
import sys
from random import randint


def help():
    print("\n")
    print(
    ''' 
	================================ Forma de uso ==========================

	python relatorios-meis.py [id_profile] [nome_do_arquivo] [nome_do_arquivo]

	Ex:.
	python relatorios-meis.py 409738522 teste1.xlsx teste2.xlsx teste3.xlsx ...

	========================================================================
	'''
    )


def create_files(id_profile, files):
    mkdir('relatorios')
    for file in files:
        workbook = xlrd3.open_workbook(file)
        worksheet = workbook.sheet_by_index(0)
        size_block = 999
        for item in range(1, int(worksheet.nrows / size_block) + 2):
            with open('./relatorios/relatorio-{}-imei-{}'.format(str(item),randint(0, 999999))+'.csv', "w", newline='\n') as f:
                f.write("modemtype,modemid,manufacturer,profiletype,profileid\n")
                if (worksheet.nrows / item) < size_block:
                    for row in range(item*size_block-size_block, worksheet.nrows):
                        f.write("IMEIS,{},Positivo,ZERO_TOUCH,{}\n".format(worksheet.cell_value(row, 2),id_profile,))
                else:
                    for row in range(item*size_block-size_block, item*size_block):
                        f.write("IMEIS,{},Positivo,ZERO_TOUCH,{}\n".format(worksheet.cell_value(row, 2),id_profile,))
                f.close()


def clear():
    if sys.platform == "linux":
        os.system('clear')
    else:
        os.system('cls')


def mkdir(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def file_exist(path):
    return os.path.exists(path)
