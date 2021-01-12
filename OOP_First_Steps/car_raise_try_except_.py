'''
    There is a plant that produce vehicles
    The price of the body - 5000 usd.

    Apart of body there are 2 comlectations
        1) 'standart'
        2) 'improved' 

    Standart complectation depend on color:

        regular color - standart price
        carbon covering adds 5% to a price of the car

    Improved complectation - possess the same features
    
    As regards items of complectation:
        1 wheel - 125 usd
        1 cahir - 105 usd
        body - 5000 usd

    3 next classes work in the same way,
    but the algorithm is different

'''


class Car:

    body = 5000
    wheel = 125
    seat = 105
    owner = 'Adam'
    price = wheel*4 + seat*4 + body

    def __init__(self, wheel=wheel, body=body, seat=seat, owner=owner, price=price):
        self.wheel = wheel
        self.body = body
        self.seat = seat
        self.owner = owner
        self.price = price

    # stanadart complectation method
    # всі параметри передані сюди будуть,
    def standart_complectation(self, color, body=body, owner=owner, wheel=wheel, seat=seat, price=price):

        return f'The owner of the car is {owner}, the price is {price} usd' if color != 'carbon' \
            else f'The owner of the car is {owner}, the price is {price * 1.05} usd'  # як атрибути екземпляра

    # improved complectation method
    def improved_complectation(self, color, body=body, owner=owner, wheel=wheel, seat=seat, climate_control=350, price=price):

        return f'The owner of the car is {owner}, the price is {price + climate_control} usd' if color != 'carbon' \
            else f'The owner of the car is {owner}, the price is {(price*1.05) + climate_control} usd'


# var1 - raise an error and fix with try when user is typing improper data
# no additional trials here, program ends afetr the firts good/bad/typing
class SelectionOne(Car):

    complectation = Car()
    color_selection = 'Please select the color of the car: '

    st_list = ['Standart', 'standart', 'regular', 'simple']
    impr_list = ['Improved', 'Better', 'Luxurious']

    def __init__(self, color_selection=color_selection, st_list=st_list, impr_list=impr_list, complectation=complectation):
        self.color_selection = color_selection
        self.st_list = st_list
        self.impr_list = impr_list
        self.complectation = complectation

    def choice(self, color_selection=color_selection, st_list=st_list, impr_list=impr_list, complectation=complectation):

        extended = st_list + impr_list
        compl_selection = input(
            'What type of complectation do U prefer: Standart/Improved?: ')

        try:
            if compl_selection in extended:
                return complectation.improved_complectation(input(color_selection)) if \
                    compl_selection in st_list else \
                    complectation.standart_complectation(
                        input(color_selection))
            else:
                raise TypeError('OOOPS. Bad input')
        except TypeError as error:
            return 'Seem\'s like U haven\'еnt provided the right choice. Please select the data again'


instance = Selection_1()
print(instance.choice())


# var2 - no exceptions here, however there is a cycle that repeats when program get's
# bad input using while loop. Allows some range of st/impr words
class SelectionSecond(Car):

    complectation = Car()

    st_list = ['Standart', 'standart', 'regular']
    impr_list = ['Improved', 'Better', 'Luxurious']
    compl_selection = 'What type of complectation do U prefer: Standart/Improved?: '
    color_selection = 'Please select the color of the car: '
    n = 0

    def __init__(self, complectation=complectation, compl_selection=compl_selection, color_selection=color_selection, st_list=st_list, impr_list=impr_list, n=n):
        self.compl_selection = compl_selection
        self.color_selection = color_selection
        self.st_list = st_list
        self.impr_list = impr_list
        self.n = n

    def select_compl(self, complectation=complectation, color_selection=color_selection, st_list=st_list, impr_list=impr_list, n=n):
        while n < 3:
            n = n + 1
            compl_selection = input(
                'What type of complectation do U prefer: Standart/Improved?: ')
            if compl_selection in st_list:
                return complectation.standart_complectation(input(color_selection))

            elif compl_selection in impr_list:
                return complectation.improved_complectation(input(color_selection))

            else:
                if n == 3:
                    return 'You haven\'t provided a correct answer'
                else:
                    print('Please select the proper complectation')
                    pass


instance = SelectionSecond()
print(instance.select_compl())


# var3 - no exceptions here, however there is a loop for that
# to awoid mistakes from user when bad input, loop is in the class
class SelectionThree(Car):

    complectation = Car()
    color_selection = 'Please select the color of the car: '
    compl_selection = 'What type of complectation do U prefer: Standart/Improved?: '

    st_tuple = ('Standart', 'standart', 'regular')
    impr_tuple = ('Improved', 'Better', 'Luxurious')

    color = 'Please select the color of the car: '
    inquiry = input('What type of complectation do U prefer: ')

    if inquiry in st_tuple:
        print(complectation.standart_complectation(input(color)))
    elif inquiry in impr_tuple:
        print(complectation.improved_complectation(input(color)))
    else:
        for i in range(2):
            print('Please select the proper complectation: ')
            inquiry = input('What type of complectation do U prefer: ')

            if inquiry in st_tuple:
                print(complectation.standart_complectation(input(color)))
                break
            elif inquiry in impr_tuple:
                print(complectation.improved_complectation(input(color)))
                break
            else:
                if i == 1:
                    print('U haven\'t provided a proper answer')
                else:
                    pass


instance = SelectionThree()
