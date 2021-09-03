from .models import CustomUser
from django import forms

class CustomUserCreationForm(forms.ModelForm):
    class Meta:

        model = CustomUser
        fields = ('email', 'password')
        labels = { 'email': 'Email',
                    'password': 'password'
                }

        required = ('email', 'password')

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'type email..'}),
            'password': forms.TextInput(attrs={'placeholder': 'type password..'})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for field in self.Meta.required:
                self.fields[field].required = True