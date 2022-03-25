import copy
from os import write
import re
# pyxl
import openpyxl as open
from pathlib import Path
from openpyxl.cell.cell import MergedCell, Cell
# python
import string
import datetime

from openpyxl.utils.exceptions import (
    InvalidFileException
)

from openpyxl import (
    Workbook,

)


class FuelArrivedField:
    '''
        ===========================================================
        This class represents a 'Fuel Supply Widget'
        ===========================================================
        Attrs:
            :param msg2: error message for inappropriate field input
            :type msg: <str>
        
        .. note::
            get_classname() - aims to get cuurent classname when 
            exceptions raised. Inherited by other field classes.
    '''

    msg = 'Please enter a correct amount'
    msg2 = 'shoud be digits or 0 if no supply'
    fuel_arrived = None

    @staticmethod
    def get_classname(field_name):
        field_name = ' '.join(
            re.findall(
                '[A-Z][^A-Z]*',
                field_name
            )
        ).capitalize()
        return field_name

    def __init__(self):
        try:
            self.fuel_arrived = int(
                input(
                    'Enter the fuel supply, kg: '
                    )
                )
        except (TypeError, AttributeError):
            print(self.msg)
        except ValueError:
            field_name = self.__class__.__name__
            msg3 =  self.get_classname(field_name)
            print(f'{msg3} {self.msg2}')
        finally:
            exit() if self.fuel_arrived is None else True

class FuelResidueField(FuelArrivedField):
    '''
        ===========================================================
        This class represents a 'Fuel Arrived Widget'
        ===========================================================
        Attrs:
            :param msg2: error message for inappropriate field input
            :type msg: <str>
    '''

    fuel_residue = None
    def __init__(self, prev_rep_date=None):
        try:
            self.fuel_residue = int(
                input(f'Введіть залишок палива КГ ' + 
                f'на дату {prev_rep_date} 23:59: ')
            )
        except (TypeError, AttributeError):
            print(self.msg)
        except ValueError:
            field_name = self.__class__.__name__
            msg3 =  self.get_classname(field_name)
            print(f'{msg3} {self.msg2}')
        finally:
            exit() if self.fuel_residue is None or prev_rep_date is None else True

class LoadXLSXFileField:

    '''
        ===========================================================
        This class represents a 'Loading XLSL File Widget'
        ===========================================================
        Attrs:
            :param msg2: error message for inappropriate field input
            :type msg: <str>
    '''
    type_error = 'Please select xlsx file properly'

    def __init__(self, path=None, document=None):
        try:
            if path is None or document is None:
                raise TypeError()

            xlsx_file = Path(
                path,
                document
                )
            self.xlsx_file = xlsx_file
            print(f'File was opened: {document}')
        except InvalidFileException as err:
            xlsx_file = None
            print(f'{err}: {document}')
        except TypeError:
            xlsx_file = None
            print(f'{self.type_error}: file - {document}')
        finally:
            exit() if xlsx_file is None else self.xlsx_file
        
    def get_work_book(self):
        print(f'{self.xlsx_file} This is xlsx file')
        work_book = open.load_workbook(self.xlsx_file)
        # print(f'Workbook was loaded: {work_book}')
        return work_book
    
    def activate_work_book(self):
        sheet = self.get_work_book().active
        # print(f'Sheet was activated: {sheet}')
        return sheet


class ParseXLSXData:

    '''
    ===========================================================
    This class represents the manufacturer of a certain product
    ===========================================================
    Attrs:
        :param path: carrier register & final report files folder
        :type path: str
        :param registry_rt: RT type fuel carrier register
        :type registry_rt: xlsx 
        :param registry_jet: JET A-1 type fuel carrier register
        :type date: xlsx
        :param  select_fuel: fuel selection depending upon type
        :type select_fuel: str
        :param format: dd-mm-yyyy Yoda time format
        :type format: str
        :param to_datetime: from <str> to <'datetime.datetime'>
        
    .. note:: 
        Intermediate parameters:
            * :param registry: INITIAL XLSX FILE TO PARSE
            * :param report: INITIAL XLSX FILE TO SAVE REPORT  

        Other 3 paramaters are lambda functions and called when necessary
            * :param to_datetime: from <str> to <'datetime.datetime'>
            * :param to_date: from <str> to <'datetime.date'>
            * :param to_str: from 'datetime.datetime'> to str
            * :param items: dict of pairs: key - carrier, value - list of amounts
            keys - created automatically from the list of carriers
            values - fuel amounts (kg), multiple values associated with a key
            * :type items: dict
        
            * :param fuel_arrived: sets value of the fuel_arrived attribute with
               setattr() function
              :type fuel_arrived: int
            * :param today: get todays time
              :type today: datetime.date
    .. note:: 
        This class represents behaviour that parses registry RT.xlsx & 
        registry JET A-1.xlsx, get, convert and record data cells to 
        report files report RT.xlsx & report JET A-1.xlsx files
    '''
    fuel_choices = ['RT', 'Jet A-1']
    
    path = '/media/netunit/storage/SoftServeItAcademy/airport_petty_algorithms/carrier_register_li'
    path_reserve = '/home/rostyslav/Общедоступные/temp_andrii/SoftServeItAcademy/airport_petty_algorithms/carrier_register_li'
    
    # RT:
    
    registry_rt = 'Реєстр Укртатнафта РТ.xlsx'
    report_rt = 'Звіт РТ.xlsx'

    # registry_rt = 'Реєстр Укртатнафта РТ.txt'
    # report_rt = 'Звіт РТ.txt'

    # Jet A-1:
    registry_jet = 'Реєстр Укртатнафта Jet A-1.xlsx'
    report_jet = 'Звіт Jet A-1.xlsx'

    select_fuel = input('Please select type of fuel U want to make a report of: ')
    
    format = '%d-%m-%Y'
    format2 = '%d.%m.%Y'
    format3 = '%Y-%m-%d'

    to_datetime =  lambda date, format: datetime.datetime.strptime(date, format) 
    to_date = lambda date, format: datetime.date.strftime(date, format) 
    to_str = lambda date, format: datetime.date.strftime(date, format) 
    
    def __init__(self,
            fuel_choices=fuel_choices, path=path, 
            report_rt=report_rt, registry_rt=registry_rt,
            report_jet=report_jet, registry_jet=registry_jet,
            select_fuel=select_fuel, format=format, format2=format2
        ):
        
        #### *** ---> select path from widget <--- *** ##### 
        self.path = path

        # initialize report depending on type of fuel
        self.fuel_choices = fuel_choices
        self.select_fuel = select_fuel
        self.items = dict([])
        # correct input conditions
        fuel_selected = select_fuel in fuel_choices
        blanc_input = len(select_fuel) < 1 or None

        try:
            self.registry = None
            self.report = None

            if blanc_input:
                raise TypeError

            if not fuel_selected:
                raise ValueError
            # 
            self.registry = registry_rt if select_fuel=='RT' else registry_jet
            self.report = report_rt if select_fuel=='RT' else report_jet

        except TypeError:
            print('Fuel selection shoudn\'t be blanc!')
        except ValueError:
            print('The fuel U\'ve  selected are not in the list!')
        except Exception as err3:
            print('Something went wrong. Try to relaunch the application')
        finally:
            exit() if self.registry is None or self.report is None else True
        print(self.registry, self.report + ' - This is ok: registry & report')

        # initialize date of report
        # this date is converted to satisfy needs of LibreOffice date format
        try:
            self.date = None
            date = input('Please select the date of report, use DD-MM-YYYY format: ')

            # correct date conditions
            blanc_input = len(date) < 1 or None

            if blanc_input:
                raise TypeError
            
            # from <str> to <'datetime.datetime'>
            date = ParseXLSXData.to_datetime(date, self.format)
            today = datetime.datetime.today()
            
            date_in_range = date < today
            if not date_in_range:
                raise AttributeError
            
            self.date = date
            self.today = today

        except TypeError:
            print('Date selection shoudn\'t be blanc!')
        except ValueError:
            print('Please enter date in the correct format: YYYY-MM-dd')
        except AttributeError:
            print('Date is out of range')
        except Exception as err3:
            print('Something went wrong. Try to relaunch the application')
        finally:
            exit() if self.date is None else True
        
        print(f'{self.date} - This is ok: date')

    def load_file_initial(self):
        '''
            accessing & loading the initial RT/JET A-1 fuel data \n\
            file from already created MS Excel file
            :returns: loaded MS Excel object for registry RT fuel
        '''
        try:
            reestr_xlsx_file = Path(
                self.path,
                self.registry
                )
            reestr_obj = open.load_workbook(reestr_xlsx_file)
            print('INITIAL File was loaded')
            return reestr_obj
        except InvalidFileException as err:
            reestr_xlsx_file = None
            print(f'{err}: {self: registry}')
        finally:
            exit() if reestr_xlsx_file is None else reestr_obj
            
    def activate_sheet_initial(self):
        '''
            activate the initial Jet fuel data sheet
            :returns: active MS Excel sheet for registry RT fuel
        '''
        registry_sheet = self.load_file_initial().active
        print('Initial sheet was activated')
        return registry_sheet

    def load_file_final(self):
        '''
            accessing & loading final RT/JET A-1 fuel data file
            :returns: active MS Excel sheet for report JET fuel
        '''
        try:
            oblik_xlsx_file = Path(
                self.path,
                self.report
                )
                
            oblik_obj = open.load_workbook(oblik_xlsx_file)
            print('Final File was loaded')
            return oblik_obj
        except InvalidFileException as err:
            oblik_xlsx_file = None
            print(f'{err}: {self.report}')
        finally:
            exit() if oblik_xlsx_file is None else oblik_obj
    
    def activate_sheet_final(self, file_final=None):
        '''
            activate the fuel data sheet
            :returns: loaded MS Excel object for fuel registry
        '''
        try:
            if not isinstance(file_final, Workbook):
                file_final = None
                raise TypeError
            report_sheet = self.load_file_final().active
            print('Final sheet was activated')
            return report_sheet
        except TypeError:
            'U should select a proper REPORT file'
        finally:
            exit() if file_final is None else report_sheet

    def check_amounts_equal(self, work_book_final):
        # adjustable: fields that should be compared
        start_rec = 5
        finish_rec = 20
        
        oblik_sheet = work_book_final.active

        recorded_value = 0
        
        for i in range(start_rec, finish_rec +1):
            condition = oblik_sheet[f'E{i}'].value != None
            if condition:
                recorded_value += oblik_sheet[f'E{i}'].value
        
        daily_amount = self.get_daily_amount()
        if not daily_amount==recorded_value:
            self.clean_fields(work_book_final)
            diff = daily_amount - recorded_value
            print( 
                'Daily amount not equals recorded value \n'  + 
                f'Difference: {diff} kg. Check REPORT fields' 
            )
            exit()
        return

    def check_key_mistakes(self, work_book_final):
        registry_sheet = self.activate_sheet_initial()
        
        a = set(i for i in 'osagau chemicals')
        b = set(i for i in 'osagau сhemicals')
        print(a, b)
        
        ## check fields for mistakes
        for i in range(1, len(registry_sheet['L'])+1):
            ## add filter by date -->

            condition = registry_sheet[f'L{i}'].value != None
            if not condition:
                continue
            cell = registry_sheet[f'L{i}']
            ### add for each letters
            mistakes = [f'mistake #{i}:, cell: {cell}, symbol {cell.value}' for value in cell.value if not cell.value in string.ascii_letters] 
            print(mistakes)

    def clean_fields(self, work_book):
        '''
            Clean cell values in working column E filled from a previous day 
            :returns: loaded MS Excel object with cleaned cells of the REPORT File
        '''
        # oblik_obj = self.load_file_final()
        # oblik_sheet = oblik_obj.active
        
        oblik_sheet = work_book.active

        for i in range(1, len(oblik_sheet['E'])+1):
            cell = oblik_sheet[f'E{i}']
            condition = isinstance(cell, Cell)
            if condition:
                cell.value = None
            else:
                continue
            
        work_book.save(self.report)
        print('Columns of the report has been cleaned')

    def read_cells(self, work_book_initial):
        '''
            Fulfill nested values dict with one or more different values (kgs)
            associated with a carrier - key
            :returns: loaded MS Excel object for fuel registry
            .. note::
                Intermediate parameters:
                * :param condition: avoid errors when iterating blank
                   cells in A column
                * :param not_nones_cells: - avoid adding
                   Nones to nested dict values
                * :param filter_by_date_cells: - avoid iterating all
                   blank spots (cells) of the REGISTRY sheet
                * :param not_nones_cells: - avoid Nones in the list of values
        '''
        
        # registry_sheet = self.activate_sheet_initial()
        registry_sheet = work_book_initial.active
        # assighn nested cells as lists
        for i in range(1, len(registry_sheet['L'])+1):
            condition = registry_sheet[f'L{i}'].value != None
            if condition:
                self.items[registry_sheet[f'L{i}'].value.lower()] = []

        # iterate through reestr sheet cells & filter by the reports date
        for i in range(1, len(registry_sheet['A'])+1):

            # avoid errors when iterating blank fields
            condition = registry_sheet[f'A{i}'].value != None

            if condition:
                filter_by_date_cells = list(filter(lambda item: item.value == self.date, registry_sheet[i]))
            
                if any(filter_by_date_cells):
                    # disclusion of None entries to the list lists of values
                    not_nones_cells = registry_sheet[f'L{i}'].value != None and registry_sheet[f'F{i}'].value != None
                    self.items[registry_sheet[f'L{i}'].value.lower()].append(registry_sheet[f'F{i}'].value) if not_nones_cells else 0
        
        
        return self.items

    def add_amounts(self):
        '''
            Getting collected amount values of fuel in kgs from REGISTRY sheet by carrier
            :returns: dict with summed data: key - carrier, value - daily amount (kg)
            .. note::
                Intermediate parameters:
                * :add amounts: the same value counted through lC with get_daily_amount()
        '''

        daily_amount = 0
        for key, value in self.items.items():
            self.items[key] = sum(value)
            # daily_amount += sum(value)
        return self.items


    def write_cells(self, work_book_final):
        '''
            :stage1: writing fields E5-E22 using prapared dict of items with 'REPORT' 
            fields C5-C22 as keys
            :stage2: write matched by key values into cells through get from loop keys
            .. note::
                Intermediate parameters:
                * :param condition: - avoid exceptions when using blank cell.value as a key
                   in REPORT sheet
                * :param record_value: - value got from items if such exists and condition 
                   was satisfied
        '''
        # oblik_obj = self.load_file_final()
        # oblik_sheet = oblik_obj.active
        oblik_sheet = work_book_final.active

        i = 0
        for carrier_cell in oblik_sheet[f'C']:

            condition = carrier_cell.value is not None
            
            # get a value from prior items dict by key from REPORT sheet C column if the key matches
            record_value = self.items.get(str(carrier_cell.value).lower()) if condition else 0

            i += 1
            if record_value:
                oblik_sheet[f'E{i}'].value = record_value            
                work_book_final.save(self.report) # change this field to automatic     

    ## *** Fuel Arrived Field *** ##
    def input_fuel_arrival(self, work_book_final):
        '''
            Fuel supply recording during the day if any
            :returns REPORT sheet: save amount of fuel supply into appropriate cell
        '''
        # oblik_obj = self.load_file_final()
        # oblik_sheet = oblik_obj.active
        oblik_sheet = work_book_final.active

        fuel_arrived_obj = FuelArrivedField()
        fuel_arrived = fuel_arrived_obj.fuel_arrived
        setattr(self, 'fuel_arrived', fuel_arrived)
    
        i = 0
        for cell in oblik_sheet[f'C']:
            i += 1
            pattern = re.compile('Прибуток палива')
            # find appropriate cell condition to write daily fuel suppply 
            result = pattern.match(str(cell.value)) is not None
            if result:
                oblik_sheet[f'E{i}'].value = fuel_arrived 
                work_book_final.save(self.report)
        
    def date_report_record(self, work_book_final):
        '''
            Recording the date of REPORT into a date-cell header
            :returns REPORT sheet: saves <str> type date, format YYYY.MM.DD
             into B3 cell
        '''
        # oblik_obj = self.load_file_final()
        # oblik_sheet = oblik_obj.active
        oblik_sheet = work_book_final.active

        # date of the report header B3 cell
        try:
            # from 'datetime.datetime'> to <str>
            # date = datetime.date.strftime(self.date, '%d.%m.%Y')
            date = ParseXLSXData.to_str(self.date, self.format2)
            oblik_sheet[f'B{3}'].value = f'Дата: {date}'
            work_book_final.save(self.report) ## change this field to automatic

        except (TypeError, ValueError) as input_error:
            print(input_error)
    

    def previous_report_date(self):
        '''
            Get date of the previous DAY REPORT
            :returns prev_rep_date: <str> type date, format YYYY-MM-DD
        '''
        prev_rep_date = self.date - datetime.timedelta(days=1)
        prev_rep_date = datetime.date.strftime(prev_rep_date, self.format3)
        return prev_rep_date

    
    def get_daily_amount(self):
        '''
            Get fuel daily fuel consumption for all carriers (kg)
            :returns: <int> daily_anount
        '''
        daily_amount = sum([i for i in self.items.values()])
        print(daily_amount)
        return daily_amount

    ## *** FUEL RESIDUE FIELD *** ##
    def get_fuel_residue(self, work_book_final):
        '''
            Get up-to-date fuel residue calculation (at the end of a previous report
            date), through the UI widget
            :returns REPORT sheet: saves <str> type date, format YYYY.MM.DD to E23/E26 fields
            .. note::
                Intermediate parameters:
                * :param residue_today - final fuel amount for all carriers
                  including supply & consumtion in (kg)
        '''
        # oblik_obj = self.load_file_final()
        # oblik_sheet = oblik_obj.active
        oblik_sheet = work_book_final.active

        # get previous report date
        prev_rep_date = self.previous_report_date()

        fuel_residue_obj = FuelResidueField(prev_rep_date)
        fuel_residue = fuel_residue_obj.fuel_residue

        # this attr would be used afterwards for another 
        # functionality
        setattr(self, 'fuel_residue', fuel_residue)
        
        # E23
        daily_amount = self.get_daily_amount()
        
        # E26
        residue_today = self.fuel_residue + self.fuel_arrived - daily_amount

        # parsing the REPORT sheet for appropriate cell names
        pattern1 = re.compile('Всього видано на пероні')
        pattern2 = re.compile('Залишок на складі ПММ')
        
        i = 0
        for cell in oblik_sheet[f'C']:
            i += 1
            search1 = pattern1.match(str(cell.value)) is not None
            search2 = pattern2.match(str(cell.value)) is not None

            if search1:
                # E23 field
                oblik_sheet[f'E{i}'].value = daily_amount
                oblik_obj.save(self.report)

            if search2:
                # E26 field
                oblik_sheet[f'E{i}'].value = residue_today
                work_book_final.save(self.report)

        print('The report has been done')
    
    def submain(self):
        # open INITIAL File
        file_initial =  LoadXLSXFileField(
            self.path,
            self.registry
        )
        
        # load INITIAL File
        work_book_initial = file_initial.get_work_book()

        # print(type(work_book_initial))
        # print(type(sheet_initial))
        
        # open FINAL File

        file_final =  LoadXLSXFileField(
            self.path,
            self.report
        )

        # load FINAL File
        work_book_final = file_final.get_work_book()

        # cleaning fields for final file
        self.clean_fields(work_book_final)
        
        # read cells from INITIAL File & collect data
        self.read_cells(work_book_initial)
        #print(self.items) +++
        self.add_amounts()
        print(self.items)
        self.write_cells(work_book_final)
        self.input_fuel_arrival(work_book_final)
        self.check_amounts_equal(work_book_final)
        self.date_report_record(work_book_final)
        self.get_fuel_residue(work_book_final)
        
        
        


'''
    Initial File was loaded
    Final File was loaded
    <class 'openpyxl.workbook.workbook.Workbook'>
    Final File was loaded
    <class 'openpyxl.worksheet.worksheet.Worksheet'>
    Final sheet was activated
'''

        
if __name__ == "__main__":

    instance = ParseXLSXData()
    instance.submain()
    
    # instance = ParseXLSXData()

    # # open INITIAL File
    # file_initial =  LoadXLSXFileField(instance.path, instance.registry)
    
    # # load INITIAL File
    # work_book_initial = file_initial.get_work_book()
    # # activate INITIAL File
    # sheet_initial = file_initial.activate_work_book()
    
    # print(type(work_book_initial))
    # print(type(sheet_initial))
    
    # # open FINAL File
    # file_final =  LoadXLSXFileField(instance.path, instance.report)

    # # load FINAL File
    # work_book_final = file_final.get_work_book()
    # # activate FINAL File
    # sheet_final = file_final.activate_work_book()

    # print(type(work_book_final))
    # print(type(sheet_final))


    # ### *** cleaning fields *** ###
    
    # instance.clean_fields(work_book_final, sheet_final)
    
    ## shift this to proceed
    # instance = ParseXLSXData()
    # print(instance.path)
    # print(self.path)
    # print(instance.report)
    # print(self.report)

    # file_initial =  LoadXLSXFileField(instance.path, instance.registry)
    # # print(file_initial.__dict__)

    # # # load INITIAL File
    # work_book_initial = file_initial.get_work_book()
    # print(work_book_initial)
    # # # activate INITIAL File
    # sheet_initial = file_initial.activate_work_book()
    # print(sheet_initial)

    # print(type(work_book_initial))
    # print(type(sheet_initial))
    
    

    ########## *** NOT REMOVE *** ###########
    #instance.load_file_initial()
    #instance.load_file_final()
    #instance.clean_fields()
    # instance.read_cells()
    # instance.add_amounts()
    # instance.write_cells()
    # instance.input_fuel_arrival()
    # instance.date_report_record()
    # instance.get_fuel_residue()
    # instance.check_cells()
