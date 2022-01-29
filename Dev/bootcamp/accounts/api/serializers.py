
from rest_framework import serializers
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.fields import (
    CharField, 
    EmailField
    )

from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    SerializerMethodField, 
    ValidationError
    )
from rest_framework.relations import HyperlinkedIdentityField

from accounts.models import (
    CustomUser,
    Token
    )

class CustomUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password',

        ]

    def create(self, validated_data):
        '''
            Password hashing is implemented with model behavior.
            Just use the data dict as a variable
            :returns: new user object created & via POST method
        '''
        model = CustomUser()
        user = model.create_user(data=validated_data)
        if not user:
            raise ValidationError(
                {'detail': 'User hasn\'t been created ヽ(冫、)ﾉ',}
            )
        user.save()
        # print(user.__dict__)
        return user

    def validate(self, data):
        email = data.get('email')
        qs = CustomUser.objects.filter(email=email)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError(
                {'detail': 'Email already exists ┐(‘～` )┌', }
            )
        print(data)
        return data
        
class CustomUserLoginSerializer(serializers.ModelSerializer):
    username = CharField(required=False, allow_blank=True,
                        allow_null=True, max_length=42
                    )
    email = EmailField(label='Email Address', required=False, allow_blank=True)
    token = CharField(allow_blank=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]

        extra_kwargs = {'password':
                {'write_only': True}
            }
    
    def validate(self, data):
        # print(data)
        '''
            we can also assighn other than rest_framework.authtoken
            here.
            :returns: validated data that comes from a client when auth process
            :raise Vlidation Error: no user obj in the db or wrong auth data
        '''
        email = data.get('email')
        username = data.get('username')
        if not email and not username:
            raise serializers.ValidationError(
                {'detail': 'Email/Username are required ┐(°,ʖ°)┌', }
            )
        
        data = dict(data)
        user_exists = CustomUser.user_exists(data)
            
        if not user_exists:
            raise serializers.ValidationError(
                {'detail': 'Email/Username are not valid ʅ(°_°)ʃ', }
            )

        user = CustomUser.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        
        user = user.exclude(email__isnull=True)
        #print(user)
        user = user.first()
        #print(user)
        #print(data.get('password'))
        if not user:
            raise serializers.ValidationError(
                {'detail': 'User wasn\'tfound (° -°）', }
            )
        correct_psw = user.check_password(data.get('password'))
        if not correct_psw:
            raise serializers.ValidationError(
                {'detail': 'Hmm ... passsword wasn\'t correct (° -°）', }
            )
        token = Token.objects.filter(user=user).get()
        data['token'] = token.key
        return data

# ['Meta', '__class__', '__class_getitem__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_args', '_context', '_creation_counter', '_declared_fields', '_get_model_fields', '_kwargs', '_read_only_defaults', '_readable_fields', '_writable_fields', 'allow_null', 'bind', 'build_field', 'build_nested_field', 'build_property_field', 'build_relational_field', 'build_standard_field', 'build_unknown_field', 'build_url_field', 'context', 'create', 'data', 'default', 'default_empty_html', 'default_error_messages', 'default_validators', 'error_messages', 'errors', 'fail', 'field_name', 'fields', 'get_attribute', 'get_default', 'get_default_field_names', 'get_extra_kwargs', 'get_field_names', 'get_fields', 'get_initial', 'get_unique_for_date_validators', 'get_unique_together_validators', 'get_uniqueness_extra_kwargs', 'get_validators', 'get_value', 'help_text', 'include_extra_kwargs', 'initial', 'instance', 'is_valid', 'label', 'many_init', 'parent', 'partial', 'read_only', 'required', 'root', 'run_validation', 'run_validators', 'save', 'serializer_choice_field', 'serializer_field_mapping', 'serializer_related_field', 'serializer_related_to_field', 'serializer_url_field', 'source', 'style', 'to_internal_value', 'to_representation', 'update', 'url_field_name', 'validate', 'validate_empty_values', 'validated_data', 'validators', 'write_only']