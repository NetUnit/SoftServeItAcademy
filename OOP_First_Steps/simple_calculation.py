'''
    Simple calculation of two digits
'''


# var1 - using ready-made attributes
# from the class
class ClassA:

    x = 4
    y = 8

    def __init__(self, x=x, y=y):
        self.x = x
        self.y = y

    def execution(self):
        return self.x * self.y


exempliar = ClassA()
print(exempliar.execution())


# var2 - using set-up attributes
# changing attributes in the function
class ClassA:

    x = 4
    y = 8

    def __init__(self, x=x, y=y):
        self.x = x
        self.y = y

    def execution(self):
        return self.x * self.y


exempliar = ClassA(4, 10)
print(exempliar.execution())


# var3 - calling through two different
# instances with two different Values
class classA:

    x = 4
    y = 8

    def __init__(self, x=x, y=y):
        self.x = x
        self.y = y

    def execution(self, x, y):
        return x * y


instance1 = classA()
instance2 = classA()

print(instance1 .execution(4, 8))
# using getattr() - to call the instance
print(getattr(instance2, 'execution')(5, 10))
