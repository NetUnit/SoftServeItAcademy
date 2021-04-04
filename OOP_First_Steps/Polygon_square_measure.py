import numpy as np
from math import sqrt
import copy
import time

# classwork1 'class Polygon' - SoftServe#9 - Lesson9 OOP


'''
    All of our geometrical fugures 
    can be also irregular apart of the 
    triangle

    https://uk.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0_\
    %D0%BF%D0%BB%D0%BE%D1%89%D1%96_%D0%93%D0%B0%D1%83%D1%81%D1%81%D0%B0

    To measure te square we should,
    setup coords and use math:
    square = ((x1y2 + x2y3 + x3y1) - x2y1 - x3y2 - x1y3) * 0.5
    for in range len(lst):

    square = |((x1y2 + x(n+1)y(n+1) + x(n)y1 - x2y1 - x(n+1)y(n+1) - x1y(n)) * 0.5| - modulo

    var3 - we select the figure, pyhon call the specific function
'''


# var1 - we are selecting coords and algorithm will detect the figure
class Polygon():

    # considered that this data came from the database in list format
    polygon = ['Triangle', 'Rectangle',
               'Pentagon', 'Hexagon',
               'Septagon', 'Octagon',
               'Nonagon', 'Decagon']

    error1 = 'incompatible order of input'
    error2 = 'please provide correct data for calculations'
    error3 = 'the program is over'

    def __init__(self, polygon=polygon, error1=error1, error2=error2, error3=error3):
        self.polygon = polygon
        self.error1 = error1
        self.error2 = error2
        self.error3 = error3

    # reassighn polygon as a dict (considering json format)
    def __add__(self, polygon):
        self.polygon = polygon.dict(enumerate(polygon))

    def set_coords(self, polygon=polygon, error1=error1, error2=error2):

        try:
            axis_x = list(map(float, input(
                'Please select the abscissa coords of each point: ').split()))
            self.axis_x = axis_x

            axis_y = list(map(float, input(
                'Please select the ordinat coords of each point: ').split()))
            self.axis_y = axis_y

            if len(axis_x) == len(axis_y):
                obj = polygon[int(len(axis_x))-3]
                self.obj = obj

                return 'Your geometrical figure is %s. The coords x are: %r, the coords y are: %r' % (obj, axis_x, axis_y)

            else:
                return error1.upper()

        except:
            return error2.upper()

    def calculation(self):
        try:
            axis_x = self.axis_x
            axis_y = self.axis_y

            # making deepcopies of axis 1, 0 points
            dp_axis_x = copy.deepcopy(axis_x)
            dp_axis_y = copy.deepcopy(axis_y)

            # convert abscissa coordinates
            axis_x.append(axis_x[0])
            axis_x.remove(axis_x[0])

            # convert ordinat coordinates
            axis_y.append(axis_y[0])
            axis_y.remove(axis_y[0])

            calc = abs(sum([a * b for a, b in list(zip(dp_axis_x, axis_y))]) - sum(
                [a*b for a, b in list(zip(axis_x, dp_axis_y))])) * 0.5

            self.calc = calc
            return f'The squre of a {self.obj} is {calc} cm2'
        except AttributeError:
            print(self.error3.upper())

            sec = 2
            while sec > 0:
                print('...')
                time.sleep(0.5)
                sec -= 1
            return '...'


instance = Polygon()

print(instance.set_coords())
print(instance.calculation())


'''
    In this case, we put bad input scenario
    to the 2nd Class, it'll decide
    whether to launch calculation or not

    We can also use only one button here, 
    to launch a program
'''


# var2
class Polygon():
    '''
    In this case, we put bad input scenario
    to the 2nd Class, it'll decide
    whether to launch calculation or not

    We can also use only one button here, 
    to launch a program
    '''

    # considered that this data came from the database in list format
    polygon = ['Triangle', 'Rectangle',
               'Pentagon', 'Hexagon',
               'Septagon', 'Octagon',
               'Nonagon', 'Decagon']

    error1 = 'incompatible order if input'
    error2 = 'please provide correct data for calculations'
    error3 = 'the program is over'

    def __init__(self, polygon=polygon, error1=error1, error2=error2,
                 error3=error3):
        self.polygon = polygon
        self.error1 = error1
        self.error2 = error2
        self.error3 = error3

    # reassighn polygon as a dict (considering json format)
    def __add__(self, polygon):
        self.polygon = polygon.dict(enumerate(polygon))

    def set_coords(self, polygon=polygon, error1=error1,
                   error2=error2):

        axis_x = list(map(float, input(
            'Please select the abscissa coords of each point: '
                                                    ).split()))
        self.axis_x = axis_x

        axis_y = list(map(float, input(
            'Please select the ordinat coords of each point: '
                                                   ).split()))
        self.axis_y = axis_y

        # BUG ######################### is here if 2 = 2-3 = -1 index
        obj = polygon[int(len(axis_x))-3]
        self.obj = obj

        return 'Your geometrical figure is %s. The coords x \
are: %r, the coords y are: %r' % (obj, axis_x, axis_y) if len(
                    axis_x) == len(axis_y) else error1.upper()

    def calculation(self):

        axis_x = self.axis_x
        axis_y = self.axis_y

        # making deepcopies of axis 1, 0 points
        dp_axis_x = copy.deepcopy(axis_x)
        dp_axis_y = copy.deepcopy(axis_y)

        # convert abscissa coordinates
        axis_x.append(axis_x[0])
        axis_x.remove(axis_x[0])

        # convert ordinat coordinates
        axis_y.append(axis_y[0])
        axis_y.remove(axis_y[0])

        calc = abs(sum([a * b for a, b in list(zip(dp_axis_x, axis_y))]) -
                   sum([a*b for a, b in list(zip(axis_x, dp_axis_y))])) * 0.5

        self.calc = calc

        return f'The square of a {self.obj} is {calc} cm2'


class Launch(Polygon):

    instance = Polygon()

    try:
        print(instance.set_coords())
        # беремо значення з класу для порівння - як об'кт в памяті, але кторий не викликається
        if instance.set_coords != instance.error1.upper():
            print(instance.calculation())
        else:
            pass

    except:
        print(instance.error2.upper())

        sec = 2
        while sec > 0:
            print('...')
            time.sleep(0.5)
            sec -= 1
        print(instance.error3.upper())


Launch()
