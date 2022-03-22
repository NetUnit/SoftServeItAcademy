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
#import xlsxwriter
path_main = '/media/netunit/storage/SoftServeItAcademy/airport_petty_algorithms/carrier_register_li'
path_reserve = '/home/rostyslav/Общедоступные/temp_andrii/SoftServeItAcademy/airport_petty_algorithms/carrier_register_li'


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
        Other 3 paramaters are lambda functions and called when necessary
        :param to_datetime: from <str> to <'datetime.datetime'>
        :param to_date: from <str> to <'datetime.date'>
        :param to_str: from 'datetime.datetime'> to str

        :param items: dict of pairs: key - carrier, value - list of amounts
        keys - created automatically from the list of carriers
        values - fuel amounts (kg), multiple values associated with a key
        :type items: dict
        
        :param fuel_arrived: sets value of the fuel_arrived attribute with
        setattr() function
        :type fuel_arrived: int

        :param today: get todays time
        :type today: datetime.date

    .. note:: 
        This class represents behaviour that parses registry RT.xlsx & 
        registry JET A-1.xlsx, get, convert and record data cells to 
        report files report RT.xlsx & report JET A-1.xlsx files
    '''
    fuel_choices = ['RT', 'Jet A-1']
    
    path = '/home/rostyslav/Общедоступные/temp_andrii/SoftServeItAcademy/airport_petty_algorithms/carrier_register_li'
    
    # RT:
    registry_rt = 'Реєстр Укртатнафта РТ.xlsx'
    report_rt = 'Звіт РТ.xlsx'

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
        reestr_xlsx_file = Path(
            self.path,
            self.registry
            )
        reestr_obj = open.load_workbook(reestr_xlsx_file)
        return reestr_obj
            
    def activate_sheet_initial(self):
        '''
            activate the initial Jet fuel data sheet
            :returns: active MS Excel sheet for registry RT fuel
        '''
        registry_sheet = self.load_file_initial().active
        return registry_sheet

    def load_file_final(self):
        '''
            accessing & loading final Jet fuel data file
            :returns: active MS Excel sheet for report JET fuel
        '''
        oblik_xlsx_file = Path(
            self.path,
            self.report
            )
            
        oblik_obj = open.load_workbook(oblik_xlsx_file)
        return oblik_obj

    def activate_sheet_final(self):
        '''
            activate the fuel data sheet
            :returns: loaded MS Excel object for fuel registry
        '''
        report_sheet = self.load_file_final().active
        return report_sheet

    def check_cells(self):
        registry_sheet = self.activate_sheet_initial()
        
        a = set(i for i in 'osagau chemicals')
        b = set(i for i in 'osagau сhemicals')
        print(a, b)
        
        ## check fields for mistakes
        for i in range(1, len(registry_sheet['L'])+1):
            condition = registry_sheet[f'L{i}'].value != None
            if not condition:
                continue
            cell = registry_sheet[f'L{i}']
            ### add for each letters
            mistakes = [f'mistake #{i}:, cell: {cell}, symbol {cell.value}' for value in cell.value if not cell.value in string.ascii_letters] 
            print(mistakes)

    def clean_fields(self):
        '''
            Clean cell values in working column E filled from a previous day 
            :returns: loaded MS Excel object with cleaned cells of the REPORT File
        '''
        oblik_obj = self.load_file_final()
        oblik_sheet = oblik_obj.active

        for i in range(1, len(oblik_sheet['E'])+1):
            cell = oblik_sheet[f'E{i}']
            condition = isinstance(cell, Cell)
            if condition:
                cell.value = None
            else:
                continue
        
        oblik_obj.save(self.report)

    def read_cells(self):
        '''
            Fulfill nested values dict with one or more different values (kgs)
            associated with a carrier - key
            :returns: loaded MS Excel object for fuel registry

            .. note::
                Intermediate parameters:
                * :param condition: - avoid errors when iterating blank
                   cells in A column
                * :param not_nones_cells: - avoid adding
                   Nones to nested dict values
                * :param filter_by_date_cells: - avoid iterating all
                   blank spots (cells) of the REGISTRY sheet
                * :param not_nones_cells: - avoid Nones in the list of values
        '''
        
        registry_sheet = self.activate_sheet_initial()

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
        '''

        daily_amount = 0
        for key, value in self.items.items():
            self.items[key] = sum(value)
            daily_amount += sum(value)
        return self.items


    def write_cells(self):
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
        oblik_obj = self.load_file_final()
        oblik_sheet = oblik_obj.active

        i = 0
        for carrier_cell in oblik_sheet[f'C']:

            condition = carrier_cell.value is not None
            
            # get a value from prior items dict by key from REPORT sheet C column if the key matches
            record_value = self.items.get(str(carrier_cell.value).lower()) if condition else 0

            i += 1
            if record_value:
                oblik_sheet[f'E{i}'].value = record_value            
                oblik_obj.save(self.report) # change this field to automatic     

    def input_fuel_arrival(self):
        '''
            Fuel supply recording during the day if any
            :returns REPORT sheet: save amount of fuel supply into appropriate cell
        '''
        oblik_obj = self.load_file_final()
        oblik_sheet = oblik_obj.active
        
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
                oblik_obj.save(self.report)
        
    def date_report_record(self):
        '''
            Recording the date of REPORT into a date-cell header
            :returns REPORT sheet: saves <str> type date, format YYYY.MM.DD
             into B3 cell
        '''
        oblik_obj = self.load_file_final()
        oblik_sheet = oblik_obj.active
        
        # date of the report header B3 cell
        try:
            # from 'datetime.datetime'> to <str>
            # date = datetime.date.strftime(self.date, '%d.%m.%Y')
            date = ParseXLSXData.to_str(self.date, self.format2)
            oblik_sheet[f'B{3}'].value = f'Дата: {date}'
            oblik_obj.save(self.report) ## change this field to automatic
            
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
        return daily_amount

    def get_fuel_residue(self):
        '''
            Get up-to-date fuel residue calculation (at the end of a previous report
            date), through the UI widget
            :returns REPORT sheet: saves <str> type date, format YYYY.MM.DD to E23/E26 fields
            .. note::
                Intermediate parameters:
                * :param residue_today - final fuel amount for all carriers
                  including supply & consumtion in (kg)
        '''
        oblik_obj = self.load_file_final()
        oblik_sheet = oblik_obj.active

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
                oblik_obj.save(self.report)

        print('It\'s ok')
        
if __name__ == "__main__":
    instance = ParseXLSXData()
    instance.load_file_initial()
    instance.load_file_final()
    instance.clean_fields()
    instance.read_cells()
    instance.add_amounts()
    instance.write_cells()
    instance.input_fuel_arrival()
    instance.date_report_record()
    instance.get_fuel_residue()
    # instance.check_cells()

    def submain():
        pass