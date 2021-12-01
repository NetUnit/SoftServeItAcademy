
from rest_framework import serializers
from manufacturer.models import Manufacturer
from bootcamp.api.serializers import CustomImageField

class ManufacturerPostSerializer(serializers.ModelSerializer):
    '''
        Serializer does 2 main things:
        :converts to JSON
        :validate data passed
    '''

    image = CustomImageField(
        max_length=None, use_url=True,
        )
    
    class Meta:
        model = Manufacturer
        fields = [
            'pk', 'title',
            'country', 'year',
            'image'
        ]

        read_only_fields = [
            'pk', 'user'
        ]

    def validate_title(self, value):
        qs = Manufacturer.objects.filter(title__iexact=value)        
        if self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError({
                'title': 'This title already exists ┐(‘～` )┌',
            })
        return value