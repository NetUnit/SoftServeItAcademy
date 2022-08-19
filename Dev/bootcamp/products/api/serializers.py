from rest_framework import serializers
from rest_framework.exceptions import APIException

from products.models import Product
from django.utils.translation import gettext as _

# ***  path imports *** #
import pathlib
from wsgiref.util import FileWrapper
import binascii
# *** Files Related Imports #
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
from PIL import Image
from manufacturer.api.serializers import ManufacturerPostSerializer

from pathlib import Path
import os
from bootcamp.settings import MEDIA_ROOT

from bootcamp.api.exceptions import (
    CustomCharField,
    TitleDuplicationError,
    TitleAbsenceError
)


class CustomImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through
    the raw post data. It uses base64 for encoding and decoding the
    contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    Correspond to /api/products/<pk> url
    """

    def to_internal_value(self, data):
        # Check if data is a base64 string
        if isinstance(data, six.string_types):
            parent_data = self.__dict__.get('parent')

            obj = parent_data._args[0]
            image = obj.image
            image_path = image.path
            path = pathlib.Path(image_path)
            if not path.exists():
                raise Http404(_('The path isn\'t valid'))

            with open(path, 'rb') as file:
                # Generate file name:
                # 12 characters are more than enough
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


# make this field as ImageField
class TemporaryApiImageData(serializers.ImageField):
    '''
    Another self-built Django REST framework field for handling image-uploads
    through the raw post data. It is used to pass: "The submitted data was not
    a file. Check the encoding type on the form." Encodes temporary API image to
    InMemoryUploadedFile type image.

    Heavily based on:
    https://programtalk.com/python-examples/django.core.files.uploadedfile.InMemoryUploadedFile/
    Correspond to /api/products/product/<pk> url
    '''

    def __init__(self, obj=None, *args, **kwargs):
        self.obj = obj
        super().__init__(*args, **kwargs)
        # self.required = False

    def get_image_file(self):
        '''
        get image from API data and converts to bytes within <class 'django.core.files.base.File'>
        :returns type <class 'bytes'> from API object
        '''
        # converts to the file-like object
        # <class 'django.core.files.base.File'
        img = self.obj.image.file

        # converts django.core.files.base.File <class 'bytes'>
        bytes_ = img.read()
        return bytes_

    def get_content_type(self):
        guessed_ = guess_type(self.obj.image.path)
        file_type = guessed_[0].split('/')
        return file_type
        return guessed_[0]

    def get_file_extension(self):
        ext = self.get_content_type()[1]
        ext = "jpg" if ext == "jpeg" else ext
        return ext

    def to_inmemory_upl_file(self):
        '''
        1) getting binary stream using the in-memory bytes buffer.
            In-memory binary streams are also available as BytesIO objects.
            BytesIO create file like object that operate on string data.
            BytesIO mimic a normal file, usually a faster option of processing files

        :converts: <class 'django.core.files.base.File' to <class '_io.BytesIO'>

        2) Collect data to create InMemoryUploadedFile
        :returns: type <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>

        https://stackoverflow.com/questions/67244002/how-to-create
        -inmemoryuploadedfile-objects-proper-in-django
        '''

        # getting in-memory file-like object
        # taking image bytes as attr
        bytes_ = self.get_image_file()
        img_io = io.BytesIO(bytes_)

        # collect InMemoryUploadedFile attrs
        # 2 assign fieldname
        field_name = self.get_content_type()[0]

        # 3 name
        ext = self.get_file_extension()
        name = f'{str(uuid.uuid4())[:12]}.{ext}'

        # 4 content_type
        content_type = '/'.join(self.get_content_type())

        # 5 size
        size = self.obj.image.size

        # 7 implement convert_image() if want to resize pict
        inm_upl_pict = InMemoryUploadedFile(
            file=img_io, field_name=field_name,
            name=name, content_type=content_type,
            size=size, charset=None
        )
        return inm_upl_pict

    # def convert_image(self):
    #     img_bytes = self.get_image_file()
    #     img_pil = Image.open(io.BytesIO(img_bytes))
    #     # byte_array  = io.BytesIO(img_bytes).getvalue()
    #     new_image_io = io.BytesIO()
    #     # img_io.height = ''
    #     # img_io.width = ''
    #     # img.save(new_image_io, format=file_extension.upper())
    #     # convert
    #     # img_file = self.to_inmemory_upl_file()
    #     ext = self.get_file_extension()
    #     # h = self.get_desired_height()
    #     # w = self.get_desired_width()
    #     # (320, 320, 'png', <PIL.Image.Image image mode=RGB size=160x160 at 0x7F1A928AB850>)
    #     # k = h/(int(img_io.height/2)
    #     resized = img_pil.resize((int(img_pil.height/2), int(img_pil.width/2)))
    #     resized.save(new_image_io, format=ext)

    def save(self, data=None):
        '''
        :returns: new raw data that is assighned with uploaded image
        '''
        inm_upl_pict = self.to_inmemory_upl_file()
        data['image'] = inm_upl_pict
        return data


class ProductPostSerializer(serializers.ModelSerializer):
    '''
    Serializer does 2 main things:
        converts to JSON
        validate data passed

    :returns: current JSON data via GET & new via POST/PUT methods
    '''
    # work for url: api/products/<pk>
    # image = CustomImageField(
    #     max_length=None, use_url=True,
    #     )

    # work for url: api/products/product/<pk>
    image = TemporaryApiImageData(
        max_length=None,
        use_url=True,
        allow_empty_file=True,
    )

    manufacturers = ManufacturerPostSerializer(many=True, read_only=True)

    # corresponds to CustomCharField
    # allow_blank will promotes default_error_messages
    title = CustomCharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        max_length=42
    )

    class Meta:
        model = Product
        fields = [
            'pk', 'title',
            'content', 'price',
            'user', 'manufacturers',
            'image'
        ]

        # required fields
        required = ['title', 'manufacturers']

        # get to know!
        extra_kwargs = {
            'title': {
                'required': True, 'allow_blank': True, 'allow_null': False
            },
        }
        # alternative to required:
        # discludes fields from required fields
        read_only_fields = [
            'pk', 'user'
        ]

    def validate_title(self, value):
        '''
        :returns: validated title
        :raises: TitleDuplicationException when duplicate title
        '''
        # filter objects with input value of title
        qs = Product.objects.filter(title__iexact=value)
        # exclude object itself in order to post/put self instance data
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise TitleDuplicationError()
        return value

    # validate fields + get fields info
    def get_validation_exclusions(self):
        return super().validate(self.fields)


class ProductCreateSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(
        max_length=None, use_url=True,
        allow_empty_file=True
    )

    class Meta:
        model = Product
        fields = [
            'pk', 'title',
            'content', 'price',
            'image'
        ]

        read_only_fields = [
            'pk', 'user'
        ]

    def to_internal_value(self, data):
        '''
        Allows image field to upload files
        :returns: validated data uploaded to db
        '''
        return data

    def validate(self, data):
        self._kwargs["partial"] = True
        print(data)
        title = data.get('title')
        if not title:
            raise TitleAbsenceError()
        qs = Product.objects.filter(title__iexact=title)
        # exclude object itself in order to post/put self instance data
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise TitleDuplicationError()
        return super().validate(data)
