from rest_framework import serializers
from products.models import Product

class ProductPostSerializer(serializers.ModelSerializer):
    '''
        Serializer does 2 main things:
        :converts to JSON
        :validate data passed
    '''
    class Meta:
        model = Product
        fields = [
            'pk', 'title',
            'content', 'price',
            'user', 'manufacturers',
        ]

