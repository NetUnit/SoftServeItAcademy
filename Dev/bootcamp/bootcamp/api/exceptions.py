from rest_framework.exceptions import APIException
from django.utils.translation import gettext as _
from rest_framework.fields import CharField

class CustomCharField(CharField):
    '''
        :raises Bad Request:: throw Exception when blank title field
        ## works  for url: http://127.0.0.1:8000/api/products/pk
    '''
    default_error_messages = {
        'blank': _('This field may not be blank (・－・。)'),
        'max_length': _('Satisfy need of {max_length} characters (　・ˍ・)'),
        'min_length': _('Ensure this field has at least {min_length} characters (・ˍ・*)')
    }
    
class TitleDuplicationError(APIException):
    '''
        Custom error that is raised when
        the same title is already in the db
        :raises TitleDuplicationError: throw Exception when duplicate title

        ## works for url: http://127.0.0.1:8000/api/products/pk
    '''
    status_code = 400
    default_detail = _('Title Already Exists ┐(‘～` )┌')

class TitleAbsenceError(APIException):
    '''
        Custom error that is raised when
        the same title is already in the db
        :raises TitleAbsenceError: throw Exception when title is empty

        ## works for url: http://127.0.0.1:8000/api/products/pk
    '''
    status_code = 400
    default_detail = _('Title Shouldn\'t be empty ╮( ˘_˘ )╭')
