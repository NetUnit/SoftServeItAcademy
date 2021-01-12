import time


'''
    Using loop for and range() sequence
    in the main block to check whether a
    password is strong and satisfy conditions
'''

# aforehand prepared answers in oreder to fill check() block
def inquiry():
    return input('PLEASE PROVIDE A PASSWORD: ')


def incorrect_answer():
    return print(('Password must contain as many as 6 characters \
    including lower-case, upper-case and numeric character').upper())


def heads_up():
    return print('BE CAREFUL IT\'S THE LAST TRIAL')


def correct_answer():
    return print('YOUR PASSWORD IS VALID')


# password check function
def condition_to_psw(psw):
    symbols = r'\n$@#'
    result = any([i.islower() for i in psw]) and any([i.isupper() for i in psw]) and \
             any([i.isdigit() for i in psw]) and any([i in psw for i in symbols])
    length = len(psw)

    if 16 > length > 6 and result:
        return True 
    else:
        return False


def psw_check_loop_for():
    for trial in range(3):
        if condition_to_psw(inquiry()): # == True
            return correct_answer()
        elif trial == 1:
            time.sleep(0.5)
            heads_up()
        else:
            incorrect_answer()

psw_check_loop_for()
