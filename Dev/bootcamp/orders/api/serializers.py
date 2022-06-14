from rest_framework import serializers
from orders.models import Order


class OrderPostSerializer(serializers.ModelSerializer):
    '''
        Serializer does 2 main things:
        :converts to JSON
        :validate data passed
    '''
    class Meta:
        model = Order
        fields = [
            'product',
            'created_at',
            'user',
        ]

        read_only_fields = [
            'pk', 'user'
        ]
