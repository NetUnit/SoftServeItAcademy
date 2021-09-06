from .models import CustomUser
from django import forms



class CustomUserCreationForm(forms.ModelForm):
    class Meta:

        model = CustomUser
        fields = ('email', 'password', 'nickname', 'name', 'surname')
        labels = { 'email': 'Email',
                    'password': 'password',
                    'nickname': 'nickname',
                    'name': 'name',
                    'surname': 'surname'
                }

        required = ('email', 'password', 'nickname', 'name', 'surname')

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
            'password': forms.TextInput(attrs={'placeholder': 'type password..'}),
            'nickname': forms.TextInput(attrs={'placeholder': 'type nickname..'}),
            'name': forms.TextInput(attrs={'placeholder': 'type name..'}),
            'surname': forms.TextInput(attrs={'placeholder': 'type surname..'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for field in self.Meta.required:
                self.fields[field].required = True


# class RegisterForm(forms.ModelForm):

#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:

#         model = CustomUser
#         fields = ('email', 'password1', 'password2')
#         labels = { 'email': 'Email',
#                     'password1': 'Password',
#                     'password2': 'Confirm Password'
#                 }

#         required = ('email', 'password1', 'password2')

#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
#             'password1': forms.TextInput(attrs={'placeholder': 'type password..'}),
#             'password2': forms.TextInput(attrs={'placeholder': 'type password again'})
#         }

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)

#             for field in self.Meta.required:
#                 self.fields[field].required = True

#     # def clean_password(self):
#     #     # Check that the two password entries match
#     #     password1 = self.cleaned_data.get("password1")
#     #     password2 = self.cleaned_data.get("password2")
#     #     if password1 and password2 and password1 != password2:
#     #         raise forms.ValidationError("Passwords don't match")
#     #     return password2
    
#     # def save(self, commit=True):
#     #     # Save the provided password in hashed format
#     #     user = super(RegisterForm, self).save(commit=False)
#     #     user.set_password(self.cleaned_data.get('password1'))
#     #     user.is_active = False # send confirmation email via signals
#     #     # obj = EmailActivation.objects.create(user=user)
#     #     # obj.send_activation_email()
#     #     if commit:
#     #         user.save()
#     #     return user