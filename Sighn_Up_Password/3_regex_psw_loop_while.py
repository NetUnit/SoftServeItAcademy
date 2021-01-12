import re
import string
import time


def incorrect_answer():
    return print(('Password must contain as many as 6 characters \
    including lower-case, upper-case and numeric characters').upper())


def inquiry():
    return input('PLEASE PROVIDE A PASSWORD: ')


def heads_up():
    return print('BE CAREFUL IT\'S THE LAST TRIAL')


def correct_answer():
    return print('YOUR PASSWORD IS VALID')


'''
    in this password-check we're gonna
    match if the password fits through:

        regex - re.findall - returns boolean 
        if a at least one symbol is in the typed data
        then expression - will return True

        for instance: QWERTy - will satisfy condition of ascii.lower()
        lowercase letters

        then we use BOOL condition to satisfy the main one
        described in a function psw_requirements()
'''

def main(psw):

    '''
        seconadary functions will inherit
        a parameter 'psw' from main
    '''

    def lowercase_letters(main):
        result = re.findall("[a-z]", main)
        return True if result else False

    def uppercase_letters(main):
        result = re.findall("[A-Z]", main)
        return True if result else False

    def numeric_characters(main):
        result = re.findall('[$#@]', main)
        return True if result else False

    def digits(main):
        result = re.findall('[0-9]', main)
        return True if result else False

    def length(main):
        result = len(main)
        return True if 16>result>6 else False

    def summary(main):
        main_result = lowercase_letters(psw) * uppercase_letters(psw) \
        * numeric_characters(psw) * digits(psw) * length(psw)
        return main_result

    return summary(main)


def psw_check_loop_while():
    trial = 3
    while trial > 0:
        trial -= 1

        if main(inquiry()): # == True
            correct_answer()
            break
        elif trial == 1:
            heads_up()
        else:
            incorrect_answer()

psw_check_loop_while()















