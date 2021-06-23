from .models import Product, Manufacturer
from django import forms


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
            'price': 'Price',
        }

        required = ('title', 'content', 'price')

        widgets = {

            'price': forms.NumberInput(),

        }

    manufacturers = CustomMMCF(
        label='Manufacturers',
        queryset=Manufacturer.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True


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

