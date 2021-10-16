from django.views import generic
from .models import CustomUser
from django import forms

################################################################################################
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'nickname', 'first_name', 'last_name')
        required = ('email', 'password1', 'password2', 'nickname')

        # hidden password input
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'type password..1'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'repeat the password..'}),
            'nickname': forms.TextInput(attrs={'placeholder': 'type nickname..'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'type name..'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'type surname..'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    # def clean_password(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
        
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(CustomUserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     user.is_active = False # send confirmation email via signals
    #     # obj = EmailActivation.objects.create(user=user)
    #     # obj.send_activation_email()
    #     if commit:
    #         user.save()
    #     return user

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

## class-based view authenticate
class LoginForm(AuthenticationForm):
    #username = forms.CharField(label='Email / Username')
    email = forms.EmailInput(attrs={'placeholder': 'type email..'})
    

class CustomUserUpdateForm:
    pass
 
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

CustomUser = get_user_model()

class CustomUserLoginForm(forms.Form):
    
    
    email_username = forms.CharField(
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

    
    
    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')

    def clean_username(self):
        email = self.cleaned_data.get('email')
        ## thisIsMyUsername == thisismyusername
        ## capitalization doesn't matter
        qs = CustomUser.objects.filter(username_iexact=email)
        if not qs.exists():
            raise forms.ValidationError('This is an invalid user')
        return email


    