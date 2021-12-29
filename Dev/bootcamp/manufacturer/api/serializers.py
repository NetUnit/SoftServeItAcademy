
from rest_framework import serializers
from manufacturer.models import Manufacturer

class ManufacturerPostSerializer(serializers.ModelSerializer):
    '''
        Serializer does 2 main things:
        :converts to JSON
        :validate data passed
    '''
    class Meta:
        model = Manufacturer
        fields = [
            'pk', 'title',
            'country', 'year',
            'image', 'media'
        ]

        read_only_fields = [
            'pk', 'user'
        ]