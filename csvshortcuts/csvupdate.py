from csvshortcuts.readfiles import *
from csvshortcuts.writefiles import *
from csvshortcuts.combinecsvs import *


class CsvUpdate:
    pass

CsvUpdate.get_past_file = get_past_file
CsvUpdate.get_file_path = get_file_path
CsvUpdate.read_csv =  read_csv
CsvUpdate.write_csv = write_csv
CsvUpdate.combine_csvs = combine_csvs
