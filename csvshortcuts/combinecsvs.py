from csvshortcuts import readfiles, writefiles


##preforms naive combination of csvs
def combine_csvs(csv_1, csv_2, matching_headers = True):

    new_table = []
    split_point = csv_1.rfind(r'\\')
    new_name = csv_1[split_point:]
    file_path = csv_1[:split_point + 1]
    table_1 = readfiles.read_csv(csv_1)
    table_2 = readfiles.read_csv(csv_2)

    if matching_headers:
        table_2.pop(0)

    for table in [table_1, table_2]:
        for row in table:
            new_table.append(row)


    writefiles.write_csv(
        f'{file_path}{new_name} combined',
        new_table
    )