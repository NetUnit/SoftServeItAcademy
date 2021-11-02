from .models import Product, Manufacturer
from django import forms
from django.utils.translation import gettext as _
from django.forms import ValidationError

# this class created only for menu product creation purpose
class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, manufacturer):
        return f'"{manufacturer.title}" ({manufacturer.country})'


# class ProductCreationForm(forms.Form):

#     title = forms.CharField(max_length=220)
#     content = forms.CharField(max_length=1000)
#     price = forms.IntegerField()


# works with * templates
# class ProductCreationForm(forms.ModelForm):
    
#     class Meta:
#         model = Product
#         fields = ('title', 'content', 'price')
#         labels = {
#             'title': 'Title',
#             'content': 'Content',
#             'price': 'Price'
#         }

#         required = ('title',)

#         widgets = {

#             'price': forms.NumberInput()
#         }

#     def __init__(self, *args, **kwargs):
#         super(ProductCreationForm, self).__init__(*args, **kwargs)

#         for field in self.Meta.required:
#             self.fields[field].required = True


## works with * templates
class ProductCreationForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'content', 'price')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'price': 'Price, $:',
        }

        required = ('title', 'content', 'price')

        widgets = {

            'title': forms.TextInput(attrs={'placeholder': 'title..'}),
            'content': forms.Textarea(attrs={'placeholder': 'type some content here..'}),
            'price': forms.NumberInput(attrs={'min':1,'max': 1000000,'type': 'number', 'placeholder': 'price..'})
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
            raise ValidationError(_('Ask admin to provide Manufacturers'), code='invalid')
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
            raise ValidationError(_(f'\"{get_title}\" isn\'t enough long'), code='invalid')
        return True

## works with * templates
# class ProductCraetionForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('title', 'content', 'price')
        

#     def title_length(self):

#         title_length = self.cleaned_data.get('title')
#         min_title_length = len(title_length) > 1

#         if not min_title_length:
#             raise forms.ValidationError('This is not long enough, at least 2')
#         return title_length


## search form to drag a keyword matched to the DB
class ItemSearchForm(forms.Form):
    
    searched = forms.CharField(max_length=220)

    widgets = {

        'searched': forms.TextInput(attrs={'placeholder': 'Search Items...'}),
    }

    def __init__(self, *args, **kwargs):
        super(ItemSearchForm, self).__init__(*args, **kwargs)
