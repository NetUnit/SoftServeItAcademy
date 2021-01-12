# codewars task10 - 'WeIrD StRiNg CaSe' - 6kyu KATA


'''
    Write a function toWeirdCase (weirdcase in Ruby)
    that accepts a string, and returns the same string
    with all even indexed characters in each word upper
    cased, and all odd indexed characters in each word
    lower cased. The indexing just explained is zero
    based, so the zero-ith index is even, therefore
    that character should be upper cased.

    The passed in string will only consist of alphabetical
    characters and spaces(' '). Spaces will only be present
    if there are multiple words. Words will be separated by
    a single space(' ').
'''

'''
# Var1 - RELEWANT WITH CODEWARS
# double iterating, filling the list + retrieving from nested list
def to_weird_case(string):
    list1 = string.split()  # 1st step create the list of str objects
    list1 = list(map(str.capitalize, list1))  # 2nd step capitalize all letters

    common_lst = list()
    for word in list1:
        lst = []
        index = 0
        for letter in word:
            if index % 2 == 0:
                lst.append(letter.upper())
            else:
                lst.append(letter.lower())
            index = index+1
        common_lst.append(lst)

    not_nested = [''.join(i) for i in common_lst]
    return ' '.join(not_nested)


string = input('Select the string U want to convert: ')
print(to_weird_case(string))


# Var2 - RELEWANT WITH CODEWARS
# Only math and string
def to_weird_case(string):
    index = 0
    WiErD = ''

    for x in string:
        if index % 2 == 0:
            WiErD += x.upper()
        else:
            WiErD += x.lower()

        index = index+1
        if x == ' ':
            index = 0
        else:
            continue

    return WiErD


string = input('Type the string here: ')
print(to_weird_case(string))
'''

# Var3 - RELEWANT WITH CODEWARS
# Enumerate into dicts
def to_weird_case(string):
    lst1 = (string.title()).split()
    lst = []

    for word in lst1:
        for key, value in enumerate(word):
            return list(enumerate(word))

            if key % 2 == 0:
                letter_by_key = word[key]
                lst.append(letter_by_key.upper())
            else:
                letter_by_key = word[key]
                lst.append(letter_by_key.lower())
                # lst.append(value.lower())

        maxi = max(0, key+1)
        word_length = len(tuple(word))

        if maxi != word_length:
            pass
        else:
            lst.append(' ')

    return ''.join(lst).rstrip()


string = input('Select the string U want to convert: ')
print(to_weird_case(string))

'''
# Var4 - RELEWANT WITH CODEWARS
# Enumerate into dicts + short hand syntax
def to_weird_case(string):
    lst1 = (string.title()).split()
    lst = []

    for word in lst1:
        for key, value in enumerate(word):
            lst.append(word[key].upper()) if key % 2 == 0 else lst.append(
                word[key].lower())
        lst.append(' ') if max(0, key+1) == len(tuple(word)) else lst

    return ''.join(lst).rstrip()


string = input('Select the string U want to convert: ')
print(to_weird_case(string))
'''