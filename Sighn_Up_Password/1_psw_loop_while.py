import time


def inquiry():
    return input('PROVIDE A KEY, PLEASE: ')


def incorrect_answer():
    return print(('Password must contain as many as 6 characters including lower-case, upper-case and numeric characters').upper())


def heads_up():
    return print('BE CAREFUL IT\'S THE LAST TRIAL')


def correct_answer():
    return print('YOUR PASSWORD IS VALID')


# password check function
def condition_to_psw(psw):
    symbols = r'\n$@#'
    result = any([i.islower() for i in psw]) and any([i.isupper() for i in psw]) and any(
        [i.isdigit() for i in psw]) and any([i in psw for i in symbols])
    length = len(psw)

    if 16 > length > 6 and result:
        return True 
    else:
        return False


'''
    loop will close when counter reaches 0,
        if  strict inequality '>'

    will continue, if not strict inequality '>='
        so the algorithm while wil implement <body> one more time

    the counter should be placed before <body> 

     in the <body> in loop - we r not using break()
     due to a keyword break, return() will close the loop
'''


def check_psw_loop_while():
    counter = 3
    while counter > 0:
        counter -= 1 

        if condition_to_psw(inquiry()):
            return correct_answer()

        elif counter == 1:
            heads_up()

        else:
            incorrect_answer()

check_psw_loop_while()
