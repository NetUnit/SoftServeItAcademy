'''
    There is a class Person, the designer of which accepts three 
    parameters (not taking into account self) - the name, surname 
    and qualification of the specialist. The qualification has a 
    default value of one.

    The Person class has a method that returns a string that includes
     all the information about the employee.

    The Person class contains a destructor that displays the phrase "Goodbye, Mr.…"
     (instead of a colon, the name and surname of the object should be displayed).

    In the main branch of the program, create three objects of the Person class. 
    Look at the information about employees and fire the weakest link.

    At the end of the program, add the input () function so that the script does 
    not complete itself until Enter is pressed. Otherwise, you will immediately 
    see how all objects are deleted at the end of the program.
'''


class Person:

    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.qualification = q

    def show_info(self):
        # return f'Employee info: name - {self.name}, surname - {self.surname}, qualification - {self.qualification}'
        return 'Employee info: name - %s, surname - %s, qualification - %d' % (
                                   self.name, self.surname, self.qualification)


class Dismiss(Person):

    def __del__(self):
        print('Good bye mr. %s %s' % (self.name, self.surname))


# creating 3 objects
person1 = Person('Tim', 'Morrison')
person2 = Person('Stacey', 'Ashcroft')
person3 = Person('Mike', 'Johnson')

# display info
print(person1.show_info())
print(person2.show_info())
print(person3.show_info())

# dismiss employee (but beeing offensive to women)
dismiss = Dismiss(person2.name, person2.surname)
del dismiss
