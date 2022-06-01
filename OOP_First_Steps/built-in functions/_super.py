'''
    super() - метод, який поверне
    проксі-об'єкт, методи якого 
    шукатимуться лише у класах,
    що стоять раніше, ніж він, 
    у порядку MRO.

    метод буде шукатися у всіх класах,
    незалежно від порядку
'''


class Base:
    def price(self):
        return 10

instance1 = Base()
print(instance1.price())
## >>> 10

class InterFoo(Base):
    def price2(self):
        ## price() - метод який є у класі Base, тому його значення буде --> 10 ---> 10 * 1.1 = 11
        return super().price() * 1.1

instance2 = InterFoo()
print(instance2.price2())
## >>> 11.0

class Discount(InterFoo):
    def price3(self):
        ## price2() - метод який є у класі InterFoo, тому його значення буде --> 11 ---> 11 * 0.8 = 8.8
        return super().price2() * 0.8

instance3 = Discount()
print(instance3.price3())
## >>> 8.8


'''
    якщо ж в параметрах super() - 
    вказаний інший клас то відповідно,
    проксі об'єкт - результат виконання методу,
    повернеться саме з вказаного класу
'''

class InterFoo2(InterFoo):
    def price2(self):
        ## price() - метод який є у класі Base, тому його значення буде --> 11 ---> 11 * 1.1 = 11
        # return super().price() * 1.1 # --> потягне метод з Base
        return super().price2() * 1.1  # --> потягне метод з InterState

instance4 = InterFoo2()
print(instance4.price2())


class Model1():
    a = 5
    b = 10

    def __init__(self, a=a, b=b):
        self.a = a
        self.b = b

    def func(self):
        return self.a * self.b


obj1 = Model1()
print(obj1.a)
print(obj1.b)


class Model2(Model1):


    def __init__(self):
        super().__init__(a=self.a, b=self.b)

    def func2(self):
        return self.a * self.b



obj2 = Model2()
print(obj2.a)
print(obj2.b)

print(obj2.func())
### >>> 50 (5*10)
