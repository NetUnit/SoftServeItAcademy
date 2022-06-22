class GetTestArgs():
    
    '''
    ==================================================================
    This class represents methods to test * args 'Special Symbols'
    ==================================================================

    if we do not know exactly how many arguments passed to the function
    we use Arbitrary Arguments = * args

    "Args" is just a set of characters that are used to denote arguments.
    The main thing here is the operator *

    * args - created to identify that a function can have multiple arguments.
    the * args parameter at the top of the function means that the number of 
    arguments passed can be N when entering for example 2 or more arguments
    for example: https://prnt.sc/uko8ld
    https://habr.com/ru/company/ruvds/blog/482464/

    .. note::

        * args (Non Keyword Arguments)
        ** kwargs (Keyword Arguments)

        * https://www.w3schools.com/python/gloss_python_dictionary_add_item.asp
          https://prnt.sc/uko8ld 

    '''
    def max_min_number(self, *numbers):
        return max(numbers)

    def test_kids(self, *kids):
        return ("The youngest child is " + kids[1])

    def args_arithmetic_mean(self, *args):
        '''
        digits1, digits2 are basically abstract parameters and
        passed inside args, however we can call them if we passed
        the actual parameter name
        '''
        lst1 = list(map(int, digits1))
        print (sum(lst1)/len(lst1))

        lst2 = [int(i) for i in str(digits2)]
        return sum(lst2)/len(lst2)
    
    def some_args(self, *args):
        '''
        args is a tuple of params
        we can refer to it's value by variable name
        for instance ('100500',)
        '''
        return param1


class GetTestKwargs():
    '''
    ==================================================================
    This class represents methods to test * kwargs 'Special Symbols'
    ==================================================================

        ** is the double asterisk before the parameter name used to denote
            this type of argument. The arguments are passed as a dictionary
            and these arguments make a dictionary inside function with name
            same as the parameter excluding double asterisk 

            Key-value pairs will be assigned  as keyword parameters

            .. note::
                We can pass the whole dictionary annotated with ** symbols,
                in order to read key-value pairs of this dict().
    '''
    def print_pet_names(self, owner, **pets):
        print(f"Owner Name: {owner}")
        for pet, name in pets.items():
            print(f"{pet}: {name}")

    def test_2(self, username=None, **kwargs):
        '''
        now we can refer to a parameter we want with
        kwargs.get(parameter)
        '''
        print(username)
        name = kwargs.get('name')
        return print(name)

if __name__ == "__main__":
    # test args
    args_inst = GetTestArgs()
    print(args_inst.max_min_number(1, 2, 3, 4, 5))
    print(args_inst.test_kids("Emil", "Tobias", "Linus"))
    digits1 = input('Enter your the firts aisle of digits: ')
    digits2 = input('Enter the second aisle of digits: ')
    print(args_inst.args_arithmetic_mean(digits1, digits2))
    param1 = '100500'
    print(args_inst.some_args(param1))

    # test kwargs
    kwargs_inst = GetTestKwargs()
    kwargs_inst.print_pet_names(
        "Jonathan", 
        dog="Brock",
        fish=["Larry", "Curly", "Moe"],
        turtle="Shelldon"
    )
    paramaters = {'id': 1, 'name': 'John', 'surname': 'Doe'}
    kwargs_inst.test_2(username='NetUnit', **paramaters)
