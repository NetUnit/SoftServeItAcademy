import re
import string


# codewars task7 - Valid HK Phone Number - 7kyu KATA


'''
    In Hong Kong, a valid phone number has the 
    format xxxx xxxx where x is a decimal digit (0-9).
    For example:

    Define two functions, isValidHKPhoneNumber and has 
    Valid HK Phone Number, that returns whether a given
    string is a valid HK phone number and 
    contains a valid HK phone number respectively
    (i.e. true/false values).

    all([i.isdigit() for i in condition]) - list comprehension
    that will work like a sorting loop

    Option #2.1 Using re.serach:
        will return <span object> which equals True
        faster way

    Option #2.2 Using re.findall:
        will return the list, we need to check the list 
        in addition
'''


# RELEWANT WITH CODEWARS
# Option #1.1
def is_valid_HK_phone_number(number):
    condition = (number.strip('"')).split(' ')

    if len(condition[0]) == 4 and \
            len(condition[1]) == 4 and \
            all([i.isdigit() for i in condition]):
        return True
    else:
        return False


number = input('Type the text U r going to check: ')
print(is_valid_HK_phone_number(number))


# Option #2.1
def has_valid_HK_phone_number(number):
    # building own pattern with re.compile()
    pattern = re.compile(r'\d{4}\s\d{4}')
    result = pattern.search(number)
    return True if result else 0

    # in order to get a final-sliced number
    #final_number = ' '.join(pattern.findall(number))
    # return final_number


number = input('Type the text U r going to check: ')
print(has_valid_HK_phone_number(number))


# Option #2.2 Using findall

'''
    
    print(condition) - will return the list of digits
    as the pattern may be digits only, the last thing
    is just to check if the list == True

    [] - False
    ['2359 1478'] - True
'''


def has_valid_HK_phone_number(number):
    # your code here
    lst = (number.strip('"')).split(' ')
    return True if re.findall(r"\d{4}\s\d{4}", number) else 0


number = input('Type the text U r going to check: ')
print(has_valid_HK_phone_number(number))
