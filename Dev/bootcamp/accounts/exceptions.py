
class CustomAuthFailed(Exception):
    message = ('Authentication Failed, reasons: ' +
        'Incorrect password or username' +
        'Password may be case-sensitive' +
        'Chack if the \'Caps Lock\' key wasn\'t accidentally hit')

    def __init__(self, message=message):
        message = self.message
    
    def __str__(self):
        return(repr(self.message))