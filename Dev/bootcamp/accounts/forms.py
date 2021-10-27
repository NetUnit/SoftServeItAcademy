from django.views import generic
from .models import CustomUser
from django import forms

################################################################################################
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.forms import ValidationError
from django.utils.translation import gettext as _
import string

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1',
                  'password2', 'nickname',
                  'first_name', 'last_name'
                 )
        required = ('email', 'password1',
                    'password2', 'nickname'
                   )

        # hidden password input
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
            'nickname': forms.TextInput(
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
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

# function-based view authenticate ### not valid
class ModelLoginForm(forms.ModelForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
        required = ('username', 'password')

        labels = {
            'username': 'Email',
            'password': 'Password',
        }

        widgets = {
            #'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
            'username': forms.TextInput(attrs={'placeholder': 'type username..'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'type password..'}), 
        }

    def __init__(self, *args, **kwargs):
        super(ModelLoginForm, self).__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

## class-based view authenticate
class LoginForm(AuthenticationForm):

    '''
        This form is rederined in order to convert out of a box
        username field to email field

        NOTE:  only email Authentication
    '''

    # email_username = forms.CharField(
    #     label = 'Email/Username',
    #     widget = forms.TextInput(
    #         attrs = {
    #             'class': "form-control",
    #             "placeholder": "email or username",
    #             }
    #         )
    #     )
    
    username = forms.CharField(
        label = 'Email',
        widget = forms.EmailInput(
            attrs = {
                'class': "form-control",
                "placeholder": "email",
                }
            )
        )
    
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "id": "user-password",
                "placeholder": "password here",
            }
        )
    )

    def __init__(self, email = username, *args, **kwargs):
        super().__init__(*args, **kwargs)



class CustomUserUpdateForm(forms.Form):

    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(
            attrs = {
                'class': "form-control",
                "placeholder": "username",
                }
            )
        )

    old_password = forms.CharField(
        label = 'Current Password',
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "id": "user-password",
                "placeholder": "old password",
            }
        )
    )

    password1 = forms.CharField(
        label = 'New Password',
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "id": "user-password",
                "placeholder": "new password here",
            }
        )
    )

    password2 = forms.CharField(
        label = 'Repeat Password',
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "id": "user-password",
                "placeholder": "new password again",
            }
        )
    )

    first_name = forms.CharField(
        label = 'First Name',
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "id": "user-password",
                "placeholder": "change first_name",
            }
        )
    )

    last_name = forms.CharField(
        label = 'Lastname',
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "id": "user-password",
                "placeholder": "change last_name",
            }
        )
    )

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
            :returns: True if user object exists in the db, ValidationError when vice versa
        '''
        password = self.cleaned_data.get("old_password")
        email =  CustomUser.get_user_by_id(user_id).email
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise ValidationError(_('Previous password is incorrect '), code='invalid')
        return True

    def password_validation(self, password):
        '''
            This method checks whether a password is relibale
            :returns: True if password is ok & ValidationError when conditions not satisfied
        '''
        demand1 = any([i in string.ascii_lowercase for i in password])  
        demand2 = any([i in string.ascii_uppercase for i in password])  
        demand3 = any([i in string.digits for i in password])         
        demand4 = any([i in string.punctuation for i in password])     
        demand5 = [i in password for i in password].count(True) > 7  
        result = (demand1, demand2, demand3, demand4, demand5)
        if result.count(True) != 5:
            raise  ValidationError(_(
                'Password can’t be too similar to your other personal information. \n\
                Password must contain at least 8 characters. \n\
                Password can’t be a commonly used password. \n\
                Password can’t be entirely numeric. \n\
                Password should contain letters of lower and uppercase.'
                ), code='invalid')
        return True
        
################################################################################################
# class CustomUserCreationForm(forms.ModelForm):
    
#     # will provoke error - change to forms.Form
#     # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password', 'nickname', 'name', 'surname')
#         required = ('email', 'password', 'nickname')

#         # hidden password input
#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'type password..'}),
#             'nickname': forms.TextInput(attrs={'placeholder': 'type nickname..'}),
#             'name': forms.TextInput(attrs={'placeholder': 'type name..'}),
#             'surname': forms.TextInput(attrs={'placeholder': 'type surname..'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)

#         for field in self.Meta.required:
#             self.fields[field].required = True

# # redefine the class, deprive from required fields

# class CustomUserLoginForm(CustomUserCreationForm):

#     def __init__(self, *args, **kwargs):
#         super(CustomUserLoginForm, self).__init__(*args, **kwargs)

#         for field in self.Meta.required:
#             if field == 'email' or field == 'password':
#                 self.fields[field].required = True
#             else:
#                 self.fields[field].required = False

##################################################################################################


# class UserLoginForm(CustomUserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password', 'nickname', 'name', 'surname')
#         required = ('email', 'password')


#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'type password..'}), 
#         }

#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)

#         for field in self.Meta.required:
#             self.fields[field].required = True


# class CustomUserCreationForm(forms.ModelForm):

#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:

#         model = CustomUser
#         fields = ('email', 'password', 'nickname', 'name', 'surname')
#         labels = { 'email': 'Email',
#                     'password': 'password',
#                     'nickname': 'nickname',
#                     'name': 'name',
#                     'surname': 'surname'
#                 }

#         required = ('email', 'password', 'nickname')

#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'type password..'}),
#             'nickname': forms.TextInput(attrs={'placeholder': 'type nickname..'}),
#             'name': forms.TextInput(attrs={'placeholder': 'type name..'}),
#             'surname': forms.TextInput(attrs={'placeholder': 'type surname..'}),
#         }

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)

#             for field in self.Meta.required:
#                 self.fields[field].required = True
    
#     def clean_password(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(CustomUserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data.get('password1'))
#         user.is_active = False # send confirmation email via signals
#         # obj = EmailActivation.objects.create(user=user)
#         # obj.send_activation_email()
#         if commit:
#             user.save()
#        return user

### not valid form
# class CustomUserUpdateForm(CustomUserCreationForm):
    
#     new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)

#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'new_password', 'password1', 'password2', 'first_name', 'last_name')
#         required = ('username', 'new_password', 'password1', 'password2')

#         labels = {
#             'username': 'Username',
#             'password1': 'Password1..',
#             'password2': 'Password2..',
#         }

#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'type username..'}),
#             'password1': forms.PasswordInput(attrs={'placeholder': 'type password..1'}),
#             'password2': forms.PasswordInput(attrs={'placeholder': 'repeat the password..'}),
#             'first_name': forms.TextInput(attrs={'placeholder': 'type name..'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'type surname..'}),
#         }

#     def __init__(self, new_password = new_password, *args, **kwargs):
#         super(CustomUserUpdateForm, self).__init__(*args, **kwargs)

#         for field in self.Meta.required:
#             self.fields[field].required = True
        
#         self.new_password = new_password


####################### *** forms.Form Inheritance *** #######################
CustomUser = get_user_model()

class CustomUserLoginForm(forms.Form):
    
    email_username = forms.CharField(
        label = 'Email/Username',
        widget = forms.TextInput(
            attrs = {
                'class': "form-control",
                "placeholder": "email or username",
                }
            )
        )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
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
        ## thisIsMyUsername == thisismyusername
        ## capitalization doesn't matter
        qs = CustomUser.objects.filter(username_iexact=email)
        if not qs.exists():
            raise forms.ValidationError('This is an invalid user')
        return email


## function-based view authenticate ### not valid
# class CustomUserLoginForm(forms.ModelForm):
    
#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'password')
#         required = ('username', 'password')

#         labels = {
#             'username': 'Email',
#             'password': 'Password',
#         }

#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'type password..'}), 
#         }

#     def __init__(self, *args, **kwargs):
#         super(CustomUserLoginForm, self).__init__(*args, **kwargs)

#         for field in self.Meta.required:
#             self.fields[field].required = True