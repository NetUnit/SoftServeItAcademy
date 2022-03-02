from django.contrib.auth import authenticate, login
from accounts.models import CustomUser

import os
from rest_framework.exceptions import AuthenticationFailed

def register_social_user(provider, user_id, email, name):

    filtered_user_by_email = CustomUser.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email.first().auth_provider:

            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET')
            )

            return {
                'username': registered_user.username,
                'email':  registered_user.email,
                'tokens': registered_user.tokens()
                }
        else:
            raise AuthenticationFailed(
                detail='Please continue login using' + filtered_user_by_email.first().auth_provider
            )
    else:
        user = {
            'username': None,
            'email':  None,
            'tokens': None
        }

        user = User.objects.create(**user)
        # user.is_verified = True
        user.auth_provider = provider
        user.save(commit=False)

