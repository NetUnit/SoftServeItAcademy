# codewars task4 - 'Create Phone Number!'- 6kyu KATA


'''
    Write a function that accepts an array of 10 integers (between 0 and 9),
    that returns a string of those numbers in the form of a phone number.:

    ex. create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) to "(123) 456-7890"

    no inverted commas in a ex.2
'''


# NON-RELEVANT WITH CODEWARS
def create_phone_number(digits):
    digits = list(map(str, digits))
    digits.insert(0, '"')
    digits.insert(1, '(')
    digits.insert(5, ')')
    digits.insert(6, ' ')
    digits.insert(10, '-')
    digits.append('"')
    return ''.join(digits)


print(create_phone_number(list(range(10))))


# RELEVANT WITH CODEWARS - it's just enough to convert the type of 'n' to 'str'
def create_phone_number(digits):
    digits = list(map(str, digits))
    digits.insert(0, '(')
    digits.insert(4, ')')
    digits.insert(5, ' ')
    digits.insert(9, '-')
    return ''.join(digits)


print(create_phone_number(list(range(10))))
