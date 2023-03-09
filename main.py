from csvshortcuts.csvupdate import CsvUpdate
from table import Table
from problem import Problem
from collections import deque
from os import listdir
from random import randint




if __name__ == '__main__':

    ##Convert to allow updating files later
    all_tables = {}
    all_questions = []
    folder_path = r'D:\Leetcode\Questions by Filter'


    for file in listdir(folder_path):

        ##Setup for future plans
        name = file.split(' ')[0]
        filepath = folder_path + r'\\' + file
        table = CsvUpdate.read_csv(filepath)
        table.pop(0)
        all_tables[name] = table

        ##Randomizer

        for row in table:
            all_questions.append(row)

    your_question = all_questions[randint(0, len(all_questions))]

    print(f'Your question is {your_question[0]} from {your_question[-1]}')

