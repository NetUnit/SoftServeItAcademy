import copy
from os import write

# openpyxl lib
import openpyxl as open
# path lib
from pathlib import Path
from openpyxl.cell.cell import MergedCell, Cell

import string
import datetime
import re

from openpyxl.utils.exceptions import (
    InvalidFileException
)

from openpyxl import (
    Workbook,
)

from validators.file_field import LoadXLSXFileField

from validators.supply_input_fields import (
    FuelArrivedField,
    FuelResidueField,
    FuelPickupField
)


class ParseXLSXData:
    '''
    ===========================================================
    This class represents the Application Core parser
    ===========================================================
    Attrs:
        :param fuel_choices: for launching report from terminal
        :param fuel_choices: list
        :param path: carrier register & final report files folder
        :type path: str
        :param registry_rt: name of xlsx file for RT grade of fuel
        :type registry_rt: str
        :param registry_jet: name of xlsx file for JET A-1 grade of fuel
        :type registry_jet: str
        :param  select_fuel: fuel type selection depending upon type
        :type select_fuel: str
        :param format: dd-mm-yyyy Yoda time format
        :type format: str
        :param date: date of the following report to be done
        :type date: str, None - by default
        :param fuel_arrival: sets value of the fuel_arrived
        :type fuel_arrival: int
        :param fuel_pickup: sets value of the fuel uploaded into trucks
        :type fuel_arrived: int
        :param fuel_residue: sets value of the fuel remain at the facilities
        :type fuel_arrived: int
        :param today: get todays time
        :type today: datetime.date

    .. note::
        File INITIAL is used as a REGISTER file
        File FINAL is used as a REPORT file

        Intermediate parameters:
            * :param registry: INITIAL XLSX FILE TO PARSE
            * :param report: INITIAL XLSX FILE TO SAVE REPORT
            * :param items:  aims to store/retrieve/sum data values
               parsed from xlsx file

        Other 3 paramaters are lambda functions and called when necessary
            * :param to_datetime: from <str> to <'datetime.datetime'>
            * :param to_date: from <str> to <'datetime.date'>
            * :param to_str: from 'datetime.datetime'> to str
            * :param items: dict of pairs: key - carrier, value - amounts list
            keys - created automatically from the list of carriers
            values - fuel amounts (kg), multiple values associated with a key
            * :type items: dict

    .. note::
        This class represents behaviour that parses registry RT.xlsx &
        registry JET A-1.xlsx, get, convert and record data cells to
        report files report RT.xlsx & report JET A-1.xlsx files
    '''
    fuel_choices = ['RT', 'Jet A-1']

    path = '/media/netunit/storage/SoftServeItAcademy/' \
        + 'airport_petty_algorithms/carrier_register_li'
    path_reserve = '/home/rostyslav/Общедоступные/temp_andrii/' \
        + 'SoftServeItAcademy/airport_petty_algorithms/carrier_register_li'

    # RT fuel type filenames:
    registry_rt = 'Реєстр Укртатнафта РТ.xlsx'
    report_rt = 'Звіт РТ.xlsx'

    # Jet A-1 fuel type filenames:
    registry_jet = 'Реєстр Укртатнафта Jet A-1.xlsx'
    report_jet = 'Звіт Jet A-1.xlsx'

    format = '%d-%m-%Y'
    format2 = '%d.%m.%Y'
    format3 = '%Y-%m-%d'

    date = None
    to_datetime = lambda date, format: datetime.datetime.strptime(date, format)
    to_date = lambda date, format: datetime.date.strftime(date, format)
    to_str = lambda date, format: datetime.date.strftime(date, format)

    def __init__(
        self, path_initial=None, path_final=None, file_initial=None,
        file_final=None, select_fuel=None, date=None, fuel_arrival=None,
        fuel_pickup=None, fuel_residue=None
    ):

        self.path_initial = self.path if path_initial is None else path_initial
        self.path_final = self.path if path_final is None else path_final

        # initialize report depending on type of fuel
        if select_fuel is None:
            select_fuel = input(
                'Please select type of fuel U want to make a report of: '
            )

        self.select_fuel = select_fuel
        self.items = dict([])

        # correct input conditions
        fuel_selected = select_fuel in self.fuel_choices
        blanc_input = len(select_fuel) < 1 or None

        try:
            if blanc_input:
                raise TypeError

            if not fuel_selected:
                raise ValueError

            self.file_initial = self.registry_rt if select_fuel == 'RT' else self.registry_jet
            self.file_final = self.report_rt if select_fuel == 'RT' else self.report_jet

            self.registry = self.file_initial
            self.report = self.file_final

            self.fuel_arrival = fuel_arrival
            self.fuel_pickup = fuel_pickup
            self.fuel_residue = fuel_residue

        except TypeError:
            print('Fuel selection shoudn\'t be blanc!')
        except ValueError:
            print('The fuel U\'ve  selected are not in the list!')
        except Exception as err3:
            print('Something went wrong. Try to relaunch the application')
        finally:
            exit() if self.registry is None or self.report is None else True

        # initialize date of report
        # this date is converted to satisfy needs of LibreOffice date format
        try:
            if date is None:
                date = input(
                    'Please select the date of report, use DD-MM-YYYY format: '
                )
            # correct date conditions
            # admissible only for manual-input not date picker
            blanc_input = len(str(date)) < 1 or date is None

            if blanc_input:
                raise TypeError

            # check whteher the date belongs to <'datetime.date'>
            date_picker = isinstance(date, datetime.date)

            if date_picker:
                date = ParseXLSXData.to_str(date, self.format)

            # riases exception here if improper input, format!=self
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

    def load_file_initial(self):
        '''
            accessing & loading the INITIAL RT/JET A-1 fuel data \n\
            file from already created MS Excel file
            :returns: loaded MS Excel object for registry RT fuel
        '''
        try:
            reestr_xlsx_file = Path(
                self.path,
                self.registry
                )
            reestr_obj = open.load_workbook(reestr_xlsx_file)
            return reestr_obj
        except InvalidFileException as err:
            reestr_xlsx_file = None
            print(f'{err}: {self: registry}')
        finally:
            exit() if reestr_xlsx_file is None else reestr_obj

    def activate_sheet_initial(self):
        '''
            activate the INITIAL Jet fuel data sheet
            :returns: active MS Excel sheet for registry RT fuel
        '''
        registry_sheet = self.load_file_initial().active
        return registry_sheet

    def load_file_final(self):
        '''
            accessing & loading FINAL RT/JET A-1 fuel data file
            :returns: active MS Excel sheet for report JET fuel
        '''
        try:
            oblik_xlsx_file = Path(
                self.path,
                self.report
                )

            oblik_obj = open.load_workbook(oblik_xlsx_file)
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
            return report_sheet
        except TypeError:
            'U should select a proper REPORT file'
        finally:
            exit() if file_final is None else report_sheet

    def check_amounts_equal(self, work_book_final, sheet_final):
        '''
            parses the FINAL sheet with fuel records by carrier
            search for distinction by total value of fuel in REPORT cells &
            carrier value in INITIAL file
            :returns: clened MS Excel object for fuel REPORT when values don't
             match & exit from app
        '''
        # adjustable: fields that should be compared when check keys
        start_rec = 5
        finish_rec = 20
        recorded_value = 0

        for i in range(start_rec, finish_rec + 1):
            condition = sheet_final[f'E{i}'].value != None
            if condition:
                recorded_value += sheet_final[f'E{i}'].value

        daily_amount = self.get_daily_amount()
        if not daily_amount == recorded_value:
            self.clean_fields(work_book_final, sheet_final)
            diff = daily_amount - recorded_value
            print(
                'Daily amount not equals recorded value \n' +
                f'Difference: {diff} kg. Check REPORT fields'
            )
            exit()
        return

    def check_key_mistakes(self, work_book_initial):
        '''
            check INITIAL sheet carrier names for grammar mistakes or
            non-equalities
            :returns: printed messages when mistakes found
        '''
        sheet_initial = work_book_initial.active

        a = set(i for i in 'osagau chemicals')
        b = set(i for i in 'osagau сhemicals')
        print(a, b)

        # check fields for mistakes
        for i in range(1, len(sheet_initial['L']) + 1):
            condition = sheet_initial[f'L{i}'].value != None
            if not condition:
                continue
            cell = sheet_initial[f'L{i}']
            # add for each letters
            error = f'mistake #{i}:, cell: {cell}, symbol {cell.value}'
            letters = string.ascii_letters
            mistakes = [
                error for value in cell.value if cell.value not in letters
                ]
            print(mistakes)

    def clean_fields(self, work_book, sheet_final):
        '''
            Clean cell values in working column E filled from a previous day
            :returns: loaded MS Excel object with cleaned cells of the REPORT File
        '''
        for i in range(1, len(sheet_final['E']) + 1):
            cell = sheet_final[f'E{i}']
            condition = isinstance(cell, Cell)
            if condition:
                cell.value = None
            else:
                continue

        work_book.save(self.report)
        # LOGGER.info('Columns of the report has been cleaned')
        # print('Columns of the report has been cleaned')

    def read_cells(self, work_book_initial, sheet_initial):
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
        for i in range(1, len(sheet_initial['L']) + 1):
            condition = sheet_initial[f'L{i}'].value != None
            if condition:
                self.items[sheet_initial[f'L{i}'].value.lower()] = []

        # iterate through reestr sheet cells & filter by the reports date
        for i in range(1, len(sheet_initial['A'])+1):

            # avoid errors when iterating blank fields
            condition = sheet_initial[f'A{i}'].value != None

            if condition:
                filter_by_date_cells = list(
                    filter(
                        lambda item: item.value == self.date, sheet_initial[i]
                    )
                )

                if any(filter_by_date_cells):
                    # disclusion of None entries to the list lists of values
                    carrier = sheet_initial[f'L{i}'].value
                    fuel_amount = sheet_initial[f'L{i}'].value
                    not_nones_cells = carrier != None and fuel_amount != None
                    self.items[
                        sheet_initial[f'L{i}'].value.lower()
                    ].append(
                        sheet_initial[f'F{i}'].value
                    ) if not_nones_cells else 0
        return self.items

    def add_amounts(self):
        '''
            Getting collected amount values of fuel in kgs from REGISTRY
            sheet by carrier
            :returns: dict with summed data: key - carrier, value -
            daily amount (kg)
            .. note::
                Intermediate parameters:
                * :add amounts: the same value counted through lC with
                get_daily_amount()
        '''
        daily_amount = 0
        for key, value in self.items.items():
            self.items[key] = sum(value)
            # daily_amount += sum(value) # optional var
        return self.items

    def write_cells(self, work_book_final, sheet_final):
        '''
            :stage1: writing fields E5-E22 using prapared dict of items with
            'REPORT' fields C5-C22 as keys
            :stage2: write matched by key values into cells through get from
            loop keys
            .. note::
                Intermediate parameters:
                * :param condition: - avoid exceptions when using blank cell.value
                as a key the in REPORT sheet
                * :param record_value: - value got from items if such exists and
                condition was satisfied
        '''
        i = 0
        for carrier_cell in sheet_final[f'C']:

            condition = carrier_cell.value is not None

            # get a value from prior items dict by key from
            # REPORT sheet C column if the key matches
            record_value = self.items.get(
                str(carrier_cell.value).lower()
            ) if condition else 0

            i += 1
            if record_value:
                sheet_final[f'E{i}'].value = record_value
                # change this field to automatic
                work_book_final.save(self.report)

    def input_fuel_arrival(self, work_book_final, sheet_final):
        '''
            Fuel supply recording during the day if any
            :returns REPORT sheet: save amount of fuel supply into appropriate cell
        '''
        fuel_arrived_obj = FuelArrivedField() if self.fuel_arrival is None else False
        if fuel_arrived_obj is not False:
            self.fuel_arrival = fuel_arrived_obj.fuel_arrived

        i = 0
        for cell in sheet_final[f'C']:
            i += 1
            pattern = re.compile('Прибуток палива')
            # find appropriate cell condition to write daily fuel suppply
            result = pattern.match(str(cell.value)) is not None
            if result:
                sheet_final[f'E{i}'].value = self.fuel_arrival
                work_book_final.save(self.report)

    def date_report_record(self, work_book_final, sheet_final):
        '''
            Recording the date of REPORT into a date-cell header B3
            :returns REPORT sheet: saves <str> type date, format YYYY.MM.DD
             into B3 cell
        '''
        try:
            # from 'datetime.datetime'> to <str>
            date = ParseXLSXData.to_str(self.date, self.format2)
            sheet_final[f'B{3}'].value = f'Дата: {date}'
            # change this field to automatic later
            work_book_final.save(self.report)

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

    def get_fuel_residue(self, work_book_final, sheet_final):
        '''
            Get up-to-date fuel residue calculation (at the end of a previous
            report date), through the UI widget
            :returns REPORT sheet: saves <str> type date, format YYYY.MM.DD to
            E23/E26 fields
            .. note::
                Intermediate parameters:
                * :param residue_today - final fuel amount for all carriers
                  including supply & consumtion in (kg)
        '''
        # E22
        self.daily_amount = self.get_daily_amount()

        # E23
        fuel_pickup_obj = FuelPickupField() if self.fuel_pickup is None else False
        if fuel_pickup_obj is not False:
            self.fuel_pickup = fuel_pickup_obj.fuel_pickup

        # get previous report date
        prev_rep_date = self.previous_report_date()

        # E26
        fuel_residue_obj = FuelResidueField(
            prev_rep_date
        ) if self.fuel_residue is None else False

        if fuel_residue_obj is not False:
            self.fuel_residue = fuel_residue_obj.fuel_residue

        residue_today = self.fuel_residue + self.fuel_arrival
        - self.daily_amount - self.fuel_pickup

        # parsing the REPORT sheet for appropriate cell names
        pattern1 = re.compile('Всього видано на пероні')
        pattern2 = re.compile('Самовивозом зі складу ПММ')
        pattern3 = re.compile('Залишок на складі ПММ')

        i = 0
        for cell in sheet_final[f'C']:
            i += 1
            search1 = pattern1.match(str(cell.value)) is not None
            search2 = pattern2.match(str(cell.value)) is not None
            search3 = pattern3.match(str(cell.value)) is not None

            if search1:
                # E21 field
                sheet_final[f'E{i}'].value = self.daily_amount
                work_book_final.save(self.report)

            if search2:
                # E22 field
                sheet_final[f'E{i}'].value = self.fuel_pickup
                work_book_final.save(self.report)

            if search3:
                # E26 field
                sheet_final[f'E{i}'].value = residue_today
                work_book_final.save(self.report)

        # LOGGER.info(u'The report has been done')

    def submain(self):
        # open INITIAL File
        file_initial = LoadXLSXFileField(
            self.path_initial,
            self.registry
        )

        # load INITIAL File
        work_book_initial = file_initial.get_work_book()

        # open FINAL File
        file_final = LoadXLSXFileField(
            self.path_final,
            self.report
        )

        # load FINAL File
        work_book_final = file_final.get_work_book()

        # activate sheets
        sheet_final = work_book_final.active
        sheet_initial = work_book_initial.active

        # cleaning fields for final file
        self.clean_fields(work_book_final, sheet_final)

        # read cells from INITIAL File & collect data
        self.read_cells(work_book_initial, sheet_initial)
        self.add_amounts()
        self.write_cells(work_book_final, sheet_final)
        self.input_fuel_arrival(work_book_final, sheet_final)

        # check if total value in REPORT equals REGISTRY data
        # self.check_amounts_equal(work_book_final, sheet_final)

        self.date_report_record(work_book_final, sheet_final)
        self.get_fuel_residue(work_book_final, sheet_final)

if __name__ == "__main__":
    instance = ParseXLSXData()
    instance.submain()
