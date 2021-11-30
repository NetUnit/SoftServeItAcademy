'''
    Припустимо є 2 стандартні типи:
    int і str. type(int) - вбудований клас Python
               type(str) - вбудований клас Python
'''

## прналежність до класів
print(type(str))  ## <class 'type'>
print(type(int)) ## <class 'type'>

################################################ Поліморфізм #######################################################
### example1
### return methods
'''
class Summation:

    a = 0;
    b = 0;

    def __init__(self, a=a, b=b):
        self.a = a
        self.b = a
    
    def behaviour(self, a=a, b=b):
        return int(a) + int(b)

class Concatenation:

    a = 0;
    b = 0;

    def __init__(self, a=a, b=b):
        self.a = a
        self.b = b

    def behaviour(self, a, b):
        return str(a) + str(b)

# створення екземплярів класу
instance_1 =  Summation()
instance_2 = Concatenation()

# надання екзмплярам атрибутів
print(instance_1.behaviour(10, 10)) ### 20
print(instance_2.behaviour(10, 10)) ### '1010'
'''

'''
### Example 2
class classA:
    a = 0; b = 0; c = 0;
    def __init__(self, a=a, b=b, *args):
        self.a = a
        self.b = b
    
    def behaviour(self, *args):
        if len(args) == 3:
            return 'This is triangle'
            # arithmetics
            #p = (a + b + c) * 0.5
            #s = (p * (p - a) * (p -b) * (p - c )) ** 0.5
            # return s
        else:
            return 'This is rectangle'
            # arithmetics
            # p = a * b
            #return p

# клас буде поводити себе по іншому у відповідності до введених параметрів
inst = classA()
print(inst.behaviour(2, 4, 5))
print(inst.behaviour(2, 4, 5, 5))

### Example3 в залежності від логіки юзера
'''

'''
## complex
## Перевизначення класу
## example 2
## return a, b - різниця
class Complex:
    
    a = 0;
    b = 0;
    counter = 0;
    def __init__(self, a, b):
        Complex.counter += 1
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return a, b
        #return Complex(a, b)

# створення об'єкта класу, який відповідає типу класу Complex()
instance_c1 = Complex(50, 50)
print(Complex.counter)
instance_c2 = Complex(50, 50)
print(Complex.counter)
print(instance_c1 + instance_c2)

## нерівні
#equals = instance_c1 == instance_c2
# print(equals)

## рівні
print(Complex==Complex)

print(instance_c1)
print(instance_c2)
'''

'''
## return Point()
class Point:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Point(x, y, z)


p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)

## витягуємо атрибути ## p1
print(getattr(p1, 'x'))
print(getattr(p1, 'y'))
print(getattr(p1, 'z'))

## витягуємо атрибути ## p2
print(getattr(p2, 'x'))
print(getattr(p2, 'y'))
print(getattr(p2, 'z'))

## пробуємо додати instancu 
print(p1 + p2) ### >>> <__main__.Point object at 0x000001C086C1F820>
'''



### Example 4
### @ classmethod 
### @ staticmethod
#####################################
class Human:
    # Атрибут класу
    species = "Homosapiens"
    name = 'Jacky'
    # Конструктор
    def __init__(self, name=name):
        self.name = name
    
    #метод екземпляру класу
    def say(self, msg):
        return "{name}>>> {message}".format(name=self.name, message=msg)
    
    # Метод класу
    @classmethod
    def get_species(cls):
        return cls.name
    # Статичний метод викликається без посилання на класс чи екземпляр
    @staticmethod
    def grunt():
        return "*Static*"

instance = Human()

# classmethod
# @classmethod - це звичайний метод класу, що має доступ до всіх атрибутам класу, 
# через який він був визван. Следовательно, classmethod - це метод, який прив'язується
# до класу, а не до екземпляру класу
print(Human.get_species())

# staticmethod - метод без параметру self, можна викликати поза класом за допомогою будь-якого instance
# @staticmethod використовується, коли ми хочемо повернтуи одне і те ж, незалежно від викликаного дочірнього класу
print(Human.grunt()) ## функція всередині класу котру можна викликати як від екз так і від самого класу
print(instance.grunt())

# method say
print(instance.say('say something'))

'''
class Summation:

    a = 0;
    b = 0;

    def __init__(self, a=a, b=b):
        self.a = a
        self.b = a
    
    def behaviour(self, c, a=a, b=b):
        return int(a) + int(b)

    def behaviour(self, a=a, b=b):
        return str(a) + str(b)


a = Summation()
print(a.behaviour(10, 10, 10))

b = Summation()
print(a.behaviour('10', '10'))

#print(Summation())
#print(Summation())
'''




