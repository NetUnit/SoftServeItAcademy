import facebook


class Facebook:
    '''
    Facebook class to fetch the user info and return it
    '''
    @staticmethod
    def validate(auth_token):
        '''
        Validate method Queries the facebook graph API to fetch the user info
        :returns: google info
        '''
        # print(auth_token) # +++
        try:
            graph = facebook.GraphAPI(access_token=auth_token)
            profile = graph.request('/me?fields=name,email')
            return profile
        except Exception as err:
            print(err)
            return 'Token is either invalid or expired: class ---> Facebook'
