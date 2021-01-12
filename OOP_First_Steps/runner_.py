'''
    In this program we get an inquiry to measure
    the distance that a fast runner will cover

    Usid try-except-raise also to catch some 
    bad inputs. 

    Due to the fact that jogging is mostly even,
    we added a small index of acceleration in order
    to increase the coverage. Making it slow 
    uniformly accelerated
'''

#  var1 method in the class
# method call


class Runner:

    V_zero = 0
    a = 0.225
    T = 180

    def __init__(self, V_zero=V_zero, a=a, T=T):
        self.V_zero = V_zero
        self.T = T
        self.a = a

    def distance(self, V_zero, a, T):
        S = V_zero * T + (a * T**2)/2
        return f'{S} metres'


exempliar = Runner()
print(exempliar.distance(0, 0.225, 180))


#  var2 calling through the class
class Runner:

    V_zero = 0
    a = 0.225
    T = 180

    def __init__(self, V_zero=V_zero, a=a, T=T):
        self.V_zero = V_zero
        self.T = T
        self.a = a

    def distance(self):
        S = self.V_zero * self.T + (self.a * self.T**2)/2
        return f'{S} metres'


exempliar = Runner(0, 0.225, 180)
print(exempliar.distance())


# var3 separated classes
class Runner:

    V_zero = 0
    a = 0.0225
    T = 300

    def __init__(self, V_zero=V_zero, a=a, T=T):
        self.V_zero = V_zero
        self.T = T
        self.a = a


class Distance(Runner):
    def distance(self, V_zero=0, a=Runner.a, T=Runner.T, n=0):
        while n < 3:

            try:
                V_zero = int(
                    input('Введіть будь-ласка початкову швидкість бігуна: '))
            except ValueError:
                print('Please select a proper start-speed!')
                n = n + 1
                if n == 3:
                    return 'U haven\'t selected a proper answer'
                else:
                    continue

            S = V_zero * T + (a * T**2)/2
            return f'{S} metres'


exempliar = Distance()
print(exempliar.distance())
