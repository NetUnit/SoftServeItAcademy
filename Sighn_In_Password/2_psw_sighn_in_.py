import time


'''
    Due to security reasons it's not the best idea
    to keep a password here in the code.
    However this part brings only educational purpose
    and in order to demonstrate passwords inquiries,
    we will keep it here :)
'''


def inquiry(psw):
    if psw == '123':
        return True
    else:
        return False


def incorrect_answer():
    return print('INVALID PASSWORD. ACCESS DENIED')


def heads_up():
    return print('BE CAREFUL IT\'S THE LAST TRIAL')


def correct_answer():
    return print('CORRECT. ACCESS GRANTED')


def main_f():
    for trial in range(3):
        if inquiry(input('Type your password here: ')):
            return correct_answer()
        elif trial == 1:
            time.sleep(0.5)
            heads_up()
        else:
             incorrect_answer()
main_f()

    