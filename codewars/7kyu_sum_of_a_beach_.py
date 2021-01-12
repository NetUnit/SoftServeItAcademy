import re


# codewars task6 - "Sum of a Beach" - 7kyu KATA
'''
    Beaches are filled with sand, water, fish, and sun.
    Given a string, calculate how many times the words "Sand",
    "Water", "Fish", and "Sun" appear without overlapping
    (regardless of the case).

    arithmetic_sequence_sum(2, 3, 5) should return 40:

    ex. of string: WAtErSlIde, GolDeNSanDyWateRyBeaChSuNN,
    gOfIshsunesunFiSh, cItYTowNcARShoW
'''

# RELEWANT WITH CODEWARS


def sum_of_a_beach(beach):

    result = []
    result.extend(re.findall(r'sand', beach.lower()))
    result.extend(re.findall(r'water', beach.lower()))
    result.extend(re.findall(r'fish', beach.lower()))
    result.extend(re.findall(r'sun', beach.lower()))
    return len(result)


# beach = input('Type the text U r going to check: ')
# print(sum_of_a_beach(beach))


# RELEWANT WITH CODEWARS
def sum_of_a_beach(beach):

    result = list()
    pattern1 = re.compile('sand')
    pattern2 = re.compile('water')
    pattern3 = re.compile('fish')
    pattern4 = re.compile('sun')

    result =                          \
    pattern1.findall(beach.lower()) + \
    pattern2.findall(beach.lower()) + \
    pattern3.findall(beach.lower()) + \
    pattern4.findall(beach.lower())

    return len(result)


# beach = input('Type the text U r going to check: ')
# print(sum_of_a_beach(beach))


# RELEWANT WITH CODEWARS
def sum_of_a_beach(beach):

    result = []
    lst = (
     'sun', 
     'fish', 
     'water', 
     'sand'
    )
    for i in lst:
        result += re.findall(i, beach.lower())
        # result.extend(re.findall(i, beach.lower()))
    return len(result)
        

# beach = input('Type the text U r going to check: ')
# print(sum_of_a_beach(beach))


# RELEWANT WITH CODEWARS
'''
    here  we have an example how to iterate a nested list
    and convert it to a common list
'''
def sum_of_a_beach(beach):
    
    result = [(re.findall(i, beach.lower())) for i in ('sun', 'fish', 'water', 'sand') if (re.findall(i, beach.lower())) != [] ]
    # result will a nested list
    sum = []
    for x in result:
        sum += x
    return len(sum)
        

beach = input('Type the text U r going to check: ')
print(sum_of_a_beach(beach))






