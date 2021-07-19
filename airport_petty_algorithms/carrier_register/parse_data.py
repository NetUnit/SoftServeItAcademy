# garbage collector

import copy
import re


# variable = 1
# print(variable)

# retrieved_from_garabage = copy.deepcopy(variable)

# variable = 2
# print(variable)

# print(retrieved_from_garabage)

# # garbage collector

# def parse_string(data, *args, **kwargs):
#     data = data.split(' ')
#     return data

# data = 'DLH 1539'
# print(parse_string(data))

import openpyxl as open
from pathlib import Path
import string



def parse_string2(*args, **kwargs):
    '''
        We will be using all retrieved data from xlsx file
        as local variables. After slicing the data we would then ask 
        a user how to save fields or rewrite data to the same/another
        file. 

        NOTE: make a script executable file then 
    '''

    # convert and find xlsx file
    xlsx_file = Path('/home/netunit/Desktop/reestr', 'reestr.xlsx')
    wb_obj = open.load_workbook(xlsx_file)
    
    sheet = wb_obj.active

    # will print A2 -value
    ##print(sheet['A2'].value)

    # convert arline var to int indices for better reading
    airline = 0 
    board_number = 1

    # iteration through row airline & board_number
    for cell in sheet:
        if cell[airline].value != 'airline':
            airline_data = cell[airline].value
            print(airline_data)
        
        #data = cell[board_number].value
        digit_number = ''.join([
            digit for digit in cell[board_number].value if digit.isdigit()
            ])
        print(digit_number)


        ## lazy version of getting str data
        # letter_component = ''.join([letter for letter in cell[board_number].value if letter not in digit_number])
        # print(letter_component)


        # getting str data using string library object
        letter_component = ''.join([
            letter for letter in cell[board_number].value if letter in string.ascii_letters
            ])
        print(letter_component)
            
print(parse_string2())
