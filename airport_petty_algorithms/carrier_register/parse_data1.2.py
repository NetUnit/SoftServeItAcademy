# garbage collector

import copy
from os import write
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
import datetime

def match_items(*args):
    pass

print(match_items())

def parse_string2(*args, **kwargs):
    '''
        We will be using all retrieved data from xlsx file
        as local variables. After slicing the data we would then ask 
        a user how to save fields or rewrite data to the same/another
        file. 

        NOTE: make a script executable file then 
    '''
    # return datetime.date.today() 2021-07-23
    # convert and find xlsx file
    reestr_lsx_file = Path(
        '/media/netunit/storage/SoftServeItAcademy/airport_petty_algorithms/carrier_register',
        'Reestr_UTN.xlsx')
    reestr_obj = open.load_workbook(reestr_lsx_file)
    
    oblik_lsx_file = Path(
        '/media/netunit/storage/SoftServeItAcademy/airport_petty_algorithms/carrier_register',
         'Oblik.xlsx')
    oblik_obj = open.load_workbook(oblik_lsx_file)

    reestr_sheet = reestr_obj.active
    oblik_sheet = oblik_obj.active
    
    # return (reestr_sheet, oblik_sheet) +++
    # will print A2 -value
    # return (reestr_sheet['A']) # will return the whole sheet column: (<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.A2>, <Cell 'Sheet1'.A3>) +++
    #[print(cell.value) for cell in oblik_sheet['A']] ## ---> МАУ | Роза Вітрів | Osagau Chemicals | +++
    
    # return datetime.date.today()
    # filter_by_date = list(filter(lambda item: item == datetime.date.today(), reestr_sheet['A'])) ### []
    # return filter_by_date
    # current_date_sheet = reestr_sheet

    ## convert date stage
    # return datetime.date.today() --> get current date
    
    # print(reestr_sheet['A2'].value == datetime.date.today()) ### ---> False need to change the date
    today = datetime.date.today()
    today = datetime.date.strftime(today, '%d.%m.%Y') ## ('23.07.2021', '23.07.2021') ---> converted done

    # create dictionary which allows duplicates keys + nested values
    items = dict([])
    print(items)
    for i in range(1, len(reestr_sheet['J'])+1):
        items[reestr_sheet[f'J{i}'].value.lower()] = []
    print(items)

    ## return reestr_sheet['A2'].value == today ---> True
    # return reestr_sheet['A']
    for i in range(1, len(reestr_sheet['A'])+1):
        ## print(reestr_sheet[i]) ++
        filter_by_date_cells = list(filter(lambda item: item.value == today, reestr_sheet[i])) ### []
        print(reestr_sheet[i])
        if any(filter_by_date_cells):
            
            ## filling a data of amounts through dict of duplicate keys + nested values
            #items[reestr_sheet[f'J{i}'].value] = []
            condition = reestr_sheet[f'G{i}'].value != 0
            items[reestr_sheet[f'J{i}'].value.lower()].append(reestr_sheet[f'G{i}'].value) if condition else items.pop()
            print(items)
            # (reestr_sheet[i]) ## same
            # print(f'G{i}: ' + str(reestr_sheet[f'G{i}'].value)) ## same
            print(reestr_sheet[f'G{i}'].value) ## --->>> GOTCHA!! ## same

            # cell of sheet oblik
            # print(oblik_sheet[f"A{i}"].value)
            
            # regex part - may adjust it later
            #print(len(re.compile(oblik_sheet[f"A{i}"].value).match(reestr_sheet[f"J{i}"].value).group(0)))
        else:
            print('sucks')
    
    ## collect data from sheet#1 - preparing fields
    ## for carrier/amount daily report
    def add_amounts(items):
        daily_amount = 0
        for key, value in items.items():
            items[key] = sum(value)
            daily_amount += sum(value)
        return items

    items = add_amounts(items)
    print(items)

   ## getting collected amount values from sheet reestr
   ## through dicts keys in the fields of sheet#2 - zvit

    ###add a match 
 
    try:
        for carrier in oblik_sheet[f'A']:
            value = items.get(str(carrier.value).lower())
            if value:
                print(f'{carrier.value}: {value}')
            else:
                pass
    except:
        print ('Nothing has been found')

    
    ## input fuel arrival:
    try:
        fuel_arrived = int(input('Введіть надходження палива, кг: '))
            
        for cell in oblik_sheet[f'A']:
            print(cell.value)
            pattern = re.compile('Надходження палива')
            condition = pattern.match(str(cell.value))
            #print(condition)
            print(f'{cell.value}: {fuel_arrived} кг' ) if condition else 'Nothing'
    except (TypeError, ValueError) as input_error:
        pass

    
    ## input fuel residue:
    try:
        yest = datetime.date.today() - datetime.timedelta(days=1)
        yest = datetime.date.strftime(yest, '%d.%m.%Y')
        fuel_residue = int(input(f'Введіть залишок палива КГ, на дату {yest} 23:59: '))
        condition = fuel_residue is not None
        print(fuel_residue) if condition else 'Nothing'
    except (TypeError, ValueError) as input_error:
        pass


    ## up-to-date fuel residue calculation (at the end of a current date)
    try:
        daily_amount = sum([i for i in items.values()])
        print(daily_amount) ### FIELD
        residue_today = fuel_residue + fuel_arrived - daily_amount
        print(residue_today) ### FIELD
    except:
        pass 



    # print(type(fuel_arrived)) <class 'int'>


    # method 2 the same
    # try:
    #     i = 0
    #     for carrier in oblik_sheet[f'A']:
    #         ss = carrier
    #         i += 1
    #         carrier = items.get(carrier.value)
    #         if carrier:
    #             print(f'{ss.value}: {carrier}')
    #             print(f'{oblik_sheet[f"A{i}"].value}: {carrier}')
    #         else:
    #             pass
    # except:
    #     return ('Nothing has been found')




        #print(filter_by_date_cells)
        # if filter_by_date_cells:
        #     x = list().append(reestr_sheet[i])
        
    #filter_by_date_cells = list(filter(lambda item: item.value == today, reestr_sheet[rieri])) ### []

    #return filter_by_date_cells



    # works
    # str_data = 'pip3 install python'
    # searched = re.match(r'pip3'|r'install', str_data)
    # return searched



    # convert arline var to int indices for better reading
    # airline = 0 
    # board_number = 1

    # # iteration through row airline & board_number
    # for cell in sheet:
    #     if cell[airline].value != 'airline':
    #         airline_data = cell[airline].value
    #         print(airline_data)
        
    #     #data = cell[board_number].value
    #     digit_number = ''.join([
    #         digit for digit in cell[board_number].value if digit.isdigit()
    #         ])
    #     print(digit_number)


    #     ## lazy version of getting str data
    #     # letter_component = ''.join([letter for letter in cell[board_number].value if letter not in digit_number])
    #     # print(letter_component)


    #     # getting str data using string library object
    #     letter_component = ''.join([
    #         letter for letter in cell[board_number].value if letter in string.ascii_letters
    #         ])
    #     print(letter_component)
            
print(parse_string2())




## fuel arrived part
    # fuel_arrived = int(input('Введіть надходження палива, кг: '))
        
    # for cell in oblik_sheet[f'A']:
    #     print(cell.value)
    #     pattern = re.compile('Надходження палива')
    #     condition = pattern.match(str(cell.value))
    #     #print(condition)
    #     #print(f'{cell.value}: {fuel_arrived} кг' ) if condition else 'None'