class Person:

    '''
    setattr() function sets the value of the attribute of an obje
    setattr(obj, name, value) - takes 3 parameters

    :param obj: object whose attribute has to be set
    :param name: attribute name
    :param value: value given to the attribute


    :type obj: <class 'type'>
    :type name: str
    :type value: int, float, str, ...

    .. note:: can be useful to emphasize
        this attr will be assigned inside class, 
        however in mappingproxy() obj it will be the last
    '''

    id = 10
    salary = 5000

    def __init__(self, id=id, salary=salary):
        self.id = id
        self.salary = salary

    def _setattr(self):
        setattr(self, 'money', 100000)

instance = Person()
instance._setattr()
print(instance.__dict__)
# >>> {'id': 10, 'salary': 5000, 'money': 100000}