from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
# from . models import CustomUser
from django.contrib.auth.backends import BaseBackend

## fixes the lowercase mistakes
class CaseInsensitiveModelBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        
        try:
            case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_username_field: username})
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user


# # class EmailBackend(ModelBackend):

# #     def authenticate(self, email, password=None, **kwargs):
# #         try:
# #             user = User.objects.get(email=email)
# #         except User.DoesNotExist:
# #             return None
        
# #         except User.MultipleObjectsReturned:
# #             user = User.objects.filter(email=email).order_by('id').first()

# #         if getattr(user, 'is_active') and user.check_password(password):
# #           return None
    
# #     def get_user(self, user_id):
# #         try:
# #             return User.objects.get(pk=user_id)
        
# #         except User.DoesNotExist:
# #             return None


