import twitter
import os


class Twitter:
    '''
    Class to decode tokens (access_token & access_token_secret)
    tokens combine the user access_token access_token_secret
    separated with space

    .. note::
        *** While the Consumer Keys (API keys) give the API context 
        about the developer App that is sending a request, 
        *** the Access Tokens provide context about the Twitter 
        user on behalf of whom the App is sending the request
    '''
    @staticmethod
    def validate_twitter_auth_tokens(access_token_key, access_token_secret):
        '''
        validation of tokens gets twitter user profile info from Twitter API
        :returns: twiiter info, dict
        '''

        # API keys
        consumer_api_key = os.environ.get('TWITTER_API_KEY')
        consumer_api_secret_key = os.environ.get('TWITTER_CONSUMER_SECRET')

        api = twitter.Api(
            consumer_key=consumer_api_key,
            consumer_secret=consumer_api_secret_key,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret
        )

        user_profile_info = api.VerifyCredentials(include_email=True)
        return user_profile_info.__dict__
