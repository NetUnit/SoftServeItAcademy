import pathlib
from mimetypes import guess_type
import xlwt
from pathlib import Path
from openpyxl.utils.exceptions import (
    InvalidFileException
)
import os
import openpyxl as open


class LoadXLSXFileField:
    '''
        ===========================================================
        This class represents a 'Loading XLSL File Widget'
        ===========================================================
        Attrs:
            :param path: path to REGISTRY & REPORT files
            :type path: <str>
            :param document: file names
            :type document: <str>
            :param type_error: error coomon for this class field
    '''
    type_error = 'Improper file extension selected'
    empty_file = 'U should select some file'
    extensions  = [
        '.xls', '.xlsx', '.xlsm','.xlsb',
        '.xltx', '.xlt', '.xltm', '.xml',
        '.xlam', '.xla', '.xlw', '.xlr',
        '.ods', '.ots', '.fods', '.uos'
    ]
    err = None

    def __init__(self, path=None, file_name=None):
        try:
            self.path = path
            self.file_name = file_name
            
            # validate
            self.validate_file()
        
            xlsx_file = Path(
                path,
                file_name
                )
            self.xlsx_file = xlsx_file
            # self.msg = f'File was opened: {file_name}'
            # print(self.msg)

        except TypeError:
            self.xlsx_file = None
            # self.err = f'{self.type_error}: file - {file_name}'

    def validate_file(self):
        '''
            accessing & validating pathes of xlsx files \n\
            :returns: loaded MS Excel object for REGISTRY/REPORT
            :raises: TypeError if file ext is different from xlsx format

            .. note::
                * :param full_path: assigned for a case of path equals dirname
                * :param path: assigned for a case of full path of file
                File FINAL is used as a REPORT filee
        '''
        path = pathlib.Path(self.path)
        full_path = os.path.join(self.path + '/' + self.file_name)
        full_path = pathlib.Path(full_path)

        # get file extension
        ext = path.suffix if len(path.suffix) > 0 else full_path.suffix

        empty_file = None in [self.path, self.file_name]
        if empty_file:
            msg = self.empty_file

        improper_file = ext not in self.extensions
        if improper_file:
            msg = self.empty_file

        if any([empty_file, improper_file]):
            print(type(self.file_name))
            self.file_name = 'None' if self.file_name == '' else self.file_name
            self.err = f'{msg}: file - {self.file_name}'
            # LOGGER.error(self.err)
            raise TypeError()

    def get_work_book(self):
        '''
            accessing & loading the INITIAL/FINAL RT/JET A-1 fuel data \n\
            file from already created MS Excel file
            :returns: loaded MS Excel object for REGISTRY/REPORT
            :ctaches: InvalidFileException if corrupt or damaged file 
        '''
        try:
            work_book = open.load_workbook(self.xlsx_file)
            # print(f'Workbook was loaded: {work_book}')
            return work_book
        except InvalidFileException as err:
            self.work_book = None
            self.err = f'{err}: {self.file_name}'
            # LOGGER.error(self.msg)
            print(self.msg)
