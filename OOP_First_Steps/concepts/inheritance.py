'''
    #4 унаслідування атрибутів одного МЕТОДУ - В ІНШИЙ

    1) заассайнити змінну яку повертаємо через return,
       в глобальний простір
    
        attribute1 = self.attribute1

    2) передати змінну self.attribute як інший атрибут,
       self.attribute1 = parameter
'''
'''
class A():
    
	x = 5; y = 3;

	def method1(self, x=x, y=y): ## множення
		self.x = x
		self.y = y
		self.multipl = x * y                                                                   
		return self.multipl                                                               

	def method2(self, x=x, y=y): ## віднімання	            # multipl = self.multipl		                      
		subtraction = x - y                
		return subtraction

instance = A()

print(instance.method1(15, 15))
print(instance.method2(15, 15))
'''

'''
    ЕКЗЕМПЛЯР КЛАСУ ЦЕ - ГЛОБАЛЬНИЙ ОБ'ЄКТ, ЩО МОЖНА ВИКЛИКАТИ ВСЕРЕДИНІ
    ІНШОГО КЛАСУ І ВІН ТАКИМ ЧИНОМ ВШИЄТЬСЯ В ЦЕЙ КЛАС, І ТОДІ ВЖЕ ВІД instance, 
    викликаємо будь-який атрибут з іншого класу 

     ОБЄКТ - 
'''

### наслідування - без передачі класу А в клас B 
### instances B - не відбудуться
class A:

    a = 10; b = 20;

    def __init__(self, a=a, b=b):
        self.a = a
        self.b = b
    
    def calc(self, a=a, b=b):
        # multipliacation
        mult = a * b
        return mult
# без передачі Class A в Сlass B
# instance_b - не виконається
class B(A):
    # class B launch class A
    pass


instance_a = A()
print(instance_a.calc(15, 10))
###>>> 200

instance_b = B()
print(instance_b.calc())
###>>> 200

### клас B унаслідує A: а трибути  і поведінку класа А (метод calc d і атрибути a=10, b=20)
print(instance_b.a)

