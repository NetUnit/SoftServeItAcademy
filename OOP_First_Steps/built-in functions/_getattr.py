class Person:

    '''
    ===================================================================
    This class represents methods to test * getattr() built-in function
    ===================================================================

    The getattr() method returns the value of the named attribute of an
    object. If not found, it returns the default value provided to the 
    function.

    :param obj: object whose named attribute's value is to be returned
    :param name: string that contains the attribute's name
    :param default: value that is returned when the named attribute is 
     not found

    :type obj: <class 'type'>
    :type name: str
    :type value: int, float, str, ...

    :raises: raises an AttributeError when the object has no such attribute
    '''

    id = 10
    salary = 5000

    def __init__(self, id=id, salary=salary):
        self.id = id
        self.salary = salary

    def _getattr(self, name, default=None):
        return getattr(self, name, default)


if __name__ == "__main__":
    instance = Person()
    print(instance._getattr('salary'))
    # >>> 5000

    print(instance._getattr('id'))
    # >>> 10

    # getattr() when named attribute is not found
    try:
        attr = 'position'
        print(getattr(instance, attr))
    except:
        print(f'This is attribute error: \'{attr}\' wasn\'t found')

    # get unknown parameter with default value if not found
    print(getattr(instance, attr, 'manager'))
