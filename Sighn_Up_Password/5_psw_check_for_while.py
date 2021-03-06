import string
import re


def validation(psw):
    for i in psw:
        if not any(i in psw for i in string.ascii_lowercase):
            return 'Did not pass a verification stage'

        if not any(i in psw for i in string.ascii_uppercase):
            return 'Did not pass a verification stage'

        if not any(i in psw for i in string.digits):
            return 'Did not pass a verification stage'
        
        if not any(i in psw for i in r'\n#$@%'):
            return 'Did not pass a verification stage'

        if not 6<len(list(psw))<16:
            return 'Did not pass a verification stage'
        else:
            return True


def check_psw_while():
    counter = 3
    while counter > 0:
        counter -= 1

        if validation(input('Please enter the password: ')) == True:
            return 'YOUR PASSWORD IS VALID'
        
        elif counter == 1:
            print('BE CAREFUL IT\'S THE LAST TRIAL')

        else:
            print(('Password must contain as many as 6 characters \
including lower-case, upper-case and numeric characters').upper())

check_psw_while()

