# codewars task5 - 'Create Phone Number!'- 7kyu KATA


'''
    Your task is to make function, which returns the sum of a sequence 
    of integers.
    The sequence is defined by 3 non-negative values: begin, end, step.
    If begin value is greater than the end, function should returns 0

    Suggested sequences:
        (2, 6, 2) - sum(12)
        (1, 5, 1) - sum(15)
        (1, 5, 3) - sum(5)
        (0, 15, 3) - sum(45)
        (16, 15, 3) - sum(0)
        (2, 24, 22), 26) - sum(26)

'''


# RELEVANT WITH CODEWARS
def sequence_sum(a, b, d):
    if a <= b:
        return sum(range(a, b+1, d))
    else:
        return 0


# RELEVANT WITH CODEWARS
def loop_sum(a, b, d):
    my_list = list()
    for i in range(a, b+1, d):
        my_list.append(i)

    return sum(my_list) if a <= b else 0


# RELEVANT WITH CODEWARS
def lambda_sum(a, b, d):

    return sum(list(map(int, range(a, b+1, d))))


# RELEVANT WITH CODEWARS
def lambda_sum(a, b, d):
    for i in range(a, b, d):
        lst = []
        lst.append(i)
    return lst


# RELEVANT WITH CODEWARS
def arithmetic_sum(a, b, d):
    '''
       if a while condition isn't stisfied sum will be 0
       as sum assighned as 0
       function wil return 0 automatically, 
       no requirements to additional conditions
    '''

    n = 1
    sequence = 0
    sum = 0

    while (n-1) <= ((b-a)/d):
        sequence = a + d*(n-1)
        n = n + 1
        sum = sum + sequence
    return sum


# RELEVANT WITH CODEWARS
def arithmetic_sum_for(a, b, d):
    '''
        due to the fact that 0 is included into a range
        we will not minus (n-1) when multiplying to 'd'
    '''
    sum = 0
    n = (b-a)//d
    for n in range(n+1):  # range will be (0, 1, 2)
        sum += a + d*(n)
    return sum


print(arithmetic_sum_for(2, 6, 2))
