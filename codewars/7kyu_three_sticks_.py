# codewars task8 - 'Three sticks'- 7kyu KATA


'''
    Imagine that you are given two sticks. You want to end up
    with three sticks of equal length. You are allowed to cut
    either or both of the sticks to accomplish this, and can
    throw away leftover pieces.

    Write a function, maxlen, that takes the lengths of the two
    sticks (L1 and L2, both positive values), that will return
    the maximum length you can make the three sticks.
'''


# RELEWANT WITH CODEWARS
def maxlen(L1, L2):
    if 0.5 * max(L1, L2) < min(L1, L2):
        return round(0.5 * max(L1, L2), 2)
    elif 1/3 * max(L1, L2) > min(L1, L2):
        return round(max(L1, L2)/3, 2)
    else:
        return min(L1, L2)


print(maxlen(73, 55))


# NON - RELEWANT WITH CODEWARS
# Natural Units, round added
def maxlen(nums):
    if 0.5 * max(nums) < min(nums):
        return round(0.5 * max(nums), 2)
    elif 1/3 * max(nums) > min(nums):
        return round(max(nums)/3, 2)
    else:
        return round(float(min(nums)), 2)


nums = tuple(map(int, input('Enter two numbers, through space: ').split()))
print(maxlen(nums))
