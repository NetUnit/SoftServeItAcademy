from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import authentication
from accounts.models import CustomUser, Token
import datetime
from rest_framework.exceptions import AuthenticationFailed


UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None,
                     email=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            )
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            ).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user


class TokenAuthBackend(authentication.BaseAuthentication):

    def authenticate(self, request, token=None, **kwargs):
        try:
            print(token)
            if token is None:
                return None

            token_qs = Token.objects.filter(key=token)
            token_qs = token_qs.exclude(user__isnull=True)
            token = token_qs.first()
            print(token)
            if token is None:
                raise AuthenticationFailed('token is invalid')
            # check token's expiry date
            if not self.validate_token(token):
                self.refresh_key(token)
                raise AuthenticationFailed('token has expired')
            user = token.user
            return user

        except UserModel.DoesNotExist:
            return None

    def validate_token(self, token):
        dt = token.created
        dt = dt.replace(tzinfo=None)
        timedelta = datetime.datetime.today() - dt
        days = timedelta.days
        return True if days < 30 else False

    def refresh_key(self, token):
        refreshed_key = Token.generate_key()
        Token.objects.filter(pk=token.pk).update(
            key=refreshed_key,
            created=datetime.datetime.now()
        )
        return token
