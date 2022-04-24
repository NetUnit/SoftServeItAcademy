import pathlib
from mimetypes import guess_type
import xlwt
from pathlib import Path
from openpyxl.utils.exceptions import (
    InvalidFileException
)
import re
import string

class FuelSupplyField:
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
    error = None
    
    def __init__(self, **fields):
        try:
            # fields validation
            for field in fields.items():
                if not isinstance(field[1], (int, float)) and not field[1].isdigit():
                    field_error = f"{field[0].capitalize()} - \"{field[1]}\""
                    raise ValueError()

                self.__setattr__(field[0], int(field[1]))

        except (TypeError, AttributeError):
            self.error = self.msg
        except ValueError:
            form_name = self.__class__.__name__
            self.error = f"{self.get_classname(form_name)}: {field_error}  \n" \
                + f"{self.msg2}"
            
    @staticmethod
    def get_classname(field_name):
        field_name = ' '.join(
            re.findall(
                '[A-Z][^A-Z]*',
                field_name
            )
        ).capitalize()
        return field_name