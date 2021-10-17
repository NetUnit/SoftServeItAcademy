from django.db import models
from django.db import models, IntegrityError, DataError
from django.http.response import Http404
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy
from django.shortcuts import get_object_or_404
# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self, email, password=None):
        '''
            Creates a user, email is set a username
            username field is excessive
        '''
        if not email:
            raise ValueError('Users  must have an email address:')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''
            Allows to create superuser with the given 
            email and password.
            install from terminal
        
        '''
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    # id = models.AutoField()
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    password = models.CharField(max_length=200, blank=False)
    nickname = models.CharField(max_length=200, blank=True)

    #username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = MyAccountManager()

    class Meta:
        ordering = ('id',)

    # def __str__(self):
    #     '''
    #         Magic method is redefined to show all information about a Product
    #         :return: product id, product title, product title, product price
    #     '''
    #     return f'{self.email} {self.password}'

    # def __repr__(self):
    #     '''
    #         This magic method is redefined to show class and id of product object.
    #         :return: class, id
    #     '''
    #     return f'{self.__class__.name}(id={self.id})'

    # def __del__(self):
	#     print('Got rid of the next params: %s %s' % (self.id, self._state ))

    @staticmethod
    def get_user_by_id(user_id=None):
        user = get_object_or_404(CustomUser, pk=user_id)
        return user

    @staticmethod
    def get_all_users():
        all_users = CustomUser.objects.all()
        users_exist = len(user for user in all_users) > 0
        return all_users if users_exist else 0

    @staticmethod
    def delete_user_by_id(user_id=None):
        user = get_object_or_404(CustomUser, pk=user_id)
        user.delete()

    # data here will be a dict(**kwargs from UI)
    def create_user(self, data):
        user = CustomUser.objects.create(**data) if data != None else 0
        user.set_password(user.password)
        user.save()
        return user

    # data here will be a dict(**kwargs from UI)
    @staticmethod
    def update_user_by_id(user_id, data=None):
        user = CustomUser.get_by_id(user_id)
        updated_user = user.__dict__.update(data)
        return updated_user

    # make api info from this
    def to_dict(self):
        '''
            :return: user email, user password, user nickname, user created_at, user is_active
            :Example:
            | {
            |   'email': John@Dillinger.yahoo.com,
            |   'nickname': 'Johny D',
            |   'name': 'John',
            |   'surname': 'Dillinger',
            | }
        '''

        fields = str(dict(self.__dict__.items()))
        index = fields.find('email') - 1
        result = '{' + f'{fields[index:]}'
        api_data = eval(result)
        return api_data

    # +++
    @staticmethod
    def get_user_by_email(email=None):
        '''
            This method is getting a user by it's email
            :return: user object via email
        '''
        try:
            user = CustomUser.objects.all().filter(email=email).get()
            # user = CustomUser.objects.get(email)
            return user
        except CustomUser.DoesNotExist:
            return False

    # +++
    @staticmethod
    def get_user_by_username(username=None):
        '''
            This method is getting a user by it's nickname
            :return: user object via nickname
        '''
        try:
            user = CustomUser.objects.all().filter(username=username).get()
            # user = CustomUser.objects.get(nickname)
            return user
        except CustomUser.DoesNotExist:
            return False

    # +++
    @staticmethod
    def user_exists(data):
        '''
            This method is redefined to check if user with 
            similar email/nickname is present in the db
            :return: True if user exists, False if opposite

            NOTE:   data is a dict that comes from form (cleaned_data)
                    dict has pairs of key-value
                    getting Value from the dict to match with the db
        '''
        # will return the query-object when match the Value from the form
        user_by_email = data.get('email')
        user_by_nickname = data.get('nickname')

        # qurying the db via data from the form (email, nickname)
        match_by_email = CustomUser.get_user_by_email(user_by_email)
        match_by_nickname = CustomUser.get_user_by_nickname(user_by_nickname)

        user_exists = bool(match_by_email) + bool(match_by_nickname) > 0
        return True if user_exists else False

    # in the case of AbstractBaseUser
    # def get_role_name(self):
    #     '''
    #         returns str role name
    #     '''
    #     return self.get_role_display()


