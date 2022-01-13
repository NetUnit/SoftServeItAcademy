
from rest_framework import serializers
from manufacturer.models import Manufacturer
from bootcamp.api.serializers import CustomImageField
from bootcamp.api.exceptions import (
    CustomCharField,
    TitleDuplicationError,
    TitleAbsenceError
    )

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


class ManufacturerCreateSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(
        required=False, max_length=None, 
        allow_empty_file=True, use_url=True
        )

    class Meta:
        model = Manufacturer
        fields = [
            'pk', 'title',
            'country', 'year',
            'image'
        ]

        # disclude fields which are not required
        read_only_fields = [
            'pk',
            ]

    def to_internal_value(self, data):
        return data

    def validate(self, data):
        self._kwargs["partial"] = True
        title = data.get('title')
        if not title:
            raise TitleAbsenceError()
        qs = Manufacturer.objects.filter(title__iexact=title)
        # exclude object itself in order to post/put self instance data
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise TitleDuplicationError()
        return super().validate(data)

# "media/manufacturers/c69d6a2f-27f.png"