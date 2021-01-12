'''
    it's a simple fucntion that 
    calulates koligrames of fuel 
    after the into-plane operation
'''


def PMM(data):
    V = data[0]
    density = data[1]
    M = V * (density/1000)
    return M


try:
    data = list(map(float, input(
        'Type the capacity of oil and density through space: ').split()))
    print(f'{round(PMM(data), 2)} кг')
except ValueError:
    print('Please. Enter a correct data through space')
except IndexError:
    print('Enter provide 2 values: capacity/density')
