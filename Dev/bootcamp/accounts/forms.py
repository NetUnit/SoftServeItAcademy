from django.contrib import auth
from django.views import generic
from .models import CustomUser
from django import forms

from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm
)

from django.contrib.auth import get_user_model, authenticate
from django.forms import ValidationError, ModelForm
from django.utils.translation import gettext as _
import string


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1',
                  'password2', 'username',
                  'first_name', 'last_name',
                  'image', 'media')
        required = ('email', 'password1',
                    'password2', 'username')
        labels = {
            'email': 'Email',
            'username': 'Nickname',
            'first_name': 'Name',
            'last_name': 'Surname'
        }

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'type email..',
                    'class': 'form-control',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'placeholder': 'type password..1',
                    'class': "form-control",
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder': 'repeat the password..',
                    'class': "form-control",
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'type nickname..',
                    'class': "form-control",
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'type name..',
                    'class': "form-control",
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'type surname..',
                    'class': "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True


class LoginForm(AuthenticationForm):
    '''
    This form is redefined in order to convert out of a box
    username field to email field

    ..note::
        only email Authentication
        Inheritance from forms.ModelForm
        is a bad idea - ModelForm is validating
        as if U r trying to create a new User,
        causing the already exists failures.
    '''
    # could be used to username-email auth
    # email_username = forms.CharField(
    #     label = 'Email/Username',
    #     widget = forms.TextInput(
    #         attrs = {
    #             'class': "form-control",
    #             "placeholder": "email or username",
    #             }
    #         )
    #     )

    # setup email auth
    username = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                "placeholder": "email",
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "password here",
            }
        )
    )

    error_messages = {
        'invalid_login': _(
            'Authentication Failed, reasons: '
            'Incorrect password or %(username)s. '
            'Both fields may be case-sensitive. '
            'Check if the \'Caps Lock\' key  wasn\'t accidentally hit '
            '(*ﾟｰﾟ)ゞ'
        ),
        'inactive': _('This account is inactive.'),
    }

    def __init__(self, email=username, *args, **kwargs):
        super().__init__(*args, **kwargs)


CustomUser = get_user_model()


class CustomUserLoginForm(forms.Form):

    email_username = forms.CharField(
        label='Email/Nickname',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "placeholder": "type email or nickname",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "password here",
            }
        )
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

    def clean_username(self):
        email = self.cleaned_data.get('email')
        # thisIsMyUsername == thisismyusername
        # capitalization doesn't matter
        qs = CustomUser.objects.filter(username_iexact=email)
        if not qs.exists():
            msg = 'This is an invalid user'
            raise forms.ValidationError(_(msg), code='invalid')
        return email


class CustomUserUpdateForm(forms.Form):

    username = forms.CharField(
        label='Nickname',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "placeholder": "username",
            }
        )
    )

    old_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "old password",
            }
        )
    )

    password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "new password here",
            }
        )
    )

    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "new password again",
            }
        )
    )

    first_name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "change first_name",
            }
        )
    )

    last_name = forms.CharField(
        label='Lastname',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "change last_name",
            }
        )
    )

    image = forms.ImageField()
    media = forms.FileField()

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     old_password = self.cleaned_data.get('password')
    #     new_password1 = self.cleaned_data.get('password1')
    #     new_password2 = self.cleaned_data.get('password2')
    #     first_name = self.cleaned_data.get('first_name')
    #     last_name = self.cleaned_data.get('last_name')

    def clean_password(self):
        '''
        This method checks & sets up a new user password
        :returns: new password if user exists & ValidationError when vice versa
        '''
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Passwords don\'t match '), code='invalid')
        return password2

    def check_user(self, request, user_id=None):
        '''
        in the Form it's prohibited to assign the password as old password
        This method checks if the previous password is correct
        :returns: True if user object exists in the db
        :raises: ValidationError when opposite
        '''
        password = self.cleaned_data.get('old_password')
        email = CustomUser.get_user_by_id(user_id).email
        user = authenticate(request, username=email, password=password)
        if user is None:
            msg = 'Previous password is incorrect'
            raise ValidationError(_(msg), code='invalid')
        return True

    def password_validation(self, password):
        '''
        This method checks whether a password is relibale
        :returns: True if password is ok
        :raises: ValidationError when conditions not satisfied
        '''
        demand1 = any([i in string.ascii_lowercase for i in password])
        demand2 = any([i in string.ascii_uppercase for i in password])
        demand3 = any([i in string.digits for i in password])
        demand4 = any([i in string.punctuation for i in password])
        demand5 = [i in password for i in password].count(True) > 7
        result = (demand1, demand2, demand3, demand4, demand5)
        if result.count(True) != 5:
            raise ValidationError(_(
                'Password can’t be too similar to your other personal information. \n\
                Password must contain at least 8 characters. \n\
                Password can’t be a commonly used password. \n\
                Password can’t be entirely numeric. \n\
                Password should contain letters of lower and uppercase.'
                ), code='invalid')
        return True
