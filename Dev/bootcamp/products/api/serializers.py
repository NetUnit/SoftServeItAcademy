from rest_framework import serializers
from products.models import Product
from django.utils.translation import gettext as _
###### *** path imports *** ######
import pathlib
from wsgiref.util import FileWrapper
from mimetypes import guess_type
import binascii
from django.forms.fields import ImageField

class CustomImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid
        import pickle
        from io import BytesIO

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            #print(True)
            #print(self.__dict__)
            parent_data = self.__dict__.get('parent')
            obj = parent_data._args[0]
            media = obj.media
            # /media/netunit/storage/SoftServeItAcademy/Dev/bootcamp/cdn_test/protected/products/creepy_bike_0WMnA1W.png --> <class 'str'>
            media_path = media.path
            # /media/netunit/storage/SoftServeItAcademy/Dev/bootcamp/cdn_test/protected/products/creepy_bike_0WMnA1W.png --> <class 'pathlib.PosixPath'>
            path = pathlib.Path(media_path)
            if not path.exists():
                raise Http404(_('The path isn\'t valid'))
            
            with open(path, 'rb') as file:

                ## BytesIO - subclass - converts string like object to bytes
                ## file_like = BytesIO(b'this is a sample bytearray') -example

                ## <class '_io.BufferedReader'>
                # print(type(file))
                ## getting in-memory file-like object
                file_like = file.read()
                ## <class 'bytes'>
                # print(type(file_like))

                ###### *** check this later *** #####
                # ## Try to decode the file. Return validation error if it fails.
                # try:
                #     # decoded_file = base64.b64decode(file_like)
                #     decoded_file = self.decode_base64(data)
                #     print(decoded_file) ### -------
                # except (TypeError):
                #     print(False)
                #     self.fail('invalid_image')  
                #######################################

                # Generate file name:
                file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.                                              
                # Get the file name extension:
                file_extension = self.get_file_extension(data)
                print(f'{file_extension}: is file extension')

                complete_file_name = f'{file_name}.{file_extension}'
                print(complete_file_name)
                ## <class 'django.core.files.base.ContentFile'>
                #data = ContentFile(decoded_file, name=complete_file_name)
                data = ContentFile(file_like, name=complete_file_name)
                return data
                
                # return super(Base64ImageField, self).to_internal_value(data)


        #     # Check if the base64 string is in the "data:" format
        #     if 'data:' in data and ';base64,' in data:
        #         # Break out the header from the base64 content
        #         header, data = data.split(';base64,')

        #     # # Try to decode the file. Return validation error if it fails.
        #     # try:
        #     #     decoded_file = base64.b64decode(file)
        #     #     # decoded_file = self.decode_base64(data)
        #     #     print(decoded_file) ### -------
        #     # except (TypeError):
        #     #     print(False)
        #     #     self.fail('invalid_image')  

        #     # Generate file name:
        #     file_name = str(uuid.uuid4())[:15] # 12 characters are more than enough.
        #     # print(file_name) ## +++                                                   9dba55b5-12e
        #     # Get the file name extension:
        #     # file_extension = self.get_file_extension(file_name, decoded_file)
        #     file_extension = self.get_file_extension(data)
        #     #print(f'{file_extension}: is file extension')

        #     complete_file_name = "%s.%s" % (file_name, file_extension, )

        #     ## <class 'django.core.files.base.ContentFile'>
        #     # data = ContentFile(decoded_file, name=complete_file_name)
      
        # return super(Base64ImageField, self).to_internal_value(data)



    ######################################################################################
    ## *** cannot use a bytes pattern on a string-like object
    # def decode_base64(self, data, altchars=b'+/'):
    #     import re
    #     """Decode base64, padding being optional.

    #     :param data: Base64 data as an ASCII byte string
    #     :returns: The decoded byte string.

    #     """
    #     try:
    #         data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    #         missing_padding = len(data) % 4
    #         if missing_padding:
    #             data += b'='* (4 - missing_padding)
    #         return print(base64.b64decode(data, altchars))
    #     except Exception as err:
    #         print(err)
    #         pass

    ############################### *** file ext *** ################################################
    def get_file_extension(self, data):
        extension = guess_type(data)[0].split('/')[1]
        extension = "jpg" if extension == "jpeg" else extension
        return extension

        ## doesn't work check this out later
    # def get_file_extension(self, file_name, decoded_file):
    #     import imghdr

    #     extension = imghdr.what(file_name, decoded_file)
    #     # print(extension)
    #     extension = "jpg" if extension == "jpeg" else extension

    #     return extension
    #################################################################################################

class ProductPostSerializer(serializers.ModelSerializer):
    '''
        Serializer does 2 main things:
        :converts to JSON
        :validate data passed
    '''
    # activate for CustomImageField() serializer
    # image = CustomImageField(
    #     max_length=None, use_url=True,
    #     )

    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=True,
        use_url=True
        )

    class Meta:
        model = Product
        fields = [
            'pk', 'title',
            'content', 'price',
            'user', 'manufacturers',
            'image'
        ]

        # image, media - needs more advanced image serializers
        required = ['title', 'manufacturers']

        read_only_fields = [
            'pk', 'user'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True


    # def validate_title(self, value):
    #     qs = Product.objects.filter(title=value)
    #     if qs:
    #         print(qs)
    #         pass