import time





def inquiry():
    return input('Type your password here: ')


def incorrect_answer():
    return print('INVALID PASSWORD. ACCESS DENIED')


def heads_up():
    return print('BE CAREFUL IT\'S THE LAST TRIAL')


def correct_answer():
    return print('Correct. ACCESS GRANTED')


def main_f():
    for trial in range(3):
        if inquiry() == '123':
            return correct_answer()
        elif trial == 1:
            time.sleep(0.5)
            heads_up()
        else:
             incorrect_answer()
main_f()

