
from rest_framework.generics import GenericAPIView

class GoogleAuthAPIView(GenericAPIView):
    
    '''
    delattr() method deletes an attribute from the object 
    (if the object allows it).
    
    delattr(name) - takes 1 parameter name
    :param name: string which is the name of the attr to be
                 removed from the object
    :param user: object whose attributes r for instance:
    
    {'_state': <django.db.models.base.ModelState object at 0x7f45c10d8b20>,
        'id': 1, 'last_login': datetime.datetime(2022, 6, 14, 16, 5, 24, 82709,
        tzinfo=<UTC>), 'is_superuser': True, 'first_name': 'Andrew', 
        'last_name': 'Proniuk', 'is_staff': True, 'is_active': True,
        'date_joined': datetime.datetime(2021, 11, 1, 18, 50, 45, tzinfo=<UTC>),
        'email': 'andriyproniyk@gmail.com', 'username': 'NetUnit',
        'password': 'pbkdf2_sha256$216000$hmA9lsNhktQm$hzaE4Zm1MRpprkVIVFAfjU=',
        'image': 'media/accounts/AVA.jpg', 'media': 'protected/accounts/AVA.jpg', 
        '_access_token_key': '787326616955457536-i6o6R96LVT8A52cXZLXhCUIvWPnyXJN', 
        '_access_token_secret': 'htO2gWkZUyH4lWYBHpC5tbkM8O0Sb3xXos78vZIqmarrn'
    }
    
    :param serializer_class: serializer to convert appropriate data into json
    :param excessive_fields: fields to be deleted before serialized

    :type user: <class 'CustomUser'>, model instance
    :type serializer_class: <class 'accounts.api.serializers.GoogleAuthSerializer'>
    :type excessive_fields: <class 'list'>

    .. note:: 
        delattr() doesn't return any value (returns None).
        It only removes an attribute (if the object allows it).
    '''

    serializer_class = GoogleSocialAuthSerializer
    # renderer_classes = [TemplateHTMLRenderer, template]
    excessive_fields = [
        '_state', 'last_login', 'password', 'auth_token',
        '_access_token_key', '_access_token_secret'
    ]

    def remove_excessive_fields(self, user):
        fields = user.__dict__.keys()
        exc = self.excessive_fields
        [user.__delattr__(field) for field in exc if field in fields]
        user_data = user.__dict__
        return user_data

# obtained user data to serialize without excessive fields
# >>> {'id': 1, 'is_superuser': True, 'first_name': 'Andrew',
#           'last_name': 'Proniuk', 'is_staff': True, 
#           'is_active': True, 'date_joined': datetime.datetime(2021, 11, 1, 18, 50, 45,
#            tzinfo=<UTC>), 'email': 'andriyproniyk@gmail.com, 'username': 'NetUnit', 
#           'image': 'media/accounts/AVA.jpg', 'media': 'protected/accounts/AVA.jpg'
# }
