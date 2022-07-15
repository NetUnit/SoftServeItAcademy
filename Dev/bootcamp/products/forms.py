from .models import Product, Manufacturer
from django import forms
from django.utils.translation import gettext as _
from django.forms import ValidationError


# this class created only for menu product creation purpose
class CustomMMCF(forms.ModelMultipleChoiceField):
    '''
    takes single queryset parameter - manufacturer objects qs
    creates the choices for the field selected from list of obj
    '''
    def label_from_instance(self, manufacturer):
        return f'"{manufacturer.title}" ({manufacturer.country})'


# model instance form for product obj
class ProductCreationForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'content', 'price', 'image', 'media')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'price': 'Price, $:',
            'image': 'Image',
            'media': 'Media',
        }

        required = ('title', 'content', 'price')

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'title..'}
            ),
            'content': forms.Textarea(
                attrs={'placeholder': 'type some content here..'}
            ),
            'price': forms.NumberInput(
                attrs={'min': 1, 'max': 1000000, 'type': 'number',
                       'placeholder': 'price..'}
            ),
        }

    manufacturers = CustomMMCF(
        label='Manufacturers',
        queryset=Manufacturer.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    def check_manufacturers(self):
        '''
        custom validation when no manufacturer exist
        :returns: True if manufacturer qs isn't empty,
        ValidationError when vice versa
        '''

        if not len(self.fields['manufacturers'].queryset) > 0:
            raise ValidationError(
                _('Ask admin to provide Manufacturers'),
                code='invalid'
            )
        return True

    def check_title(self):
        '''
        minimium title length validation
        :returns: True if product's title is enough long,
        ValidationError when vice versa
        '''

        min_title_length = len(str(self.cleaned_data.get('title'))) > 1
        if not min_title_length:
            get_title = self.cleaned_data.get('title')
            raise ValidationError(
                _(f'\"{get_title}\" isn\'t enough long'),
                code='invalid'
            )
        return True
