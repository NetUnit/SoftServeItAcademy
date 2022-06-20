import google
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.serializers import ValidationError


class Google:
    '''
    Google class to fetch user info and return it
    '''

    @staticmethod
    def validate(auth_token):
        '''
        Querying the Google oauth2 api to fetch the user info
        :returns: google info
        '''

        try:
            id_info = id_token.verify_oauth2_token(
                auth_token, requests.Request()
            )
            # the whole google user data from Google API
            # print(f"This is id_info: {id_info}")
            if 'accounts.google.com' in id_info['iss']:
                return id_info
            return 'Something bad with provider (￣□￣」)'
        except Exception:
            g_identifier = ValidationError(
                {'detail': 'Token is either invalid or expired (；⌣̀_⌣́)'}
            )
