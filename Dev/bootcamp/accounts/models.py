from django.db import models
from django.db import models, IntegrityError, DataError
from django.http.response import Http404

# Create your models here.


class CustomUser(models.Model):
    # id = models.AutoField()
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200, blank=False)
    nickname = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('id',)

    # def __str__(self):
    #     '''
    #         Magic method is redefined to show all information about a Product
    #         :return: product id, product title, product title, product price
    #     '''
    #     return f'{self.email} {self.password}'

    def __repr__(self):
        '''
            This magic method is redefined to show class and id of product object.
            :return: class, id
        '''
        return f'{self.__class__.name}(id={self.id})'

    # def __del__(self):
	#     print('Got rid of the next params: %s %s' % (self.id, self._state ))

    @staticmethod
    def get_user_by_id(user_id=None):
        user = CustomUser.objects.get(pk=user_id)
        return user

    @staticmethod
    def get_all_users():
        all_users = CustomUser.objects.all()
        users_exist = len(user for user in all_users) > 0
        return all_users if users_exist else 0

    @staticmethod
    def delete_user_by_id(user_id=None):
        user = CustomUser.objects.all().filter(pk=user_id)
        user.delete() if user else 0

    # data here will be a dict(**kwargs from UI)
    def create_user(self, data=None):
        user = CustomUser.objects.create(data) if data != None else 0
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
    def get_user_by_nickname(nickname=None):
        '''
            This method is getting a user by it's nickname
            :return: user object via nickname
        '''
        try:
            user = CustomUser.objects.all().filter(nickname=nickname).get()
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
        '''
        # data is a dict that comes from form (cleaned_data)
        # dict has pairs of key-value
        # getting Value from the dict to match with the db

        # will return the query-object when match the Value from the form
        user_by_email = data.get('email')
        user_by_nickname = data.get('nickname')

        # qurying the db via data from the form (email, nickname)
        match_by_email = CustomUser.get_user_by_email(user_by_email)
        match_by_nickname = CustomUser.get_user_by_nickname(user_by_nickname)

        user_exists = bool(match_by_email) + bool(match_by_nickname) > 0
        return True if user_exists else False

    # def get_role_name(self):
    #     '''
    #         returns str role name
    #     '''
    #     return self.get_role_display()