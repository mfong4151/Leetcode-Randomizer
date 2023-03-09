from csv import reader
from os import chdir, listdir, getcwd


def get_past_file(cwd = getcwd()):

    chdir(cwd)
    files = listdir()
    last_file = files[-1] if files else None
    return last_file

def get_file_path(file_name, cwd =getcwd()):
    chdir(cwd)
    return f'{cwd}\{file_name}'

def read_csv(file):

    table = []

    if file:
        with open(file, mode='r', newline='', encoding="utf8")as read_data_file:

            csv_reader = reader(read_data_file)
            for row in csv_reader:
                table.append(row)

    return table

