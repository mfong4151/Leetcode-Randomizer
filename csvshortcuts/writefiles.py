from csv import writer
from os import chdir, listdir, getcwd
from datetime import datetime as dt


#Responsible writing for the actual CSV file
def write_csv(data_file_name, table):
    now = dt.now()


    date_now = now.strftime("%Y/%m/%d %H:%M:%S").replace(":", ".").replace("/", ".")

    data_file_name += f' {date_now}.csv'

    with open(data_file_name, mode='w', newline='', encoding="utf-8") as data_file:

        csv_writer = writer(data_file)


        for row in table:

            csv_writer.writerow(row)
