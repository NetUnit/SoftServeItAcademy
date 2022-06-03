'''
    Supposingly we have 2 python default types:
    int & str. type(int), type(str) etc. - built-in Python class
'''

## belonging to classes
# print(type(str))  ## <class 'type'>
# print(type(int)) ## <class 'type'>

################################## *** Polymorphism *** ##################################
# ex1
# return methods
class Behaviour:

    a = 0;
    b = 0;

    def __init__(self, a=a, b=b):
        self.a = a
        self.b = a
    
    def summation(self, a=a, b=b):
        return int(a) + int(b)

    def concatenation(self, a=a, b=b):
        return str(a) + str(b)

    def behaviour(self, a=a, b=b):
        if list(map(int, [a, b])):
            return a + b
        if list(map(str, [a, b])):
            return f"'{a + b}'"

## ex2 redefine clasess
# return a, b - difference
class Complex:
    
    # a = 0;
    # b = 0;

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return a, b
        #return Complex(a, b)

# return Point()
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


if __name__ == "__main__":
    
    # ex1
    # the same class has different behavioural features
    # instantiating classes
    instance_1 =  Behaviour()
    instance_2 = Behaviour()

    # assign class attributes
    print(instance_1.summation(10, 10)) # >>> 20
    print(instance_2.concatenation(10, 10)) # >>> '1010'
    print(instance_2.behaviour('10', '20'))
    print(instance_2.behaviour(10, 20))

    # ex2
    # summation of complex numbers
    instance_c1 = Complex(50, 50)
    instance_c2 = Complex(20, 20)
    print(instance_c1 + instance_c2)

    # ex3
    # create matrix from points
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)

    # get attributes from p1 instance
    print(getattr(p1, 'x'))
    print(getattr(p1, 'y'))
    print(getattr(p1, 'z'))

    # get attributes from p2 instance
    print(getattr(p2, 'x'))
    print(getattr(p2, 'y'))
    print(getattr(p2, 'z'))

    # adding instances
    p = (p1 + p2) ### >>> <__main__.Point object at 0x000001C086C1F820>
    print(getattr(p, 'x'))
    print(getattr(p, 'y'))
    print(getattr(p, 'z'))