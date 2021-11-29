from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage
from django.utils.translation import gettext as _

PROTECTED_MEDIA = getattr(settings, 'PROTECTED_MEDIA', None)

conf_error = PROTECTED_MEDIA == None
if conf_error:
    raise   ImproperlyConfigured('PROTECTED_MEDIA is not set in settings.py')

# if conf_error:
#     raise   ImproperlyConfigured(_('PROTECTED_MEDIA is not set in seetings.py'), code='invalid')

# django-storages class
class ProtectedStorage(FileSystemStorage):
    '''
        Changing the default file system storage
        FileSystemStorage: is what media root is typically
    '''
    # media root location   
    location  = PROTECTED_MEDIA 
