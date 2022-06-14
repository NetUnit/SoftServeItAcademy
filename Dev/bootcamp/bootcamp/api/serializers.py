from rest_framework import serializers

# *** file fields *** #
from django.core.files.base import ContentFile
from mimetypes import guess_type
import io
import uuid
import base64
import six
import uuid
import pickle
from io import BytesIO

# *** path *** #
import pathlib


class CustomImageField(serializers.ImageField):
    """
    ===========================================================
    This class redefines out of a box ImageField for db record
    ===========================================================
    
    A Django REST framework field for handling image-uploads
    through the raw post data. It uses base64 for encoding &
    decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    Correspond to /api/products/<pk> url
    """
    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            parent_data = self.__dict__.get('parent')
            print(parent_data)
            obj = parent_data._args[0]
            media = obj.media
            media_path = media.path
            path = pathlib.Path(media_path)
            if not path.exists():
                raise Http404(_('The path isn\'t valid'))

            with open(path, 'rb') as file:
                # getting in-memory file-like object
                file_like = file.read()
                print(file_like)
                # Generate file name:
                # 12 characters are more than enough.
                file_name = str(uuid.uuid4())[:12]
                # Get the file name extension:
                file_extension = self.get_file_extension(data)
                complete_file_name = f'{file_name}.{file_extension}'
                data = ContentFile(file_like, name=complete_file_name)
                return data

    def get_file_extension(self, data):
        extension = guess_type(data)[0].split('/')[1]
        extension = "jpg" if extension == "jpeg" else extension
        return extension
