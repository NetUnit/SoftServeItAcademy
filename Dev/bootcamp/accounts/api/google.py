import google
from google.oauth2 import id_token
from google.auth.transport import requests


class Google:
    ''' 
        Google class to fetch the user info and return it 
    '''

    @staticmethod
    def validate(auth_token):
        
        # print(auth_token)
        print(requests.Request())

        '''
            Querying the Google oauth2 api to fetch the user info
            :returns: google info
        '''
        # print(auth_token) ### +++
        try:
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request()
            )

            # print(f'This is id_info: {idinfo}')
            request = requests.Request()

            ## This is request in API View
            ## print(request.__dict__.get('session').__dict__) + print('This is request from google')
            
            if 'accounts.google.com' in idinfo['iss']:
                return idinfo
            
        except Exception as err:
            print(err)
            return 'Token is either invalid or expired: class ---> Google'
    
    # @staticmethod
    # def authenticate(auth_token):