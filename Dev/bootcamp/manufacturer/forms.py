from django import forms
from manufacturer.models import Manufacturer


class ManufacturerCreationForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        #ordering = ['id']

        fields = ('title', 'country', 'year')

        labels = {
            'Title': 'title',
            'Country': 'country',
            'Year': 'year'
        }
    
        required = ('title', 'country', 'year' )

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True