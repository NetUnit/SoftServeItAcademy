from django import forms


class ProcessContactForm(forms.Form):

    first_name = forms.CharField(
        label='Firstname',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "placeholder": "type your name/nickname",
            }
        )
    )

    last_name = forms.CharField(
        label='LastName',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "placeholder": "your surname",
            }
        )
    )

    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "placeholder": "type email",
            }
        )
    )

    cell = forms.CharField(
        label='Tel',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "placeholder": "tel. number",
            }
        )
    )

    feedback = forms.CharField(
        label='Feedback',
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                "placeholder": "no less than 80 characters",
            }
        )
    )

    # url = forms.URLField()

    def clean(self):
        email = self.cleaned_data.get('email')
        feedback = self.cleaned_data.get('feedback')


# search form to drag a keyword matched to the DB
class ItemSearchForm(forms.Form):
    
    searched = forms.CharField(max_length=220)

    widgets = {
        'searched': forms.TextInput(attrs={'placeholder': 'Search Items...'}),
    }

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
