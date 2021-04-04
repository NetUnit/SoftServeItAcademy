import string

# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)

### згенерувати пароль модулем рендом
def pass_cheker(password):
    
    demand1 = any([i in string.ascii_lowercase for i in password])  # bool1
    demand2 = any([i in string.ascii_uppercase for i in password])  # bool2
    demand3 = any([i in string.digits for i in password])           # bool3
    demand4 = any([i in string.punctuation for i in password])      # bool4
    demand5 = [i in password for i in password].count(True) > 7     # bool5
    result = (demand1, demand2, demand3, demand4, demand5)
    return "Invalid password" if result.count(True) != 5 else 'Password is OK'


psw1 = 'ds7#45A3'
psw2 = 'sdsd'

if __name__ == '__main__':
    print(pass_cheker(psw1))
    print(pass_cheker(psw2))


