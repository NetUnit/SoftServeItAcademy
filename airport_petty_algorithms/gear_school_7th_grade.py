'''
    There are 4 gears. Every gear has fixed amount of teeth:
    n1 = 9, n2 = 15, n3 = 8, n4 = 16
    frequency/speed of the first gear is w = 5 rounds/sec 
    
    So the task is to find out the speed of rotation (T),
    of the fourth gear.

    Alternative calculation:
    we can assighn Tn as T2=(T1*Z1/Z2)....T4
    https://www.youtube.com/watch?v=2XheMMd_A90&ab_channel=%/
    D0%90%D0%BD%D0%B4%D1%80%D1%96%D0%B9%D0%86%D1%81%D0%B0%D0%BA
'''


def gear_wheel(w):
    n1 = 9
    n2 = 15
    n3 = 8
    n4 = 16
    T = 1/(w*((n1/n2)*(n3/n3)*(n3/n4)))
    return f'{round(float(T), 2)} rounds/sec'


w = int(input('Select a speed of the first wheel: '))
print(gear_wheel(w))
