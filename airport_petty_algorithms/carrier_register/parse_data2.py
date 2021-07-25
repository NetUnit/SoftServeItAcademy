# garbage collector

import copy
from os import write
import re

import openpyxl as open
from pathlib import Path
import string
import datetime
#import xlsxwriter

def parse_string(*args, **kwargs):
    '''
        We will be using all retrieved data from xlsx file
        as local variables. After slicing the data we would then ask 
        a user how to save fields or rewrite data to the same/another
        file. 

        NOTE: make a script executable file then 
    '''

    ## convert and find xlsx file --> make a widget for file location later
    ## [.....] ADD WIDGET HERE
    reestr_lsx_file = Path(
        '/home/netunit/Desktop/carrier_register',
        'Реєстр Укртатнафта Jet A-1.xlsx')
    reestr_obj = open.load_workbook(reestr_lsx_file)
    
    oblik_lsx_file = Path(
        '/home/netunit/Desktop/carrier_register',
         'Звіт 23.07.2021 Jet A-1.xlsx')
    oblik_obj = open.load_workbook(oblik_lsx_file)

    print(type(oblik_obj))

    reestr_sheet = reestr_obj.active
    oblik_sheet = oblik_obj.active

    ## convert lambda function for date convert- ---> allows to convert date's if sheet was changed
    ## NOTE: remake this fucntion after beacuse if the cell is not a timedatae format it'll raise an error
    ## to an appropriate format: '%Y-%m-%d'
    converted = lambda date: datetime.date.strftime(date, '%Y-%m-%d')
    
    #get today's date
    today = datetime.date.today() ## 2021-07-24 <class 'datetime.date'>
    
    ## create a dictionary which allows duplicates keys + nested values
    #  --> remake to a the LC later
    items = dict([])

    for i in range(1, len(reestr_sheet['L'])+1):
        condition = reestr_sheet[f'L{i}'].value != None
        if condition:
            items[reestr_sheet[f'L{i}'].value.lower()] = []

    ## iterate through reestr sheet cells and get filter by todays date
    for i in range(1, len(reestr_sheet['A'])+1):
        
        ## avoid errors when iterating blanc fields
        condition = reestr_sheet[f'A{i}'].value != None

        ## use this condition to raise date_error and render to a window of errors
        ## whnen incorrect date was put or wrong format 
        condition2 = isinstance(reestr_sheet[f'A{i}'].value, datetime.date) 
        
        if condition:
            filter_by_date_cells = list(filter(
                lambda item: str(item.value)[:10] == converted(today), reestr_sheet[i]
                ))
        
            if any(filter_by_date_cells):
                
                ## this condition will avoid adding Nones to nested dict values
                ## avoid: TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
                condition3 = reestr_sheet[f'F{i}'].value != None
                items[reestr_sheet[f'L{i}'].value.lower()].append(reestr_sheet[f'F{i}'].value) if condition3 else 0
                    
    ## getting collected amount values from sheet reestr by carrier
    ## returns dict with the next data: key - carrier, value - daily amount in kgs
    def add_amounts(items):
        daily_amount = 0
        for key, value in items.items():
            items[key] = sum(value)
            daily_amount += sum(value)
        return items

    items = add_amounts(items)
    print(items)


    ## writing fields E5-E22 using prapared dict of items
    ## with 'Zvit' Fields C5-C22 as keys
    ## stage2: write matched by key values into cells through
    ## get from loop indices - i
    try:

        i = 0
        for carrier_cell in oblik_sheet[f'C']:

            ## condition willl avoid exceptions
            ##  when using blank cell as a key 
            condition4 = carrier_cell.value is not None
            record_value = items.get(str(carrier_cell.value).lower()) if condition4 else 0
            
            ## iteration should be in this block 
            ## as we need to get all indices of cells and sort only those
            ## where carrier/key - value from items were found
            i += 1
            if record_value:
                oblik_sheet[f'E{i}'].value = record_value            
                oblik_obj.save('Звіт 23.07.2021 Jet A-1.xlsx')         

    except:
        print ('Render a possible error here to the window')

    
    ## input fuel arrival:
    try:
        fuel_arrived = int(input('Введіть надходження палива, кг: '))
        i = 0
        for cell in oblik_sheet[f'C']:
            i += 1
            pattern = re.compile('Прибуток палива')
            ## find appropriate cell condition to write daily fuel suppply 
            condition = pattern.match(str(cell.value)) is not None
            if condition:
                oblik_sheet[f'E{i}'].value = fuel_arrived 
                oblik_obj.save('Звіт 23.07.2021 Jet A-1.xlsx')

    except ValueError as input_err:
        print('Please do not enter letters')
        pass

    except (TypeError, AttributeError) as input_error:
        print('Please enter a correct amount')
        pass


    ## input fuel residue:
    ## dependant block on up-to-date fuel residue calculation
    try:
        yest = datetime.date.today() - datetime.timedelta(days=1)
        yest = datetime.date.strftime(yest, '%d.%m.%Y')
        ## variable value will be added for todays residue calculation
        fuel_residue = int(input(f'Введіть залишок палива КГ, на дату {yest} 23:59: '))
        ## awoid errors when blanc field of fuel supply (no fuel supply daily)
        condition = fuel_residue is not None
        #print(fuel_residue) if condition else 'Nothing'
    except (TypeError, ValueError) as input_error:
        pass


    ## up-to-date fuel residue calculation (at the end of a current date)
    try:
        daily_amount = sum([i for i in items.values()])
        print(daily_amount) ### E23 field
        residue_today = fuel_residue + fuel_arrived - daily_amount
        print(residue_today) ### FIELD E26 field
    except:
        pass 

            
print(parse_string())