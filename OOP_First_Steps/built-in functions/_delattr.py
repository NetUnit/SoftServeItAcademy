class User:

    '''
    ===================================================================
    This class represents methods to test * delattr() built-in function
    ===================================================================

    The delattr() deletes an attribute from the object (if the object 
    allows it).

    delattr() takes two parameters:

    :param obj: object whose named attribute's value is to be returned
    :param name: string that contains the attribute's name

    :type obj: <class 'type'>
    :type name: str

    :raises: raises an AttributeError saying the object has no such attribute
    '''

    id = 7
    username = 'JohnyD'
    email = 'JohnyDx64@gmail.com'

    def __init__(self, id=id, username=username, email=email):
        self.id = id
        self.username = username
        self.email = email

    def _delattr(self, param):
        print(self.__dict__)
        return delattr(self, param)

if __name__ == "__main__":
    user = User()
    print(user.__dict__)
    # {'id': 7, 'username': 'JohnyD', 'email': 'JohnyDx64@gmail.com'}
    print(user._delattr('email'))
    print(user.__dict__)
    # >>> {'id': 7, 'username': 'JohnyD'}

    # delattr() when named attribute is not found
    try:
        attr = 'first_name'
        delattr(user, attr)
    except:
        print(f'Cannot delete attribute: \'{attr}\' wasn\'t found')
