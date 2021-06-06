from products.models import Product
from django import forms


# class ProductCreationForm(forms.Form):

#     title = forms.CharField(max_length=220)
#     content = forms.CharField(max_length=1000)
#     price = forms.IntegerField()

class ProductCreationForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('title', 'content', 'price')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'price': 'Price'
        }

        required = ('title', )

        widgets = {

            'price': forms.NumberInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProductCreationForm, self).__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
