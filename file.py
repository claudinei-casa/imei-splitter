#!./venv/bin/python
# -*- coding: utf-8 -*-
import csv
import os
import shutil


def create_csv_file(id_profile, file, file_number):
    '''
    Create a csv file with id_profile = id for google
    file = path to csv file with name
    file_number = number of file when selected files > 1
    '''

    # Size or numeber os lines - 1 (header) from csvs outputs
    size_block = 999
    data = []
    # Read a csv file and save it in a list 
    with open(file, "r") as f:
        database = csv.reader(f)
        for row in database:
            data.append(row)

    rows = data[1:]
    header = data[:1]
    number_of_rows = len(rows)
    number_of_blocks = number_of_rows // size_block

    for item in range(1, number_of_blocks + 2):
        print("Gerando arquivo(s): {}".format(str(file_number)))

        # Column selected from the table, this column indicate the device IMEI on the input file csv.
        column = 1

        with open('./relatorios/relatorio-file-{}-imeis-item-{}.csv'.format(str(file_number),str(item)), "w", newline='\n') as f:
            f.write("modemtype,modemid,manufacturer,profiletype,profileid\n")
            # Final block contents or number_of_rows % size_block
            if (number_of_rows / item) < size_block:
                print("Planilha {}".format(str(item)))
                for row in range(item*size_block-size_block, number_of_rows):                       
                    f.write("IMEI,{},Positivo,ZERO_TOUCH,{}\n".format(rows[row][column],str(id_profile)))
            # Another blocks
            else:
                print("Planilha {}".format(str(item)))
                for row in range(item*size_block-size_block, item*size_block):
                    f.write("IMEI,{},Positivo,ZERO_TOUCH,{}\n".format(rows[row][column],str(id_profile)))


def mkdir(path):
    #Delete the directory if it already exists
    if file_exist(path):
       remove_dir(path)

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)


def file_exist(path):
    return os.path.exists(path)


def remove_dir(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        print(f"Error:{ e.strerror}")
