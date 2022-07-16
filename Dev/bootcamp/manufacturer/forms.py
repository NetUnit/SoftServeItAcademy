from .models import Manufacturer
from django import forms


# works with * templates
class ManufacturerCreationForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('title', 'country', 'year', 'image', 'media')
        labels = {
            'title': 'Title',
            'country': 'Country',
            'year': 'Year',
            'image': 'Image',
            'media': 'Media',
        }

        required = ('title', )

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title..'}),
            'country': forms.TextInput(attrs={'placeholder': 'country..'}),
            'year': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
