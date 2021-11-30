import time

'''
    Інкапсуляція - надання атрибутуб об'єкту
    локального значення всередині класуб з метою
    уиникнення помилок. Для того щоб зона застосуваня
    цього атрибуту був чітко обмежений клас
'''
'''
## variant 1
class A:

    counter = 0;

    def __init__(self):
        A.counter += 1
    
count1 = A()
time.sleep(0.5)
print(count1.counter)
count1 = A()
time.sleep(0.5)
print(count1.counter)
count1 = A()
time.sleep(0.5)
print(count1.counter)
count1 = A()
time.sleep(0.5)
print(count1.counter)
count1 = A()
time.sleep(0.5)
print(count1.counter)

### проте якщо поза класом змніти значення counter звернувшись
### до атрибуту від імені класу то це призведе до збою всередині класу
A.counter = 88
count1 = A()
time.sleep(0.5)
print(count1.counter)
'''
### вивід буде >>> 89, тобто наш лічильник збився
'''
    тому щоб інкапсулювати цей атрибут
    в області дії цього класу використовується
    agreement - атрибут буде доствпний тільки всередині класу
'''


class B:
    __counter = 0
    def __init__(self):
        B.__counter += 1

        
count1 = B()
time.sleep(0.5)
print(count1.__counter)
##AttributeError: 'B' object has no attribute '__counter'


'''
    Щоб знову оримати доступ до об'єкта,
    потрбіно виконати:  B._B__counter:

    або 
'''