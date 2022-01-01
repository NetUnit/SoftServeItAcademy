from rest_framework import serializers
from products.models import Product
from django.utils.translation import gettext as _

################## ***  path imports *** ##################
import pathlib
from wsgiref.util import FileWrapper
import binascii
################## *** Files Related Imports ##################
from django.forms.fields import ImageField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from mimetypes import guess_type
import io
import uuid
import base64
import six
import uuid
import pickle
from io import BytesIO
import PIL

class CustomImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            #print(True)
            print(type(self.__dict__))
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

## make this field as ImageField
class TemporaryApiImageField(serializers.ImageField):
    '''
        Another self-built Django REST framework field for handling image-uploads
        through the raw post data. It is used to pass: "The submitted data was not
        a file. Check the encoding type on the form." Encodes temporary API image to 
        InMemoryUploadedFile type image.

        Heavily based on:
        https://programtalk.com/python-examples/django.core.files.uploadedfile.InMemoryUploadedFile/
    '''
    def __init__(self, obj=None):
        self.obj = obj
    
    def get_image_file(self):
        '''
            get image from API data and converts to bytes within <class 'django.core.files.base.File'>
            :returns type <class 'bytes'> from API object
        '''
        # converts to the file-like object
        # <class 'django.core.files.base.File'
        img = self.obj.image.file
        print(type(img))
        ## converts django.core.files.base.File <class 'bytes'>
        bytes_ = img.read()
        #print(bytes_)
        # data = request.data.get('image') # http://127.0.0.1:8000/media/media/products/creepy_bike_38pNNVf_QjOtmQc.jpg
        return bytes_

    def to_inmemory_upl_file(self):
        '''
            1) getting binary stream using the in-memory bytes buffer.
                In-memory binary streams are also available as BytesIO objects.
                BytesIO create file like object that operate on string data.
                BytesIO mimic a normal file, usually a faster option of processing files
                
            :converts: <class 'django.core.files.base.File' to <class '_io.BytesIO'>

            2) Collect data to create InMemoryUploadedFile
            :returns type <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        '''
        
        # 1) getting in-memory file-like object 
        # taking image bytes as attr
        bytes_ = self.get_image_file()
        img_io = io.BytesIO(bytes_)

        # 2) collect InMemoryUploadedFile attrs
        guessed_ = guess_type(self.obj.image.path)
        # print(self.obj.image.path)
        file_type = guessed_[0].split('/')
        ext = file_type[1]
        ext = "jpg" if ext == "jpeg" else ext
        #2 fieldname
        field_name = file_type[0]
        #3 name
        name = f'{str(uuid.uuid4())[:12]}.{ext}'
        #4 content_type
        content_type = guessed_[0]
        #5 size
        size = self.obj.image.size
        inm_upl_pict = InMemoryUploadedFile(
            file=img_io, field_name=field_name,
            name=name, content_type=content_type,
            size=size, charset=None
            )
        # print(type(inm_upl_pict))
        return inm_upl_pict

    def convert_image(self):
        img = self.obj.image
        # https://stackoverflow.com/questions/67244002/how-to-create-inmemoryuploadedfile-objects-proper-in-django
        pass
        

    def save(self, data=None):
        '''
            returns: new raw data that is assighned with uploaded image
        '''
        inm_upl_pict = self.to_inmemory_upl_file()
        data['image'] = inm_upl_pict
        return data

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

    # image = TemporaryApiImageField()

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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for field in self.Meta.required:
    #         self.fields[field].required = True
    

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title=value)
    #     if qs:
    #         print(qs)
    #         pass