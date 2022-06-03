Типи даних:

	MUTABLE:
			- list, set, dict  and user-defined classes

	IMMUTABLE:
			- int, float, decimal, bool, str, tuple, and range




	Атомарні типи даних:  'при призначенні атомарного об\'єкта копіюється його значення, при призначенні посилального об\'єкта копіюється посилання'.
	Ссилочні типи даних: 



# ОПЕРАТОРИ - Keywords

del - оператор (keyword) широкого призначення, який видаляє як цілі об'єкти так і їх окремі частини (класи, списки, змінні)'
	видалає привязку цього імені, списку як з локального так і глобального простору імен

	def del_object(object): 
    	object = list(map(lambda x: x, input('Type some elements here with no spaces: ')))
    	del object[0]  # видалить першу частину списку
    	#del object[0:2] # видалить частину списку яка зріжеться
    	return object




// - ділення без остачі

	def divsion_round(object):
		return object//2

	>>> 5//2=2
	>>> 1//2=0

	Ділення без остачі меншого числа поверне 0!!



# ЦИКЛИ

'''
	Основна відмінність в циклах полягає в тому, що цикл while - ПРАЦЮЄ НЕПЕРЕРВНО ДО ПЕВНОЇ УМОВИ
													цикл for - ПРАЦЮЄ N - КІЛЬКІСТЬ ПОВТОРЕНЬ == кількість ітерованих елементів 

'''

# ЦИКЛ for - ВІДОМИЙ ДІАПАЗОН ВИКОНАННЯ

	## цикли for застосовуються в 3ьох основних випадках
for - цикл, застосовується для того, щоб перебрати елементи ітерабельного об'єкта
for - цикл, викликає почерговий запуск функції next()
for - цикл, без виконання вийнятку - StopIteration, після останньї вдалої ітерації


 - 'i' - елемент ітерабельного ОБ'ЄКТА, ПОЧЕРГОВИЙ ПРОХІД ПО СВОЇХ ЕЛЕМЕНТАХ
 - 'i' - кількість разів виконання певної логіки, дії, формули
 - 'i' - елемент ітерабельного об'єкта 'i' може виступати як АРГУМЕНТ в АЛГОРИТМІ ТІЛА ЦИКЛУ

    Ітерабельні об'єкти:
        - list, tuple, set
        - range()
        - str

		!!! int не є ітерованим об'єктом, так як в памяті він представляється як однорідний об'єкт

		цикл for - викликає почерговий запуск функції next()
		до її останнього значення, тобто логічного завершення
		не видаючи в кінці вийняток StopIteration

		# структура циклу for:

		for <variable> in <object-iterator>:
    		<body>

		<end of the loop> # ЯКЩО ХОЧЕМО ВИВЕЧТИ ОСТАННЄ ЗНАЧЕННЯ - ВИПСУЄМО RETURN НА РІВНІ ЛІНІЙКИ <end of the loop>

		де, 
		    <variable> - умовна змінна - елемент об'єкта-ітератора (ітерабельного об'єкта)
		             зазвичай умовною змінною є символ 'i' або 'item' (можна використовувати будь-яку іншу назву)
		    <object-iterator> - ітерабельний об'єкт або дані, які містять ітерабельні елементи: - list, tuple, set. range(). str
		    
		    <body> - тіло циклу, тіло циклу пишеться на відступах 4 відступи
		            !!! тіло циклу повинно бути обовязково

		    <end of the loop> - за замовчуванням буде, останнім елементом ітерації в списку
		    print(i) - виведе останній елемент в ітерабельному об'єкті 

		-'i' - елемент ітерабельного об'єкта - ITEM
			
			for i in range(1, 10):
				print(i)

		-'i' - КОМПОНЕНТ ЛІЧИЛЬНИКА - кількість разів виконання певної логіки, дії, формули (для прикладу сума всіх елементів послідовності range())
			
			s=0
			for i in range(1, 10):
				s += i
				print(s)

		-'i' - АРГУМЕНТ в АЛГОРИТМІ ТІЛА ЦИКЛУ (який змінює основну змінну)

			var=2

			for i in range(1, input()):
				print(var**i)


	# Оператори в циклах:

	pass - 
	NOTHING HAPPENS


	continue - пропускає виконання дії прописаної в заданій умові
	ALLOWS SKIPPING SOME PART OF A LOOP
	Для прикладу якщо ми хочемо щоб щось добавтлося, вивелося або відбулося, в тіло цієї умови проставляєтьс coninue і цикл прямує до наступної умови, дії
	
		for i in 'hello world':
    		if i == 'o':
        		continue # якщо буде pass замість continue, то все ітерація не пропуститься
    		print(i * 2, end='')

    		>>> 'hheellll  wwrrlldd' - одразу закінчить цикл і передасть до наступної дії, все що після continue - не виконається, пропустить ітерації букв 'o'


    	while n < 3:
            
            try:
                V_zero = int(input('Введіть будь-ласка початкову швидкість бігуна: '))
            except ValueError:
                print('Please select a proper start-speed!')
                n = n + 1
                if n == 3:
                    return 'U haven\'t selected a proper answer'
                else:
                    continue

            #S = V_zero * T + (a * T**2)/2 ### ЦЯ ЧАСТИНА ЦИКЛА БУДЕ МЕРТВОЮ ПІСЛЯ CONTINUE, ЯКЩО ВИКОНУЄТЬСЯ УМОВА ПО CONTINUE
            #return f'{S} metres'


    break - достроково перериває цикл 
    LOOP TERMINATION - NOTHING WILL HAPPEN

    	>>> for i in 'hello world':
		        if i == 'o':
		            break
		     print(i * 2, end='')

			>>> 'hheellll' - коли цикл досягне букви 'o' - ітерація закінчиться 


# МЕТОДИ РОБОТИ ЗІ СТРНІГОВИМИ ТИПАМИ ДАНИХ

split() - створення списку з даних типу STR (розбиття по пробілах)
	<'str'> - тільки до STR

	def list_creation_split():
    	return input('Type some words that will split between and form the list: ').split() - розбиття по пробілу

	def list_creation_split():
    	return input('Type some words that will split between each other and form the list: ').split(',') - розбиття по символу (символ може бути будь-яке значення - навіть слово)


join() - метод, котрий перетворює strінгу в список - використовуючи by_default - пробіл
join(char) - в якості аргументу може використовуватися будь-який розділювач, що розділить елементи списку за цими аргументами 

	def from_list_to_str(separator):
    	# wil create the list with separate elements (no spaces)
    	char = list(map(str, input('Put some characters that will create the list of str\'s: ')))
    	
    	# створить strінгу знову, проте в якості рохділювача - присвоїли умовний сепаратор. join() - метод сепаратора
    	return separator.join(char)

	print(from_list_to_str('✓')) 

	original list - ['і', 'в', 'і', 'в', 'і', 'в']
	>>> і✓в✓і✓в✓і✓в


strip() - видаляє, тільки перші і останні елементи СТРІНГИ
strip(arg) -  це видалення пробілів, проте можна також видаляти і за конкретно вказаним символомб якщо такі є однакові на початку і в кінці
	<'str'> - тільки до STR

	def deletion(text):
    	return text.strip(', ') # повидаляє коми з початку і кінця стрінги
		print ( deletion (', Hello, world, Mars, '))

		>>> 'Hello, World, Mars'

lstrip() - видалення символів пробілів на початку рядка
lstrip(arg) #ми можемо вставити також параметр, по якому саме здійснюється видалення включно з ним, як і у випадку з split()
<'str'> - тільки до STR

	def deletion_left():
		txt = '#%998 Hello World'
    	return text.lstrip('#%998 ') #видалить символ вставлений з початку стрінги - зліва + із вставленим пробілом

    	>>> 'Hello World'

rstrip() - видалення символів пробілів в кінці рядка
rstrip(arg) - #ми можемо вставити також параметр, по якому саме здійснюється видалення включно з ним, як і у випадку з split()
<'str'> - тільки до STR

	def deletion_left(txt):
		txt = 'Hello World /////+'
    	return txt.rstrip('/////+') # видалить символ вставлений з початку стрінги - справа

		>>> 'Hello World'


replace() - замінить певний символ або фразу на інший вказаний
replace('arg1', 'arg2') - 'arg1' - те що заміняємо, 'arg2' - те на що заміняємо
<'str'> - тільки до STR

	def replace_symbols(txt): 
    	return txt.replace('bananas', 'apples') # тут 'apples' заміняться на 'bananas'

	txt = 'I love bananas'
	print (replace_symbols(txt))

		>>> 'I love apples'


ascii - генерує список з цифр, букв, символів (потрбіно щоб був імортований модуль string)

	def ascii_generator():
		return string.ascii_letters # string тут як модуль (імпортована бібліотека string)

		>>> [a-Z] (видасть суму всіх маленьких та великих букв від мальної а до великої Z)

	def ascii_lower():
		return string.ascii_lowercase

		>>> [a-z]

	def ascii_upper():
		return string.ascii_uppercase

		>>> [A-Z]


capitalize() - метод, котрий перетворює першу букву strінги в велику
<'str'> - тільки до STR

	def capitalize_expression(txt):
    	return txt.capitalize()

    	# barcelona will win the match  - original str
    	>>> 'Barcelona will win the match'


title() - метод, котрий перетворює всі букви strінги в великі. Тобто кожне слово - з великої літери
<'str'> - тільки до STR
	def title_expression():
    	txt = input('Put some names here that U would like to make as title, start from the lowercase: ')
    	return txt.title()
<'str'> - тільки до STR

	# original str - Barcelona, Real Madrid, Atletico Madrid, Espaniol
	>>> Barcelona, Real Madrid, Atletico Madrid, Espaniol


lower() - метод, котрий повертає всі букви у нижній регістр
		def from_upper_to_lower():
    		txt = input('Select your text: ')
    		return txt.lower()

print(from_upper_to_lower())
	# BARCELONA REAL MADRID ATLETICO MADRID ESPANIOL
	>>>  barcelona, real madrid, atletico madrid, espaniol 


upper() - метод, котрий повертає всі букви у верхній регістр

		---//---


islower() - метод, котрий повертає boolean значення True, якщо ВСІ букви у strінзі - великі
	[i.islower() for i in psw] - вираз, який перетворить кожний іtem (cимвол) - в BOOLEAN значення, False - якщо є символ верхнього регістру, True - якщо нижнього
	добре застосовувати разом з any(), таким чином просканується наявність елементів верхнього/нижнього регістрів

BOOLEAN
	def lowercase_all_check(txt): 
    	return txt.islower()

    	>>> True/False

isupper() - метод, котрий повертає boolean значення True, якщо ВСІ букви у strінзі - великі
BOOLEAN
    def uppercase_all_check():
    	txt = input('Put some expression here that U would like to check for UPPERCASES: ')
    	return txt.isupper()

    	>>> True/False

isdigit() - метод, котрий повертає boolean значення True, якщо ВСІ у strінзі всі цифри




# Методи створення списків:

int:
	
	a = 100
	a = [a]
	print(a)
	#>>> 100


	a = 100
	lst = []
	lst.append(a) #- ФОРМУЄ ОБ'ЄКТ В ПАМЯТІ
	print(lst)
	#>>> 100


	list(a) 
	#>>> TypeError: 'int' object is not iterable - ТІЛЬКИ ДЛЯ ІТЕРАБЕЛЬНИХ ОБ'ЄКТІВ








import random

str_to_list = list(map(str, input('Setup fruits that will fulfill your fruit list: ').split())) # str в <list>
str_to_tuple = tuple(map(str, input('Setup fruits that will fulfill your fruit list: ').split())) # str в <tuple>
str_to_set = set(map(str, input('Setup fruits that will fulfill your fruit list: ').split())) # str в <set>



#1 методом append() - Pomeranska T
lst = []
x = input ('Please type some data here')
lst.append(x)
print (lst)


''' НАЙПРОСТІШИЙ СПОСІБ '''

# метод split() - створення списку з даних типу STR (розбиття по пробілах)
def list_creation_split():
    return input('Type some words that will split between and form the list: ').split()

# extend() extension of an empty list
lst = []
x = input ('Please type some data here').split()
lst.extend(x)
print (lst)

#2 Функція list()
x = input ('Please type some data here')
y = int('Please type some data here')

lst = list(x) # will create the list of 'str' - as isput is str by default
lst_int = list(y) # will create the list of 'int'

# 2 добавляння одного списку до іншого
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = []
for i in my_list:
    new_list.append(int(i))

print(new_list)

#3 використовуючи цикл 'for' для створення списку
	def lst_app_iter():
		lst = []
		for (i) in range(1, x+1): # так як 'range' використовує int-ові значення потрібно привести все до int значень
			lst.append(int(i))

			if len(lst) == x:
				return (lst)
	
	x = int(input('Type the end of the list: '))	
	print(lst_app_iter())

# Using cycle for # create an iterator that will fulfill the list
	def append_func(x):
    	lst = []
    	for i in range(1, x+1):
        	lst += [i] # lst + [i] - ітератор

        	if len(lst) == x-1:
            	return (lst)

	x = int(input('Type the end of the list: '))
	print(append_func(x))


# using for loop - НАПОВНЕННЯ СПИСКУ ЗА ДОПОМОГОЮ ЦИКЛУ
b=[]
num = int(input ('Type the end of your list: '))
i = 1
for i in range(0, num):
	b=b+[i]
if len(b) == num:
	print (b)


# using cycle while 
c = []
i = 0
while i < 20: # кількість елементів у списку !!!!!!!!!!!!!!!
	c.append(random.randint(0,100))
	i += 1

print (c)

# +1 варіант з циклом while
	def lst_app_while(num):
		lst = []
		i = 1
		while i <= num:
			lst += [i]
			i += 1
		
			if i == num+1:
				return lst
	

num = int(input('Type the end of your list: '))
print (lst_app_while(num))

######################################


# Through range sequence:

	def lst_through_range(n):
		return (list(range(n)))

	n = input()


##################3 Створення списків за дпопомгою lambda ################################

	# 1 вхідний параметр int змінна
		
		#1) потрібно зробити елемент iterable:
		#2) mapимо і коневруємо кожен елемент в int 
		#3) обгортаємо наплени sequence в список

	def check_odd_even(number):
    	x = lst_map = list(map(int, str(number).split()))

    num  = 123
    ### >>>  [1, 2, 3] - list of integers
    ### >>> print(type(x[0])) ---> class<int>

    # якщ вхідний параметр str послідовність чисел то можна використати num.split() - свторить список str з чисел ['1', '2', '3'] 



#3 List Comprehension - LC
    
    # Основний вираз: 

    str_list = [str(i) for (i) in letters] # сформує список зі слів - stringових значень
    int_list = [int(i) for (i) in digits] # сформує список з цифр - intових значень

    # різні типи LC - як функція
	def lc():
		x = int(input('Type some digits: '))
		# return [int(i) for (i) in x]
		# return [str(i) for (i) in x]
		# return [(i) for (i) in x]
		# return [str(i) for (i) in str(x)]
		# return [int(i) for (i) in range (1, x+1)]
		return [int(i) for i in str(random.randint(1, x))]

	print(lc())

	def lc_2()
    	for (i) in range(1): # 1 generating 1 time
        	num_rand = random.randint(1000000000, 10000000000) #generating a regular 10digit number from 1000000000 to 100000000000 - додали 1 нуль
													   # для прикладу тут може бути число 1999999999, яке без 1ниці близьке до кінця рендомоного числа
    	int_lst = [int(i) for i in str(num_rand)] # using 'LC' to create a list of integers 
											  # утворить список з десяти чисел
	print (int_lst)

# LC як СИНТАКСИЧНИЙ ВИРАЗ ПЕРЕТВОРЕННЯ ПОСЛІДОВНОСТЕЙ АБО ОБ'ЄКТІВ ІТЕРАТОРІВ
# list comprehension як засіб перетворення списків, або фільтрації списків по заданих умовах
	

	На відміну від звичайного ІТЕРАТОРА не просто проітерує об'єкти а і одразу сформує список з них:

		lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		#    #    #    #    #     #     #     #
		for i in lst:
	        i = i*2
	        print(i)

    	return lst
    	#>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    	lst = [i**2 for i in lst]
    	#>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]





	def odds_check_function():
    	doubled_odds = [n*2 for n in range (10) if n%2 == 1]
    	return doubled_odds
    	# виведуться числа 1, 3, 5 , 7, 9 і котрі помножаться на 2 
    	# числа виведуться з діапазону 10 (1-9)
	print(odds_check_function())

	def reverse_function():
		a = ['apple', 'banana', 'cherry', 'pineapple' ]
    	b = [i[::-1] for i in a ] # оберне кожну букву в елементі списку
    	c = [i for i in b[::-1] ] # оберне кожен елемент в списку (слово)
    	return (b, c)

    	>>> ['pineapple', 'cherry', 'banana', 'apple']
    	>>> ['elppa', 'ananab', 'yrrehc', 'elppaenip']

    def from_nested_to regular():
		list = [['T', 'h', 'I', 's'], ['I', 's'], ['A'], ['T', 'e', 'S', 't']]
		not_nested = [''.join(i) for i in common_lst ]

		>>> ['ThIs', 'Is', 'A', 'TeSt']


	def from_nested_to_regular2(lst):
		
		regular = []

		for x in lst:
			for y in x:
        		regular += [y]

		x = [['span1', 'span2', 'span3'], ['sPaN', 'span6', 'span12']]

		##>>> ['span1', 'span2', 'span3', 'sPaN', 'span6', 'span12']


		видалення дублів зі списку - ЦИКЛ ПЕРЕБОРУ
		rough_list = [1, 2, 3, 2, 3, 4, 5, 6, 1, 6]

		s = set()
		for i in [1, 2, 3, 2, 3, 4, 5, 6, 1, 6]:
	    s.add(i)

		activities=list(s)
		print(activities)
		[1, 2, 3, 4, 5, 6]
 
	Генерація одного числа n - кількість разів
	
		num_of_times = int(input('Type the quntity of times: '))
		lst = [0 for i in range (num_of_times+1)]
		print(lst)	
		>>> [0, 0, 0, ...]



### Lambda Statements - https://howto.lintel.in/writing-shorthand-statements-in-python/

>>> foo = lambda a: a+3
>>> foo(3)
6
>>> foo(8)



















#3.1 List Generator
	
	# зразок генератора як функції
	# генератор це функція яка запамятовує останній виклик, на якому вона завершила своє відпрацювання
	# і при другому зверненні він стартує з цього стану
	def count_down(num):
		print('Start')
		while num > 0: # поки номер > 0
			yield num  # проробляй # дає можливість нам заморозити цей стан виклику
			num -=1

	next (count_down(25))

	# Генератор поверне "заморожене" значення в пам'яті "<generator object generator.<locals>.<genexpr> at 0x7f5f6c9eb9e0>" 
''' 
    Генератор виконається раз як тільки виконається проставлена умова
    і запам'ятається на тому ж значенні де вона і виконалась перший раз
    Наступного разу генератор запуститься вже з місця де він закінчив попередній раз
'''
	# зразок генератора як синтаксичного виразу, аналог LC
	def generator(num):
    	gen = (x*x for x in range (1, num)) # using parenthes instead of rectangular brackets 
    	return gen

	num = int(input('Type some number: '))
	print(generator(num))

# 3.3.1 ФУНКЦІЯ map():

map() - повертає проітерований обєкт типу <map object at 0x7f739467ba60>
filter() - повертає проітерований обєкт типу <filter object at 0x7f13a1bebe50>
			
			!!! їх потрібно повертати за допомогою функції list(), set(), tuple() або ін.

	# Видалення дублів
	def removing_duplucates(matched_items):
		matched_items = ['Raspberry Pi', 'Turing Pi', 'Turing Pi']
		filtered_lst  = matched_items[:]
    	return tuple(filter(lambda x: matched_items.remove(x) is None and matched_items.count(x) == 0, filtered_lst))
		
		>>> ['Raspberry Pi', 'Turing Pi']
		# https://stackoverflow.com/questions/41522601/python-removing-duplicates-in-list-only-by-using-filter-and-lambda

'''
	ФУНКЦІЯ MAP():
    ЗАСТОСОВУЄ ВВЕДЕНУ В ЇЇ ТІЛО ФУНКЦІЮ АБО МЕТОД
    ДО КОЖНОГО ОКРЕМОГО ЕЛЕМЕНТА

        1) map(abs, sequence) варіант #1 з функцією - IN-BUILT function
'''
	
	IN-BUILT function in map(): # функцію потрібно буде вводити без дужок!!

	# перетворить всі елементи в абсолютні числа
	a = [-1, -2, 3, 4, -5]
	print(map(abs, a))

	>>> [1, 2, 3, 4, 5]


	OWN-function - власноруч створена функція
	# A
	# СТВОРЮЄМО ФУНКЦІЮ МНОЖЕННЯ
	def f_multiply(x):
    	return x**2

    # ПЕРЕДАЄМО ЦЮ ФУНКЦІЮ ЯК АРГУМЕНТ В ФУНКЦІЮ map()
    a = [1, 2, 3, 4, 5]
	b = list(map(f_multiply, a))
	print(b)
	# помножить всі цифри в списку на 2
	>>> [1, 4, 9, 16, 25]


	# B
	# СТВОРЮЄМО ФУНКЦІЮ ОБРАХУНКУ СИМВОЛІВ STR:
	def f_count_symbols(x):
    	return len(x)

    # ПЕРЕДАЄМО ЦЮ ФУНКЦІЮ ЯК АРГУМЕНТ В ФУНКЦІЮ map():
    a = list(map(str, input('Select str data here: ').split()))
    >>> ['snow', 'rain', 'sun', 'wind']
    c = print(list(map(f_count_symbols, a)))
    # обрахує кількість символів в кожному елемннті списку - тобто слові
    >>> [4, 4, 3, 4] 



    МЕТОД В ЯКОСТІ АРГУМЕНТА у функції map(str.lower, sequence):

    def convertation('Cherry', 'Banana', 'Apple'):
    	a = list(map(str.upper, input('Select str data here: ').split()))
		return (a)

		>>> ['CHERRY', 'BANANA', 'APPLE']

	АНОНІМНІ ФУНКЦІЇ "lambda"
	

# в цей спосіб виконаємо створення списку з послідовності цифр які cформуються у 'int'овий список
# цей спосіб добре підходить для створення списків з одиничними символами
# УВАГА! Цей спосіб не підйде для створення списків з символами більше 9!!
	
	def list_map_no_space_lambda():
	lst_map = list(map(lambda x: int(x), input('Enter a multiply value with no spaces: '))) # Proniuk A.
	return lst_map

		>>> [1, 2, 3, 4, 5]

	def list_map_nospace():
	lambda_lst = list(map(int, input('Please type some data here with no spaces: '))) # Proniuk A.
	return lambda_lst

		>>> [1, 2, 3, 4, 5]

    # введення цифр через 'space'- intовий список
    # УВАГА! Цей спосіб підйде для створення списків з довільними цифрами N-значними
    #https://foxford.ru/wiki/informatika/metody-split-i-join-dlya-spiska-strok-v-python
	def list_map_with_spaces(1 2 3 4 5):
		lst_map = list ( map (int, input ('Enter a multiply value through a space: ').split())) #T.Pomaranska
		return lst_map

		>>> [1, 2, 3, 4, 5]

	def list_map_with_spaces(1 2 3 4 5):
	num = input ('Type some digits through space: ')
	arith_lst = list ( map (int, num.split())) # тут потрібно використовувати введення через пробіл
	return arith_lst

	print(list_map_with_spaces())
		>>> [1, 2, 3, 4, 5]


	my_list = [1, 2, 3, 4, 5]
	lambda_lst = list(map(lambda x: x*x, x) ) - помножить кожен з елементів на 2
	>>> [1, 4, 9, 16, 25]


#### створення списку з допомогою lambda функції
[1, 1, 3, 5, 13, 21, 55]
result2 = filter(lambda x: x % 2 == 0, fib) # профільтрує список, видасть всі парні бо справдиться умова x%2 = 0 або True, всі False відсічуться
print (result2)


СИНТАКСИЧНИЙ ВИРАЗ ПЕРЕБОРУ ЗА ДОПОМОГОЮ lambda + map()

	# Перевагою цього лямбда оператора є тещо він використовується в комбінації з map() функцією яка містить дава аргументи:
	# 1) САМУ ФУНКЦІЮ
	# 2) АРГУМЕНТИ ФУНКЦІЇ, SEQUENCE - ПОСЛІДОВНІСТЬ


	a = [1,2,3,4]
	b = [17,12,11,10]
	c = [-1,-4,5,9]

	d = [] # d.append (map(lambda x,y:x+y, a,b))) - не буде працювати

	map(lambda x,y:x+y, a,b)
	map(lambda x,y,z:x+y+z, a,b,c)
	

# 3.3.2 ФУНКЦІЯ filter():

filter() Застосовується для того щоб відфільтрувати елементи ітерабельного об'єкта:
         Повертає <filter object at 0x7f13a1bebe50>, який є sequence - котрий можна обробити list()

	# create the list
	x = [i for i in range(11)]
	print(x)


	# filter the list for evens with lambda # same1
	y = list(filter(lambda value : value%2 == 0, x))
		>>> [0, 2, 4, 6, 8, 10]

 
	# filter the list for evens with LC # same1
	z = [even for even in x if even%2 == 0]
		>>> [0, 2, 4, 6, 8, 10]

	def lst_remove_item():
		lst = [i for i in range(5)]
		msg = filter(lambda x: x != 0, lst)
		return list(msg)

		>>> [1, 2, 3, 4]

    def fib_filter():
	    fib = [0,1,1,2,3,5,8,13,21,34,55]
	    result = filter(lambda x: x % 2, fib) 
	    return type(result)

	    >>> [1, 1, 3, 5, 13, 21, 55]


	def filtration_by_symbol():
		arr = input('Enter items of your array:  ').split()
		lst_filter = list(filter(lambda x: x.count('o')==0, arr[:]))
		return lst_filter

		# ['soso', 'oro', 'ii'] - original str
		>>> ['ii'] 

	# lambda для роботи з STR даними
	def color_list(colours):
		end_letter = 'e'

		with_e = list(filter(lambda x: x.endswith(end_letter), colours))
		without_e = list(filter(lambda x: not x.endswith(end_letter), colours))
		return f'The list with suffix e: {with_e}. The list without suffix e: {without_e}'

		# colours = ['red', 'orange', 'blue', 'brown', 'green', 'white']
		>>> The list with suffix e: ['orange', 'blue', 'white']. The list without suffix e: ['red', 'brown', 'green']

# 3.3.3 ФУНКЦІЯ reduce():
#lst_reduce = reduce(lambda x, y: x+y, result2) -дізнатися
#print(lst_reduce)






### РОБОТА З NESTED OBJECTS:
	
	LC - zяк засіб перебору елементів NESTED LIST
	    
	    def from_nested_to regular:
		list = [['T', 'h', 'I', 's'], ['I', 's'], ['A'], ['T', 'e', 'S', 't']]
		not_nested = [''.join(i) for i in common_lst ]

		>>> ['ThIs', 'Is', 'A', 'TeSt']


		# віднімаємо дані з тюпла, підносимо до квадрату, наповнюємо новий список цими значеннями
		# [(40, 30), (30, 20), (20, 10)]
		lst = []
		for a, b in zipped_list:
		    a = [(a - b)**2]
		    lst += a

		>>> [100, 100, 100]

		цей же вираз можна і записати через LC:

		[ (a - b)**2 for a, b in lst]


# ФОРМАТУВАННЯ

name = 'DataCamp'
type_of_company = 'Educational'

## enclose your variable within the {} to display it's value in the output 
print (f"{name}' is a {type_of_company} company ")
 
# f: Кожна f-string конструкція складається з 2ох частин, перша з самого власне f-ідентифікатора форматування перед лапками тексту, і наступна з тексту який ми хочемо передати ззовні {в дужки} саме для виводу. Фігурних дужок може бути багато.
# Змінні у фігурних дужках це звичною мірою текстовий формат даних.



x = ['James', 'Sam', 'John']
secret_names = map(lambda x: hash(secret_names), x)
print (list(secret_names))






################### порівняння LC i map:
#основна відмінність це list() - функція розбиває окремі слова на елементи списку. Слово - елемент списку

#args* kwargs** #########################################################################################
# 1.1
	def max_min_number(*numbers):
    	return max(numbers)


		print (max_min_number(1, 2, 3, 4, 5))

	''' *args - створена для того щоб ідентифікувати що у функції може бути декілька аргументів. 
		параметр *args у верхній частині функції означає що кількість переданих аргументів може бути N
		при ввведенні для прикладу 2ох або більше аргументів 
		для прикладу: https://prnt.sc/uko8ld
		https://habr.com/ru/company/ruvds/blog/482464/
	'''
# 1.2 Оператор «звёздочка»

	a = [1,2,3]
	b = [*a,4,5,6]
	print(b) # [1,2,3,4,5,6]

'''
   ** Два символи за допомогою яких створюється словник
   В ньомумістяться іменовані аргументи, 
   передані функциї при її виклику

   Тобто, якщо параметром функції є словник - dict,
   котрий має багато key-Value у свою чергу

'''

	def print_pet_names(owner, **pets):
   		print(f"Owner Name: {owner}")
   		for pet, name in pets.items():
      	print(f"{pet}: {name}")

		print(print_pet_names("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon"))
            
'''
	Owner Name: Jonathan
	dog: Brock
	fish: ['Larry', 'Curly', 'Moe']
	turtle: Shelldon

'''





BUILT-IN FUNCTIONS - ВБУДОВАНІ ФУНКЦІЇ:

ord(), chr(),
round(), divmod()



print() - функція вивести на екран

	def print_simple(var):
		return (input"Type the content U want to show on the screen: ")



len() - кількість елементів у списку intових та  strінгових
	
	def len_words(): # recursion function 
    	lst = list(map(lambda x:x, input('Type some text here: ').split()))
    	return len(lst)
    
		print(len_words())

		>>> ['dsdjs dsdhsjhd'] - len for this words will be '2'

sum() - функція, яка повертає арифметичну суму всіх елементів
    <list>, <tuple>, <dict>, <range(x)>

object.diff() - метод протилежний sum()

    'iterable' - послідовність intових чисел 'sequence', яка повиннна бути просумована sum.
    sum(iterable) - by_default - виведе арифметичну суму всіх intових елементів у списку
    sum(iterable, start) - виведе арифметичну суму всіх intових елементів у списку проте стартом додавання буде змінна 'start'


	def arithmetic_sum():
    	lst = list(map(int, input('Put the digits that will form the list: ')))
    	return sum(lst)

    def sequence_sum():
    	return sum(range(10))

	# арифметична сума зі стартом 'start'

	def arithmetic_sum_start():
    	items = input('Please type some digits with no spaces.')
    	lst = (int(i) for (i) in items )
    	return sum(lst, 100) # в якості старту тут - 100. Тобто всі числа будуть додватися між собою нез нуля а зі ста

max() - функція яка знаходить максимальне число зі списку. Якщо STR - повертає максимальне значення в алфавітному порядку

	def max_(items):
		lst = []
		for i in items:
			lst += [i]

		#print(lst)
		return max(lst)

		# original STR - ABCDEF
		>>> 'F', так як F з цих букв буде мати найбільшу вагу по алфавіту

	    maximum повинна брати не менше як 2 аргументи, якщо це не sequence або list
    	max (arg1, arg2), аргумент 1, аргумент 2: більше/менше значення

		def findMaxSum(list_first):
			maximum = 0
    		for x in list_first:
        	maximum = max(sum(x), maximum) 
                                       
    	return maximum

		list_first = [[11, 2, 3], [44, 5, 6], [10, 1, 2], [17, 8, 6]]
		# >>> maximum = max(55, 0) В ДАНОМУ ВИПАДКУ


pow() - функція pow() підносить число до степеня. Перший параметр - власне число, другий - степінь:
	
	def function(a, b):
		return pow(a, 2), pow(b, 3)
	print (function(5, 10))
	>>> (25, 1000)



sorted(par) - ФУНКЦІЯ яка сортує елементи списка в алфавітному порядку by_default або за вказнаим параметром 
			- обовязково повинна приймати деякий параметр
		<list>, <tuple>, <set>

		def sort_list():
			coutries = set(map(str, input('Select the countries attending the tournament, using space: ').split()))
			return sorted(countries)

			!!! sort() & sorted() - COMPARISON

			parameter.sort() - METHOD
			sort(parameter) - FUNCTION


type() - функція, яка повертає тип об'єкта. Об'єктом може бути будь-який тип даних.
	   - <list>, <tuple>, <dict>, <set>, <str>, <hex>, <map>
	
	def type_object():
		# для прикладу повернемо тип даних <dict> до типу даних, які прийшли з сервера за допомогою in-built функції dict()
		data_from_dict = {
  			"brand": "Ford",
  			"model": "Mustang",
  			"year": 1964
		}
		return type(data_from_dict)
	
	>>> '<class 'dict'>'


isinstance(object, type) - фунція, як перевіряє чи належить даний об'єкт іншому об'єкту, є даними іншого класу або екземпляру класу
		
		isinstance коротко: is this an  instance --- тобто чи це об'єкт
		
		var1: - з її допомогою можна також перевірити чи належить об'єкт до певного типу (певного типу даних) як із варіантом type()

		x = isinstance(5, int)
		#>>> True

		var2:
		class myObj:
  			name = "John"

			y = myObj()

			x = isinstance(y, myObj) # myObj - є екземпляром класу myObj
			# >>> True

		var3:
		Крім того, isinstance() за порівнянням з type() дозволяє перевірити дані на приналежності, хоча б одному типу із кортежу, переданого у якості другого аргументу

		a = (5, 10)

		isinstance(a,(float, int, str, tuple))
		>>>True

		isinstance(a,(float, int, str))
		>>>False



dir() -  функція dir() - видає набір всіх методі і функцій, які можуть бути застосовані до об'єкта #

		class Person:
  			name = "John"
  			age = 36
  			country = "Norway"

  			>>> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__'....

dir(object) - поверневсі методи котрі притаманні даному класу/об'єкту


abs() - функція переворення всіх знаків ітерабельного об'єкта на плюсові (переведе всі інтові значення позитивні/негативні в абсолютні числа ) #
 		
 		def absolute_digits():
 			a = [-1, -2, 3, 4, -5]
 			return abs(a)
 		>>> [1, 2, 3, 4, 5]


enumerate() - функція, яка в якості аргументу бере ітерабельний об'єкт, і повертає пронумерований об'єкт типу <enumerate object at 0x7f5297ee7840>, який
			  можна витягнути у:

			  dict():
			  # {0: 'This', 1: 'is', 2: 'a', 3: 'string'}

			  список tuples:
			  list():
			  # [(0, 'This'), (1, 'is'), (2, 'a'), (3, 'string')]

			enumerating days of week straing from 1
			 def day_of_week():
    			x = dict(enumerate((calendar.day_name), 1))
    			return x


reverse() - працює без присвоєння, разовий метод
!!! ' '.join. тільки з присвоєнням

###### конвертація списку в стрінгу

# використовуючи map та lambda числення
1) str_join_map = ” “.join(map(str, lst_mixed)) 

2) ' '.join(list) # має бути повернута оператором return


###ВСІ ОПЕРАТОРИ СПИСКІВ: https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

split() - розбиває введені символи по словах з інпут і формує список ЗІ СТРІНГИ (СФОРМУЄ СПИСОК)
		- формує список зі стрінги і розбиває по словах
		<str> !!! формує список з STR

		- виконати розбиття можна і по символу наприклад по комі list = long_date.split(',')

		def shorten_to_date(long_date):
    		sequence = long_date.split(',')
    		return sequence[0]
			print(shorten_to_date("Tuesday January 29, 10pm"))

    		>>> Tuesday January 29

    	розбиття by_default

    	def list_creation_split():
    		return input('Type some words that will split between and form the list: ').split() - розбиття по пробліу

    	<str> дані можна також розбивати по сепаратору:
    		  проте прописавши N - відповідну кількість змінних на які розіб'ється str

    		  name = 'John Smith'
			  first_name, last_name = name.split()
			  print(last_name) >>> 'Smith'
			  print(last_name, first_name, sep=', ') >>> 'John Smith'


append() - метод, який додає intове або strінгове значення на початок списку
		 - за допомогою цього методу можна наповнювати заздалегідь-створений порожній список

		def put_item_to_lst():
			lst = list(map(str, input('Type some text here with spaces').split()))
			lst.append(input'Add some item to the list')
			return lst

insert(pos, element) - insert() вставляє фіксоване значення на фіксоване мсіце у списку
										   - insert() примйає 2 аргументи (позиція в списку, елемент в списку)

		def fix_item_to_lst(позиція в списку, елемент в списку):
			lst = list(map(str, input('Type the list of employers with spaces: ').split()))
			lst.insert(-1, input('Add some item to the list - '))
			return lst

clear() - The clear() method видаляє всі елементи зі списку
		
		def wipe_lst():
			lst = [str(i) for (i) in input('Type some elements of the list using space: ').split()] # using lc як синтаксичний вираз
			lst.clear()
			return lst


copy() - клонує список проте наслідує всі зміни від нього автоматично. При зміні оригіналу - змінюється і shallow copy()
		!!! це діє тільки для nested об''єктів списку, тобто тільки ті які розміщені в списку. якщо в список додано нові обєкти через extend(), add(), append() - shallow список тоді не зміниться

		def copy_list_like_obj():
    		obj = list(map(str, input('Select the list like object U want to create: ').split()))             # object should be <list>, <set>, <tuple>, <dict>
    		obj2 = obj.copy() # створить shallow copy, яка при зміні obj (оригіналу) буде змінюватись також 

        	obj[0] = 5 # змінили елемент списку obj з індексом 0 на 5 - SHALLOW COPY зміниться також 
    		# obj2 - помінявся також - бо він тяне інформацію з кореневого 'obj'

        	### !!!!! проте тільки при зміні nested() об'єктів - тих які вже вставлені в список!!!!
        	obj.append('Marocco') # змінить тільки оригінал obj, shallow copy - не зміниться 
    		obj.extend('Marocco') # змінить тільки оригінал obj, shallow copy - не зміниться 



deepcopy() - копіює незалежну від оригіналу копію і при зміні оригіналу - deepcopy() вже не зміниться
		   - deep.copy - повертає значення первісного елемента. повинен бути імпортований модуль copy
 
 		import copy
 		
		def copy_list_like_obj():
    		obj = list(map(str, input('Select the list like object U want to create: ').split()))            # object should be <list>, <set>, <tuple>, <dict>
    		obj_copy = obj.copy()
    		obj_deepcopy = copy.deepcopy(obj) # copy - імпортований модуль
   


count() - метод count() повертає кількість елементів із заданим значенням                                    # object should be <list>, <tuple>
    	  повертає кількість входжень даного елесента в strінгу intовий список

		 def count_symbol_str():
    		lst_str=list(map(str, input('Please type some data here with no spaces: ').split()))
    		#2#lst = tuple(map(str, input('Please type some data here with no spaces: ')))

			word = input('Type some stuff here: ')
			how_many = word.count('y')

			>>> 
			
    	def count_symbol_int():
    		lst=list(map(int, input('Please type some data here with no spaces: ')))
    		# аргументом в даному випадку є цифра 5, рахуємо кількість входжень цієї цифри в деякий список
    		count_lst=lst.count(5)
    		return count_lst

    		!!! count(буква) також можна застосовувати до звичайної стрінги

extend() - метод який дозволяє продовжити список значеннями іншого списку або фіксованим значенням Value. Те ж саме що додавати список№1 до списку  №2.
		<list>
		
		def extended_list():
    		lst = list(map(lambda x: int(x), input('Type the number that will create your list: ')))
    		lst2 = [str(i) for (i) in str(input('Type the number which will be split to digits and added to the first list: '))]
    		lst.extend(lst2)
    		return lst

    		# return lst.extend(lst2) # !!! функція не спрацює (тільки через присвоєння), спочатку потрібно її виконати# а потім повернути об'єкт з памяті через return

    		a = [1, 2, 3]
    		b = [3, 4, 5]
    		a.extend(b)

    		###>>> [1, 2, 3, 4, 5, 6]
    		

    

reverse() - метод повертає значення елементів списку у зворотньому порядку
		 <list> !!!only

		def reverse_items():
			employee_lst = list(map(str, input('Type professions of attendancies: ').split()))
			employee_lst.reverse()
			return employee_lst

			# return lst.reverse() # !!! функція не спрацює (тільки через присвоєння), спочатку потрібно зберегти продовжений список в памяті # а потім повернути об'єкт з памяті через return


sort() - метод який сортує елементи списка в алфавітному порядку by_default
		<list>, <tuple>, <set>
		def sort_list():
			countries = list(map(str, input('Select the countries attending the tournament, using space: ').split()))
			countries.sort()
			return countries

			тут можна задати додаткову функцію яка поверне змінений елемент по якому відсортуємо список
			
			def set_parameter(items):
				return len(items) # параметром тут буде кількість елементів - тобо відсортує по кількості елементів 
			
			згідно цієї фунції-параметра можна задати умову по якій відбудеться сортування (key=set_parameter) ДЕ key - константа, set_parametr (умова зміни параметра)
			
			def sort_list_by_parameter():
    			sort_lst = list(map(str, input('Select the countries attending the tournament, using space: ').split()))
    			sort_lst.sort(key=set_parameter)
    			return sort_lst

sorted(par) - ФУНКЦІЯ яка сортує елементи списка в алфавітному порядку by_default або за вказнаим параметром 
			- обовязково повинна приймати деякий параметр
		<list>, <tuple>, <set>

		def sort_list():
			coutries = set(map(str, input('Select the countries attending the tournament, using space: ').split()))
			return sorted(countries)

			!!! sort() & sorted() - COMPARISON

			parameter.sort() - METHOD
			sort(parameter) - FUNCTION


remove(x) - метод видаляє елемент зі списку із вказаним значенням. ValueError, якщо такого елемента не існує
			<list>, <set> 

    	def remove_item_str():
			# for example there we're typing some fruits like: Cherry Pineapple Plum Pear
			# it'll creat the list of str's ['Cherry', 'Pineapple', 'Plum', 'Pear']
			fruit_lst = list(map(str, input('Type your beloved fruits here: ').split()))
			# now we need to execute something to remove like 'Plum'
			fruit_lst.remove('Plum')
			return fruit_lst

			original = ['Cherry', 'Pineapple', 'Plum', 'Pear']
			>>> ['Cherry', 'Pineapple', 'Pear']

		def remove_item_int():
			fruit_lst = list(map(int, input('Type your beloved fruits here: ').split()))
			# ввести тільки intові значення
			fruit_lst.remove(1)##!!!!!!!!! intoві значення потрібно вводити без лапок
			return fruit_lst

			print(remove_item_int())


[:] - зріз списків аналогічний lst.remove

			def removal(a):
				a = [4, 5, 6]
				a = a[1:]
				return a

			#>>> [5, 6]

pop() - метод ПОВЕРТАЄ ОСТАННІЙ елемент зі СПИСКУ якщо індекс не вказаний # pop()[0:4] обріже стрінгу в останньому елементі списка 
pop(i) - видаляє i-ий элемент зі списку і повертає його, якщо індекс не вказаний - обріже дефолтно останній елемент
		<str>, <list>, <dict>
		
		def return_element(n):
			a = list(range(1, 15, 3))
			b = a.pop(n-1)
			return b

			>>> створили список з даних range() [1, 4, 7, 10, 13] >>> вибрали з нього елемент №1 та з індексом 2

		def shorten_smthn(long_smthn):
    		sequence = long_smthn.split()
    		sequence.pop()
    		#sequence.pop(0) # обріже перше значення
    		return ' '.join(sequence)

			long_smthn = 'Hello World and Mars' 
			print (shorten_smthn(long_smthn))		

del - !!!! УВАГА - НЕ МЕТОД !!! оператор (keyword) широкого призначення, який видаляє як цілі об'єкти так і їх окремі частини (класи, списки, змінні)'
		видалає привязку цього імені цбого списку як з локального так і глобального простору імен

		def del_object(object): 
    		object = list(map(lambda x: x, input('Type some elements here with no spaces: ')))
    		del object[0]  # видалить першу частину списку
    		#del object[0:2] # видалить частину списку яка зріжеться
    		return object


index() - метод повертає індекс першого знайденого елемента в списку 
		- список можна також задавати не цілий а зрізаний, щоб звузити таким чином пошук+ обмежити кількість аргументів, які видадуться

		def several_indexes_find():
			a = ['a', 'c', 'e', 'a', 'b']

		print (a.index('a')) #0
		print (a.index('a', 2)) #3
		print(a.index('a', 2, 4)) #3
		print(a.index('a', 2, 3)) - will throw a ValueError - елементу не буде в діапазоні


str.find('substring', start/end) - way to Find the Index of a Substring in Strings in Python:
		
		string = {'_state': '<django.db.models.base.ModelState object at 0x7f3f2f689bb0>', 'id': None, 'email': '', 'password': '', 'nickname': '', 'name': '', 'surname': ''}

		index = x.find('email', start) ## індекс email від початку стрінги - по факту індекс -1 який потрбіно буде зрізати
		# index is 87
		result = '{' + f'{x[index-1:]}'



diff() - метод з Pandas: ЗНАЙДЕ РІЗНИЦЮ МІЖ 2ома списками або ЕЛЕМЕНТАМИ В NESTED OBJECTS АБО EЛЕМЕНТАМИ В NESTED OBJECTS
		
			Для прикладу є 2 списки з точок координат:

			[60, 35, 10] - p1
			[80, 40, 0] - p2

			# створить матрицю або nested object:
			arr = np.array([p1, p2])
			[[60. 35. 10.]
 			 [80. 40.  0.]]
	        
	        calc = np.diff(arr, axis = 0)

			axis - параметр, який означає:

				axis = 0 - списки віднімаються по вертикалі

							[[40. 30. 20.]
	 							[30. 20. 10.]]

	 						>>> [[-10. -10. -10.]]

	 			axis = 1 - списки віднімаються по горизонаталі

							[[60. 35. 10.]
	 						 [80. 40. 0.]]

	 						>>> [[-25. -25.]
	 							 [-40. -40.]]

	# 12ий пункт: https://coderoad.ru/22320534/%D0%9A%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80-axis-%D0%B8%D0%B7-NumPy
 	# Сode#2: chrome-extension://mbniclmhobmnbdlbpiphghaielnnpgdp/screenshot.html?id=screenshot_0.43687697238270573

## dicts
get() - метод d dict. Повертає значення елемента Value через специфічний ключ key
		<dict>

		def get_item_from_dict():
			car = {
            	"brand": "Ford",
            	"model": "Mustang",
            	"year": 1964
        	}
			return car.get('model') # метод get() можна використовувати одразу з return
			>>> 'Mustang'

щоб добавити новий елемент в <dict> потрібно просто вписати його разом з key-Value
		<dict>
		def add_item_to_dict():
			car = {
				"brand": "Ford",
            	"model": "Mustang",
            	"year": 1964
            }
            car['color'] = 'red'

            >>> {"brand": "Ford", "model": "Mustang", "year": 1964, 'color': 'red'}


		dict_ = {
    		'car1': 'Ford',
    		'car2': 'Mercedes',
    		'car3': 'Audi'
		}

щоб замінити новий елемент в <dict> потрібно просто вписати його разом з key-Value
			dict_['car1'] = 'BMW' #якщо заассайнимо той самий ключ то значення Value поміняється.
			dict_['car4'] = 'BMW' #якщо заассайнимо інший ключ то добавиться нове значення Value. 

update() - метод який дозволяє змінити дані <dict>№1, даними <dict>№2. keys, values - зміняться

		def updated_set_by_list():

    		kvps = {'1': 1, '2': 2, '3': 4, '4': 4, '5': 5} 
			newData = {'1': 10, '3': 30}
			
			kvps.update(newData)
    		return kvps

    		>>> {'1': 10, '2': 2, '3': 30, '4': 4, '5': 5} тобто змінилися пари '1': 1 та '3': 4

dict(**data, key=value) - vетод для обновленння/добавляння інфи в dict(). id добавиться в кінець і відсортувати далі можна через метод sorted()
    		
			!!! тільки для str ключів інакше TypeError: keywords must be strings (ключі мають бути в str форматі)
			!!! id - стане також str типом даних, 'id'

	    	data = { "username": "newtheUser", "firstName": "newJohn", "lastName": "newJames", "email": "john@email.com", "password": "new12345" }
	        data = dict(**data, id=1)

	        ### >>>>
	        		# updated_data = { 'username': 'newtheUser', 'firstName': 'newJohn', 'lastName': 'newJames', 'email': 'john@email.com', 'password': 'new12345', 'id': 1}



keys() - method keys() -для dict - пвертає всі ключі наявні в dict()	

			def items_dict_():
				    
				car = {
				        "brand": "Ford",
				        "model": "Mustang",
				        "year": 1964,
				        "condition": 'decent',
				        'previous owner': 1
				    }

		    car.keys() # <class 'dict_items'>
		    
		    return list(car.keys())

		    >>> ['brand', 'model', 'year']


    4 ways of Check if Key Exists in the dict:

    dict_ = {'fruit1': 'Apple', 'fruit2': 'Banana', 'fruit3': 'Cherry', 'fruit4': 'Strawberry'}
 		
 		### method 1 (in dict)
    	1) key_exist = 'fruit1' in dict_
		   print(key_exist_)

		   ### >>> True

		### method 2 (in dict_.keys())
		2) key_exist = 'fruit1' in dict_.keys()
		   print(key_exist_)

		   ### >>> True

		### method 3 ## порівняти значення методу get() != None ----> True, dict.get(key, default=None) - basic syntax
		3) key_exist = dict_.get('fruit1') != None
		   print(key_exist)
			
		   ### >>> True

		### method 4 ## instance method: __instance__
		4) key_exist = dict_.__contains__('fruit1') 
			print(key_exist)
			
		метод __contains__ перевіряє чи 'fruit1' є об'єктом класу dict_ ## (типу), тому може бути застосований ло будь-якого об'єкта що може мітсити 
		# key, наприклад:

		dict_.keys().__contains__('fruit1')
		list(dict_.keys()).__contains__('fruit1')





values() - method values() -для dict - пвертає всі значення наявні в dict()	

			def items_dict_():
				    
				car = {
				        "brand": "Ford",
				        "model": "Mustang",
				        "year": 1964,
				        "condition": 'decent',
				        'previous owner': 1
				    }

		    car.values() # <class 'dict_items'>
		    
		    return list(car.values())

		    >>> ['Ford', 'Mustang', 1964]


items() - 	method items() -для dict - повертає пари повністю в форматі <class 'dict_items'> == який по суті, є списком тюплів dict_items([( ), (  )])
    		це тюпли в списку - по парах key-value
		
		def items_dict_():
		    car = {
		            "brand": "Ford",
		            "model": "Mustang",
		            "year": 1964,
		            "condition": 'decent',
		            'previous owner': 1
		        }

		    pair = car.items()
		    return list(pair) # <class 'dict_items'>

		print(items_dict_())

		>>> [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('condition', 'decent'), ('previous owner', 1)]

		# РОЗБИТТЯ dict() на пари - виведення в лісти


			def add_item_to_dict(car):
				
			    keys_lst = []
			    values_lst = []
			    
			    for key, value in car.items():
			        
			        # формування списку keys, values: +[i]
			        keys_lst += [key]

			        # формування списку keys, values: append()
			        keys_lst.append(key)

	    return keys_lst
			
			car = {
			    "brand": "Ford",
			    "model": "Mustang",
			    "year": 1964,
			    "condition": 'decent',
			    'previous owner': 1
			}

		print(add_item_to_dict(car))		

		>>> ['brand', 'model', 'year', 'condition', 'previous owner']
		>>> ['Ford', 'Mustang', 1964, 'decent', 1] - values_lst


eval('str_data_like_dict') - метод котрий перетворить str дані (типу dict()) в dict:
	
		some_dict = {'_state': <django.db.models.base.ModelState object at 0x7f1d54b09af0>, 'id': None, 'email': '', 'password': '', 'nickname': '', 'name': '', 'surname': ''}
		--> eval(some_dict)
		>>> {'_state': <django.db.models.base.ModelState object at 0x7f1d54b09af0>, 'id': None, 'email': '', 'password': '', 'nickname': '', 'name': '', 'surname': ''}


	

ІТЕРАТОР ДЛЯ dict():
		
		# var1
		person = {} - це dict, який будемо наповнювати
		person['key#'] = [list of added values]


		str_data = 'John Smith New York PennStateUniversity 5 4 5 5 4 3 5'
		str_data = ['John', 'Smith', 'New', 'York', 'PennStateUniversity', '5', '4', '5', '5', '4', '3', '5']

		виберемо заповненння з 5ого елемента ітерабельного об'єкта str_data
		for i in str_data[5:]:
			person['key#'].append(i)    - ассайнимо ключ котрий будемо добавляти до нашого dicta()
										 заасайнений ключ буде відображати ячейку котру будемо заповнювати у форматі "key: value"

		print(person)


		# var2
		Створення dicta з елементів списку 1 символ - ключ, 2ий символ - value

		pattern_list = ['eu_kyiv', '24834', 'eu_volynia', '20231', 'eu_galych', '23745', 'me_medina', '18038', 'af_cairo', '18946', 'me_tabriz', '13421', 'me_bagdad', '22723', 'af_zulu', '09720']

		settlement = [i for i in pattern_list[::2]]
		# ['eu_kyiv', 'eu_volynia', 'eu_galych', 'me_medina', 'af_cairo', 'me_tabriz', 'me_bagdad', 'af_zulu']

		population = [int(i) for i in pattern_list[1::2]]
		# [24834, 20231, 23745, 18038, 18946, 13421, 22723, 9720] візьме тільки кожен другий елмент - населення в числах

		# ЗІПУЄМО ОБИДВА СПИСКИ
		zip_iterator = dict(zip(population, settlement))


		# ПОШУК МАКСИМАЛЬНОГО КЛЮЧА І ЗНАЧЕННЯ ЩО ЙОМУ ВІДПОВІДАЄ
		max(zip_iterator.keys()) - максимальне значення ключів dict.        zip_iterator.keys() - list всіх ключів

		max_key = max(zip_iterator.keys()

		zip_iterator[key]                                                  - value яке йому відповідає

		print(zip_iterator[key], max(zip_iterator.keys())








## sets - IMMUTABBLE !! DICT БЕЗ ПОВТОРЕНЬ
	    <set> - immutable тип даних
        !!! в set дані не повторюються, 
            тому при застосуванні функції len()
            до set {} - розрахується тільки кількість елементів,
            які не мають дублів

        !!! - set - скорочує на унікальність елементів, застосувавши для списку з однаковиими елементами - відкине елементи тіщо повторюються    

update() - метод який дозволяє вставити дані (<list>, <tuple>, <dict>) в <set>. Елементи проте змішаються в довільному форматі
		   !!! не застосовується до інших immutable типів даних
		   !!! застосовується до mutable типів даних типу <dict>


		def set_update():
		    kvps = set({'1', '2', '3', '4', '5'})
		    newData = set({'6', '7'})
			kvps.update(newData)
			return (kvps)

			>>> {'5', '2', '3', '1', '6', '7', '4'}

		def updated_set_by_list():
    		more_fruits = list(map(str, input('Setup fruits that will fulfill your fruit list: ').split())) #str в список <list>
    		fruits = set(map(str, input('Setup fruits that will fulfill your fruit list: ').split())) #str в сет <set>
    		fruits.update(more_fruits)
    		return fruits

    		#Original 'str': Cherry Banana Strawberry
    		#Setup 'str': Pineapple Plum Pear Orange
    		
    		>>> {'Cherry', 'Banana', 'Pineapple', 'Orange', 'Pear', 'Strawberry', 'Plum'}

discard() - метод який дозволяє видалити визначений елемент із <set>, проте на відміну від remove() - не підніме помилку, якщо такого елемента в <set> не виявиться
		  - не застосовується до інших immutable типів даних
			<set>

		def discard_set():
    		fruits = set(map(str, input('Setup fruits that will fulfill your fruit list: ').split())) # str список # applicable to tuples, set
    		fruits.discard('Plum')
    		return fruits

		print(discard_set())

intersection() - method returns a set that contains the similarity between two or more sets.
			
			a = ['apple', 'banana', 'cherry']
			b = ['potatoe', 'cucumber', 'beat', 'apple']

			# will find common elements between 2 sets
			distinction = set(a).intersection(set(b))		

			>>> {'apple'}

# 4.1 Dict Comprehension:








ДОДАВАННЯ ТА МЕРДЖЕННЯ СПИСКІВ:
#https://www.geeksforgeeks.org/python-ways-to-concatenate-two-lists/

zip(list, list) - формує єдиний список із двох списків по типу застібки:
## для прикладу є 2 списки:
coord1 = [3, 10, 2] # список1 a1, a2, a3
coord2 = [-20, 5, 1] # список2 писок1 b1, b2, b3
united_list = list(zip(coord1, coord2)) # сформує список №3 із тюплів що містять значення обох списків, який буде поєднанням обох списків по прототипу 'tuple in list'

	##>>>[(3, -20), (10, 5), (2, 1)]

	#дія2
	# далі значення цих туплів можна просумувати 
	summarized_1 = [(a+b) for a, b in united_list] # using list comprehension for changing a sctructure of  the list
	#using lambda expression
	summarized_2 = list (map (lambda x: sum(x), united_list)) # 'x' - тут буде одиниця списку а саме "тупл" (3, -20)

	
	summarized_22 = list (map (lambda x: sum (x), zip (coord1, coord2) )) # записали список одним рядком








enumerate - дізнатися !!!function adds a counter as the key of the enumerate object.b
розбиває список на 2 частини по ітемах (1) - ключ, порядок 2) сам елемент



### ЗРІЗ СПИСКІВ List_Slice()

	""" 
	   зріз списків відбувається за схемою:
	       1) між індексами вказується те що саме залишається(не те що зрізається)
	            для прикладу між елементами списку [2:5] - ТЕ ЩО МІЖ ІНДЕКСАМИ ЗАЛИШАЄТЬСЯ - РЕШТУ ВІДСІКАЄТЬСЯ    

	       2) ВКЛЮЧНО/НЕ ВКЛЮЧНО     INCLUDED/NOT INCLUDED

	""" 

	# ІНДЕКСИ В СПИСКУ
	''' 1ий символ - нульовий індекс [0]'''
	lst = ["apple", "banana", "cherry"]
	print(lst[0])

	>>> ['apple']

	''' 2ий символ - 1ий індекс [1]'''
	lst = ["apple", "banana", "cherry"]
	print(lst[1])

	>>> ['banana']

	''' останній елемент списка '''
	lst = ["apple", "banana", "cherry"]
	print(lst[-1])

	>>> ['cherry']

	# ЗРІЗАННЯ СПИСКІВ
	''' !!!!!!!!!!!!!ПРАВИЛО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	    ВКЛЮЧНО/НЕ ВКЛЮЧНО       INCLUDED/NOT INCLUDED
	    зріз списка [2:5]: 
	        зрізання відбудеться того що поза діапазоном від [2:5] = [2:5-1]
	        2ий індекс включиться
	        5ий індекс не включиться
	'''
	lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(lst[2:5])

	>>> ['cherry', 'orange', 'kiwi']
	'''
	    як бачимо 0ий і 1ий індекс відсікнеться і до 2ого не включаючи його
	    все включно від 5ого індекса відсікнеться також
	    https://prnt.sc/v9lm98 - w3schools explanation
	'''

	#без початкового індекса

	''' 
	    Відсутність початкового значення Value, зрізу списку означатиме зріз до 0вого значення з лівої частини
	    Елемент з індексом 4 в даному випадку відсікнеться так як діє правило ВКЛЮЧНО/НЕ ВКЛЮЧНО = ТЕ ЩО ЗАЛИШЕТЬСЯ 
	'''
	lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(lst[:4]) # початок зрізу означатиме індекс "0"

	>>> ["apple", "banana", "cherry", "orange"]

	#без кінцевого індекса
	'''
	    не вказавши значення Value кінцевого індекса
	    його права частина вже не відсікатиметься.
	    Список попрямує до кінця.
	'''
	lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(lst[2:])  #кінець зрізу означатиме список прямує до кінця і його права частина не відсікатиметься
	                # права частина 

	#>>> [cherry", "orange", "kiwi", "melon", "mango"]

	#з мінусових індексів

	'''
	    + індекси йдуть від 0 і з початку до кінця
	    - індекси йдуть від -1 і до початку
	    Залишиться від -4 - ВКЛЮЧНО - 'orange'
	               від -1 - НЕ ВКЛЮЧНО - 'mango' - ОБРІЖЕТЬСЯ
	'''
	lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(lst[-4:-1])

	# >>> ['orange', 'kiwi', 'melon']    (REMAIN IN THE LIST- INCLUDED : NOT INCLUDED - NOT REMAIN IN THE LIST)


	#без початкового/кінцевого індексів
	'''
	    відсутність початкового значення Value, зрізу списку означатиме зріз до 0вого значення
	    відсутність кінцевого значення зрізу Правої частини списку означатиме, що список попрямує до кінця - не відсікатиметься
	'''
	lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(lst[:])

	#>>> ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


	#з нульовими індксами повністю
	'''
	sqs [0:0] від 0 не включно і до нуля включно - ТОБТО ЗРІЖЕТЬСЯ ВСЕ 
	'''

	lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(lst[0:0])

	#обертання списку з кінця і до початку (реверс списку)

	lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(lst[::-1])
	#>>> ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']

	# hash
	error = "You input negative number: . Try again."  #: - 25


	hash = error[:error.index('.')] + str(number) + error[error.index('.'):]
	# error.index('.') - кінець зрізу списку з індексом '.' - 25ий індекс (25-1)
	# винесеться все від 0 до 24, 25ий вже зріжеться

	error[error.index('.'):]
	# зріжемо все від крапки до кінця списку від 25(включно) до кціня


	# Заміна значень в списку
	'''
	    Оскільки список є mutable (а отже займає більше місця за замовчуванням)
	    Його окремі значення можна обробляти не тільки функціями, але і заміняти значення
	    індексуючи деякі елементи та присвоюючи їм окреме значення
	    
	'''

	lst = ["apple", "banana", "cherry"]
	lst[1] = 'beet' # змінили значення 2ого елемента в списку на beet - буряк
	print(lst)

	# хід списку

	'''
	    Часто із зрізом списку застосовують
	    ще хід зрізу, він є третім аргументом
	    3 - третій аргумент - крок зрізання
	    Схема зрізання буде:
	        (REMAIN IN THE LIST- INCLUDED 1:10 NOT INCLUDED - NOT REMAIN IN THE LIST)
	        крок 2 - означає через 1ин
	'''

	digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # список, масив даних
	# зріжемо список від 1


    BOOL значення з list():
		lst1 = []                         ПОРОЖНІЙ СПИСОК [] - False, [i] = True
        lst2 =[i for i in range(5)]

        if not lst1:
            print('empty list == False')
        else:
            print('listwith at least one item  == True')




    ### SEARCH

    1. contains
    2. iteration (on elist through another)
    3. name.find("IT") - find - функція яка знаходить індекс декотрого елемента в STRінзі

    	def find_index():
    		name = "SoftServe IT  Academy"
    		return name.find("IT")

			print(find_index())
			>>> 10

    4. RegEx - characters ^ - beginning, $ - end, uppercase, 




STRiнгові літерали:
'\n' - літерал переносу на інший рядок "\n" 'newline'
	 - 

	def string_wrap(str1ng_):
    	return str1ng_


	str1ng_ = 'Backslash before "n", as in \n, inserts a new line character'  #doctest: +NORMALIZE_WHITESPACE'
	print(string_wrap(str1ng_))


	>>> 'Backslash before "n", as in                                                                                                                                                                                                                                                      
		, inserts a new line character'                                                                                                                                                                                                                                                             
		# відбудеться перенос рядка в другу лінійку

'\r' - 'carriage return' ???

'\t' - 'tab' return ???









set - скорочує на унікальність елементів


# модуль requests в програмці. json request 

#"name.repalce('O', 'o') - тільки разаово міняє об'єкт в памяті створює 0."



## регістри в списках

S.title() - Першу букву кожного слова ПЕРЕВОДИТЬ В ВЕРХНІЙ РЕГІСТР, а всі інші в нижній
S.capitalize() - Перекладає ПЕРШИЙ СИМВОЛ РЯДКА В ВЕРХНІЙ РЕГІСТР, а всі інші в нижній

sort() - ВІДСОРТУЄ СПИСОК по алфавіту якщо буквенний список, якщо цифровий в порядку зростання. одиничний метод (не приймає аргументу) - вкиконується разово, при return - повертає None
sorted() - функція. ВІДСОРТУЄ СПИСОК по алфавіту якщо буквенний список, якщо цифровий в порядку зростання.

	def sorter(textbooks):
    #return sorted(textbooks) # сортує список, зберігається зразу, тому може бути одразу і повернений
    
	textbooks.sort() # метод, відпрацьовує тільки раз, тому в пам'яті не зберігається
    return textbooks
    #return re.sub(r'[,\s]',' ', textbooks)

*args - створена для того щоб ідентифікувати що у функції може бути декілька аргументів. 
	параметр *args у верхній частині функції означає що кількість переданих аргументів може бути N
	при ввведенні для прикладу 2ох або більше аргументів 
для прикладу:


### ПОРІВНЯННЯ ДВОХ СПИСКІВ НА НАЯВНІСТЬ ЕЛЕМЕНТІВ:
 #1) МЕОД ANY - ПОВЕРТАЄ BOOLEAN ЗНАЧЕННЯ ПРИ ЗАСТОСУВАННІ ДО ДАНИХ ФОРМАТУ 'STR' - ВКАЗУЄ НА НАЯВНІСТЬ СИМОЛУ 

 	#### 1
 	result =  any([i in str_1 for i in (character_lst)]) # any return bool data - True/False

	str1 - текстова змінна, стрінга яку ми перевіряємо на нявність сумісності, 
 	character_lst - список який містить повну кількість символів - ітерований об'єкт 

	return True if not result else False

	#### 2
	sequence1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	sequence2 = [2, 6, 10]

    return True if any([i in sequence1 for i in sequence2]) else False

    ## поверне BOOL значенння


 #2) МЕОД ALL - ПОВЕРТАЄ BOOLEAN ЗНАЧЕННЯ ПРИ ЗАСТОСУВАННІ ДО ДАНИХ ФОРМАТУ 'STR' - ВКАЗУЄ НА НАЯВНІСТЬ СИМВОЛУ 

 	!!! Математичні опреатори які не стоять біля числа не належать до int(), не входять також до i.isdigit()
 	!!! З числом входять до типу int()
 	print(type(-10)) #>>> True

 	# спосіб
 	[1, 2, 3] або ['1', '2', '3']
 	# перевірка чи всі три цифри int чи str 
 	condition = all(map(lambda x: int(x), [a, b, c]))
 	#якщо всі int або int representation of digits - поверне True

 	#спосіб2
 	condition = tuple(map(lambda x: int(x), (a, b, c)))
 	# створити список але тоді якщо буква - Exception ValueError

 	#спосіб3
 	# потрібно ообернути число в str число
 	non_iterable = 12345
 	iterable = str(non_iterable) ### >>> '12345'
 	condition = all([i.isdigit for i in iterable])

 	#виключення "-" в isdigit не входить !!!
 	number = '-38'
 	False = all[i.isdigit() for i in str(number)]

 	#спосіб4
 	# конвертуємо кожну str в int, перевизначаємо умову створити список з int чисел
 	# isinstance - приймає  змінні - об'єкт на який перевіряємо, клас до якого він належить
 	x = all([int(i) for i in num if isinstance(int(i), int) == True])


 	### пошук числа букви яка знаходиться в стрнзі - повертаємо Bool значення
 	root = '/user/1'
    self.path = root 
    сorrect_id = len([True for i in root.split('/') if i == '1']) == True

 	## check if all digits are integers
 	a = '3'
	b = 3
	c = 3
	sides = (a, b, c)
	##condition_error2 = isinstance(a, int) ## +++

	condition_error2 = len([i for i in sides if isinstance(i, int)==False]) ### [i for i in sides if isinstance(i, int)==False] >>> ['3'] - далі його просто потрібно порахувати



 #3)  FINDING COMMON ELEMENTS IN THE LIST: set.intersection(*map(set, [a, b, c]))
 	  # виведе список однакових елементів характерних для інших списків

 	>>> a = [1, 2, 3, 4]
	>>> b = [2, 3, 4, 5, 6]
	>>> c = [3, 4, 5, 6, 10, 12]

	>>> common_elements_in_all = list(set.intersection(*map(set, [a, b, c])))
	>>> connon_elements [3, 4]
	#https://stackoverflow.com/questions/57210753/find-common-values-in-multiple-lists


#4) видалення дублів зі списку - ЦИКЛ ПЕРЕБОРУ

		rough_list = [1, 2, 3, 2, 3, 4, 5, 6, 1, 6]

		s = set()
		for i in [1, 2, 3, 2, 3, 4, 5, 6, 1, 6]:
	    s.add(i)

		activities=list(s)
		print(activities)
		>>> [1, 2, 3, 4, 5, 6]


#5) FINDING COMMON ELEMENTS IN TWO LISTS BUT WITH EQUAL INDEXES:

		lst1 = ['humid', 'warm', 'indoor', '25']
		lst2 = ['warm', 'humid', 'indoor', '25'] 

		lst1 = list(map(lambda x, y: x==y, lst1, lst2))
     	>>> [False, False, True, True]

 

 #2) i.islower() та і.isupper() методи:
### ПОТРІБНО ПРИВЕСТИ ДАНІ ДО ФОРМАТУ 'LIST' - СФОРМУВАТИ 1ИН ЗАГАЛЬНИЙ СПИСОК ЗІ ВСІХ СИМВОЛІВ - ІТЕРОВАНИЙ ОБ'ЄКТ ЗА ДОПОМОГОЮ extend() 

i.islower() - find Lowercase letter in the 'list' (password) #BOOL
i.isdigit() - find digit in the 'list' (password) #BOOL # isdigit() method returns “True” if all characters in the string are str(digits), Otherwise, It returns “False”
			>>> a = '15
				a.isdigit()
				>>> True
			>>> b = 'a15'
				b.isdigit()
				>>> False
i.isupper() - find Uppercase letter in 'list' (the password) #BOOL
i.isalpha() - methods returns “True” if all characters in the string are alphabets, Otherwise, It returns “False” #BOOL
# compares symbol_lst with psw_lst (if symbols exists in in list


result = any ([i.islower() for i in character_lst]) result = any ([i.islower() for i in character_lst]) and any([i.isupper() for i in character_lst]) and any([i.isdigit() for i in character_lst ]) and any([i in character_lst for i in symbol_lst])



### REGULAR EXPRESSIONS (RegEx)

re.match(pattern, string): метод що шукає по заданому шаблону проте ТІЛЬКИ ПО ПЕРШОМУ СЛОВУ В РЯДКУ (ЯКЩО ПЕРШЕ СЛОВО СПІВПАДАЄ З ПОШУКОМ - МЕТОД СПРАЦЮЄ, ЯКЩО НІ ТО ПОТРІБНО ЗАДАВАТИ 'start' i 'end')
	<str> - тільки для STR

	result = re.match(r'AV', 'AV Analytics Vidhya AV')
	return result.group(0)

		>>> <Match object>
		>>> 'AV'
	!!! УВАГА !!! ШУКАЄ ТІЛЬКИ ПО ПЕРШОМУ СЛОВУ !!! ЯКЩО В ПЕРШЕ СЛОВО НЕ AV - поверне значення None
	'''
	метод group() - застосовуєтьс ядля того щоб вивести вміст рядка що шукаємо.
	Результатом цієї функції є - об'єкт з типом <re.Match object; span=(0, 8), match='Portugal'>, який можна трактувати як BOOL
	'''

re.search(pattern, string): метод що шукає по заданому шаблону проте ПО ВСЬОМУ РЯДКУ (Метод search() ШУКАЄ ПО ВСЬОМУ РЯДКУ, І ПОВЕРТАЄ ВСІ СПІВПАДІННЯ У ВИГЛЯДІ)
	<str> - тільки для STR

	result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
	return result.group(0) 
	
		>>> 'Analytics'

		!!! Поверне перше знайдене співпадіння у форматі <Match object>
		>>> Результатом цієї функції є - об'єкт з типом <re.Match object; span=(0, 8), match='Portugal'>, який можна трактувати як BOOL
		
		>>> <Match object>


    group() - метод застосовуєтьсдля того щоб вивести вміст рядка що шукаємо.
	          Результатом цієї функції є - об'єкт з типом <re.Match object; span=(0, 8), match='Portugal'>, який можна трактувати як BOOL


### ВСІ СПІВПАДІННЯ
re.findall(pattern, string): цей метод повертає СПИСОК <list> всіх знайдених співпадінь 
	<str> - тільки для STR

	result = re.findall(r'AV', 'AV Analytics Vidhya AV')
	return result

	>>> ['AV', 'AV'] - повертає список всіх співпадінь. Якщо співпало 3 рази - поверне 3 рази.

re.split(pattern, string): цей метод повертає СПИСОК <list> всіх знайдених співпадінь 
	!!! за допомогою re.split - розбиття на ел списку може відбуватися за допомогою свого паттерна або 
	<str> - тільки для STR
	
	def re_split_items_by_symbol():
    	items = input('Select the countries attending the tournament, using space: ')
    	return re.split('\s', items) # в даному випадку розбиття по пробілах

    	# original STR - Portugal Spain Brazil Uruguay
    	>>> ['Portugal', 'Spain', 'Brazil', 'Uruguay'] - відбудеться розбиття списку по пробілах

### Заміна співпадінь
re.sub(pattern1, pattern2, string): цей метод замінить введений паттерн на інший теж введений в паттерн (Metacharacters чи Special Sequences)
	<str> - тільки для STR
	
	result = (re.sub(r'[,;%&\s]',' ', long_date)).split()   # '[,;%&\s]' - перша частина паттерну ',;%&' - всі ці символи будуть замінені на один єдиний символ 
															# ' ' - друга частина паттерну (застосується також до всіх пробілів між словами)
	return (shorten_to_date("Mo;nda%y Febru&ary 2, 8pm"))

	# >>> на виході отримаємо 'Mo nda y Febru ary 2'  - символи заміняться на спейси

re.compile() - умовний регулярний вираз, який по своїй суті є штучно створеним patternom
			 - використовується разом з re.findall(), re.search(), re.match() - для того щоб не вводити паттерн окремо

	def re_findall_items_through_compile():
    	pattern = re.compile('Portugal') # задали свій паттерн через compile()
    	items = input('Select the countries attending the tournament, using space: ')
    
    	return pattern.findall(items) # в даному випадку pattern вводити вже не потрібно, оскільки ми його задали попередньо
                                      # функція compile() виступає вже об'єктом, що несе за собою певну логіку: pattern = re.compile('Portugal')
	
         через re.compile() - прописали слово(pattern), по якому здійснюємо пошук в strінзі                          

         original str - Portugal Spain Brazil Uruguay Portugal 
         >>> ['Portugal', 'Portugal'] - оскільки Portugal є 2 рази в списку - список складатиметься з 2-ох слів




### INSTANCE METHODS

__contains__() -  instant method which we can use to check if it contains
				  another string or not, Python string_object.__contains__() is an instance
                  method and returns boolean value True or False depending on whether the string 
                  object contains the specified string object or not

	def expression_(dt):

	    iso_to_str = dt.isoformat() 
	    #return type(iso_to_str)
	    return True if iso_to_str.__contains__("12") and iso_to_str.__contains__("24") else False

		dt = date(2002, 12, 24) # dt - обов'язково повинен бути формату date
		__contains__ - метод обробки str даних, тому iso_to_str повинно бути <class 'str'>

		>>> True, так як цей паттерн присутній в даній strінзі
		

		'''
			1) порівняння ключів одного dict_ на нявність в іншому за допомогою __contains__
		'''


		d1 = {'fruit1': 'Apple', 'fruit2': 'Banana', 'fruit3': 'Cherry', 'fruit4': 'Strawberry'}
		d2 = {'fruit4': 'Apple', 'fruit5': 'Banana', 'fruit6': 'Cherry', 'fruit7': 'Strawberry'}

		keys_exist = list(filter(d1.__contains__, d2.keys()))
		print(keys_exist)

		### >>> ['fruit4']
		a = 'Cherry'
		b = 'Cherry'

		result = a.__contains__(b)
		print(result)
		>>>  True, так як цей паттерн присутній в даній strінзі


ФОРМАТУВАННЯ:

	
	ПО ТИПУ: '<class.str>.format(0, 1, 2)'

		def greet(name, surname, lastname):
			if name != 'Johny':
				return ("Hello, mr. {0} {1} {2}!".format(name, surname, lastname)) # the second method of doing this
			else:
				return ("Hello, {0} {1}!".format(name, lastname))

				#>>> замість item можемо присвоювати все що необхідно



	ПО ТИПУ ШАБЛОН:

		def greet(name):
			if name != 'Johny':
				return ("Hello, {}!".format(name)) # the second method of doing this
			else:
				return ("Hello, {name}!".format(name = 'item'))

				#>>> замість item можемо присвоювати все що необхідно


		def greet(parameter):
    		if name == "Johny":
        		return "Hello, my love!"
    		else:
        		return "Hello, {name}!".format(name=parameter)

        	#>>> 2ий name - це змінна, 



    f - рядок:

    	def greet(name):
			if name != 'Johny':
				return (f'Hello, {name}!') # the second method of doing this
			else:
				return ('Hello, my love!')


ADVANCED FORMATTING: Форматування з допомогою оператора %:

		# var1
		
		class Name:

			name = 'John'
			lastname = 'Smith'
			balance = 4500

			def __init__(self, name=name, lastname=lastname, balance=balance):
				self.name = name
				self.lastname = lastname
				self.balance = balance

			def balance_for_person(self, name, lastname, balance):
				return 'Місячна зарплата для %s %s, складає %d usd' % (name, lastname, balance)
		        #return f'Місячна зарплата для {name} {lastname}, складає {balance} usd' - еквівалент
		 
		# parametr by default when 
		# not being setup here
		name_selection = Name()
		print(name_selection.balance_for_person('Kim', 'Nolo', 6000))


		# var2
		print ('%(language)s has %(number)03d quote types.' % {"language": "Python", "number": 2})

		    %s - буква
    		%d - цифра
    			%5d - 5 цифр, якщо число довге (тіьки для натуральних чисел)
    		%r - літерал python
    		%(key)s - ключ dict
    		%(number)03d - ключ dict, де перша цифра - 0, а 3тя цифра - цифра d (значення яке прилетить)

			%.6f - якщо формат чила float - кільки знаків після коми + саме число до коми



			
			https://pythonworld.ru/osnovy/formatirovanie-strok-operator.html













### OOP

Базові концепції:

	Змінні ---> об'єкти
				Екземпляр класу - Об'єкт (слова синоніми) 

	Функції ---> методи

	Клас - прототип об'єкту, шаблон, template. Креслення по котрому ми конструюємо нашу програму.

	Іnstantiation - процес створення instances: екзмплярів класу: instance = ClassA()


	Класи можуть бути також дочірніми або батьківськими:

	class СlassA:
		attributes # батьківський

	class ClassB(СlassA): # дочірній
		attributes











НАСЛІДУВАННЯ: 

	'''
	    ЕКЗЕМПЛЯР КЛАСУ ЦЕ - ГЛОБАЛЬНИЙ ОБ'ЄКТ, ЩО МОЖНА ВИКЛИКАТИ ВСЕРЕДИНІ
	    ІНШОГО КЛАСУ І ВІН ТАКИМ ЧИНОМ ВШИЄТЬСЯ В ЦЕЙ КЛАС, І ТОДІ ВЖЕ ВІД instance, 
	    викликаємо будь-який атрибут з іншого класу 
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
	print(instance_a.calc())
	###>>> 200

	instance_b = B()
	print(instance_b.calc())
	###>>> 200


Звертання до атрибутів класу:

	class ClassA:

		a = 10; b = 50 # атрибут ClassA - дані що містить СlassA, котрими ми будемо розпоряджатися

		def function(self):
			return print('Do something')

	# параметр self буде містити інфу про instance, від instance викликаємо метод function.
	# без 'self' параметра не отримаємо доступ 

	instance1 = ClassA()
	instance1.function()

	# звертання до атрибутів класу - через екземпляр ClassA - instance1
	print(instance1.__class__.a)
	#>>> 10
		

	Використання атрибутів взятих із класу:


	Оримання атрибуту через екземпляр класу

	class A:

		x = 4;
		y = 5;

	    #загрузка параметрів з body
	    def __init__(self, x=x, y=y):
	        self.x = x
	        self.y = y

	    def create(self):
	        return x * y

	inst = A()
	print(inst.x)
	### >>> 4


	#1 отримання доступу до атрибуту класу - з body, класу
	class classA:

	    x = 4; y = 8

	    def __init__(self, x = x, y = y):
	        self.x = x
	        self.y = y
	    
	    def execution(self, x, y):
	        return x * y

	exempliar = classA()
	print(exempliar.execution(4, 8))
	#>>> 32

	#2 звертання до атрибутів класу
	class ClassA:

	    '''
	        Звертання до атрибутів КЛАСУ
	    '''
	    
	    # атрибути ClassA - дані що містить СlassA, до котрих хочемо отримати доступ
	    a = 10; b = 50 

	    def function(self):
	        return 'Do something'

		# звертання до атрибуту класу через екземпляр класу, без використання параметрів
		# при виклику методу

		instance1 = ClassA()
		print(instance1.__class__.a)
		#>>> 10


		#3 звертання до атрибутів класу
		class ClassA:

		    a = 10; b = 40

		    def __init__(self, a=a, b=b):
		        self.a = a
		        self.b = b

		    def multiplication(self, a=a, b=b):
		        return self.a * self.b


		instance = ClassA()
		print(getattr(instance, 'a'))
		# >>> 10

setattr(obj, name, value) - # function sets the value of the attribute of an object setattr(obj, name, value) - takes 3 parameters
	    :param obj: object whose attribute has to be set
	    :param name: attribute name
	    :param value: value given to the attribute

    	setattr(instance, 'd', 100)
    	print(instance.d)
    	# >>> 100

getattr(object, name[, default]) -  # Метод getattr() повертає значення названого атрибута an об'єкт.
		# Якщо не знайдено,він повертає значення за замовчуванням, надане до
     	# функція. Значення, яке повертається, коли названий атрибут не знайдено



		print(getattr(instance, 'c'))
		# >>> returns None when attribute not found

		print(getattr(instance, 'c', 70))
		# >>> returns 70 if not c attr value


delattr(object, name)

		delattr(instance, 'b')
		print(instance.__dict__)
		# >>> {'a': 10} b - has been deleted

		print(delattr(user, 'c'))
		# >>> AttributeError: first_name

		print(instance.multiplication())
		#>>> 400

		# 4 унаслідування атрибутів одного класу - іншими

		!!!! init робить змінні оного класу доступними для іншого при звертанні через self (4.3)

		class ClassA:

		    a = 10; b = 40

		    def __init__(self, a=a, b=b):
		        self.a = a
		        self.b = b


		class ClassB(ClassA):

		    def multiplication(self):
		        return self.a * self.b
		        ###>>> 400

		        # щоб мати можливість використати ці змінні, в якості інших параметрів
		class ClassB(ClassA):

		    	def multiplication(self):
		        	return self.a * self.b

		instance = ClassB()
		print(instance.multiplication())

			###>>> 2500

			# 4 унаслідування методів одного класу - іншими

			class A:

			    a = 10; b = 20;

			    def __init__(self, a=a, b=b):
			        self.a = a
			        self.b = b
			    
			    def calc(self, a=a, b=b):
			        # multipliacation
			        mult = a * b
			        return mult

			class B(A):
			    # class B launch class A
			    pass


			instance = A()
			print(instance.calc())
			###>>> 200

			instance = B()
			print(instance.calc())
			###>>> 200
			    
 
			instance = Triangle()                                   ## A() - батьківський клас, який унаслідував клас Polygon, 
																	#  тому можемо використовувати методи та атрибути Polygon від імені екземплярів
																	#  дочірнього класу Triangle
			instance.set_sides()
			instance.find_area()


			### !!!! init робить змінні оного класу доступними для іншого при звертанні через self
			4.3
			class Runner:
				def __init__(self, V_zero, T, a):
					self.V_zero = V_zero
					self.T = T
					self.a = a

				class Distance(Runner):
					def distance(self):
					S = self.V_zero * self.T + (self.a * self.T**2 * 0.5)
					return S




		# 4 унаслідування атрибутів одного МЕТОДУ - В ІНШИЙ
		   # АТРИБУТ ЯКИЙ ХОЧЕМО ВИКОРИСТАТИ ПОВИНЕН ПОТРАПИТИ В ГЛОБАЛЬНИЙ ПРОСТІР ЧЕРЕЗ return               

			class A():
		    
		    def method1(self, x=5, y=3):
		        self.x = x
		        self.y = y
		        multipl = x * y                                                                   

		        self.multipl = multipl # заассайнили метод multipl через об'єкт self 
		        return multipl                                                                    # self.multipl = multipl

		    def method2(self, number=15):	                                                      # multipl = self.multipl
		        multipl = self.multipl # надали значенню multipl значення multipl з 
		                               # попереднього методу через об'єкт self
		        calc = number - multipl
		        return calc

				instance = A()
				print(instance.method1())
				print(instance.method2())

		#>>> X = 15 - 15 = 0 


			'''
			    instance.set_coords - ЦЕ ОБ'ЄКТ ЯКИЙ ПОВЕРНЕ МЕТОД ІНШОГО КЛАСУ,
			    НЕЗАЛЕЖНО ВІД ТОГО ЯКИМ БУДЕ РЕЗУЛЬТАТ.

			    ЕКЗЕМПЛЯР КЛАСУ ЦЕ - ГЛОБАЛЬНИЙ ОБ'ЄКТ, ЩО МОЖНА ВИКЛИКАТИ ВСЕРЕДИНІ
			    ІНШОГО КЛАСУ І ВІН ТАКИМ ЧИНОМ ВШИЄТЬСЯ В ЦЕЙ КЛАС, І ТОДІ ВЖЕ ВІД instance, 
			    викликаємо будь-який атрибут з іншого класу 

			     ОБЄКТ - 
			'''

			class ClassA:

			    a = 10;
			    
			    def method1(self):
			        return a
			    def method2(self):
			    	return b


			class B():

			    instance = ClassA

			    try:
			    	# об'єкт що містить інформацію
			        if instance.method == True        
			            instance.method2()
			        else:
			            pass
			    except:
			        return 'Error'

			B()




		# 5 Використання класу в класі (КОЛИ ХОЧЕМО ПЕРЕОПРИДІЛИТИ ЗМІННІ В КЛАСІ), ПОТРІБНО ТАКОЖ ВИКОРИСТАТИ self.a, self.b - в методі класу,
																					# щоб переоприділити змінні: self.a, self.b

			class ClassA:

		    a = 10; b = 40

		    def __init__(self, a=a, b=b):
		        self.a = a
		        self.b = b


			class ClassB(ClassA):

			     def multiplication(self, a = 15, b = 40):
			        self.a = a
			        self.b = b
			        return self.a * self.b



		instance1 = ClassA()
		instance2 = ClassB()

		print(instance1.__class__.a - instance1.__class__.b)
		print(instance1.__class__.a - instance1.__class__.b)


		print(instance2.multiplication()) # по замовчуванні будуть ті, що в 1804 рядку
		print(instance2.multiplication(50, 50)) # їх також можна переоприділити вже викликавши екземпляр класу


СТВОРЕННЯ/ПРИКРІПЛЕННЯ НОВИХ АТРИБУТІВ ЧЕРЕЗ ООП:
        
        1) КЛАС

        2) ЕКЗЕМПЛЯР КЛАСУ 

		class ComplexNumber:

    		def __init__(self, r=0, i=0):
        		self.real = r
        		self.imag = i

    		def getData(self, real, imag):
        		return (f'{real}+{imag}j')
        		#print('{}+{}'.format(self.real, self.imag))

		instance2 = ComplexNumber(1) # ЗААССАЙНИМО АТРИБУТ real
		'''
		    2) ЧЕРЕЗ ЕКЗЕМПЛЯР:
		        1) instance2 = ComplexNumber(1) - СТВОРИЛИ ЕКЗЕМПЛЯР КЛАСУ ComplexNumber - instance2
		        2) ЗААССАЙНИЛИ НОВИЙ АТРИБУТ ЕКЗЕМПЛЯРУ ПРОСТИМ СПОСОБОМ: instance2.attr = 55 

		        Догрузили екзепляр класу instance2 - третім атрибутом, котрого немає в жодному 
		        в intstance1. 
		'''
		instance2.attr = 55

		print(instance2.real, instance2.imag, instance2.atttt)

		>>> 1 0 55


### НАДАННЯ ЗНАЧЕННЯ АТРИБУТУ КЛАСУ

		## АССАЙНИМО ЗНАЧЕННЯ АТРИБУТУ КЛАСУ:
		Person.money = 9500 - цей Атрибут зассайниться всередині класу, проте в mappingproxy() об'єкті він буде в кінці mappingproxy()
			>>> ... '__doc__': None, 'money': 9500} 


		## ДОДАВАННЯ АТРИБУТУ БЕЗПОСЕРЕДНЬО В КЛАС:
		setattr(obj, name, value) - прийматиме 3 параметри.
		        
		        1) object - Class Person
		        2) ім'я атрибуту - position
		        3) Value - значення Атрибуту

				setattr(Person, 'money', 11000)
				>>> weakref__' of 'Person' objects>, '__doc__': None, 'money': 'Ivan' }





Поліморфізм - в залежності від типу даних з якими ми працюємо, оператор діє по різному.
			  
			  Для прикладу оператор +:

			  якщо ми маємо дані у форматі int: + працює як математичний оператор
			  якщо ми маємо дані у форматі str: + працює як конкатенуючий оператор

			  оператор %, з str типами даних, format sryle - форматування str типів даних
			  оператор %, з int типами даних, спрацьовує як ділення по модулю x: 7%2 = 3




class Car:

	def drive():
		return 'Let\'s go'


exempliar = Car()


Function - функція, якщо вона викликається з класу: Car.drive().

Method - метод, якщо він викликається через екземпляр класу: exempliar.drive()

Bound method - метод, якщо ми до нього просто звертаємося через екземляр класу, але не викликаємо: exempliar.drive (<bound method Ball.ball_type of <__main__.Ball object at 0x7ff669cc7a30>>)

		як витягнути інфу з bound method 






# Class Atrributes (дані КЛАСУ):

### НАДАННЯ ЗНАЧЕННЯ АТРИБУТУ КЛАСУ

## АССАЙНИМО ЗНАЧЕННЯ АТРИБУТУ КЛАСУ:
Person.money = 9500 - цей Атрибут зассайниться всередині класу, проте в mappingproxy() об'єкті він буде в кінці mappingproxy()
	>>> ... '__doc__': None, 'money': 9500} 


## ДОДАВАННЯ АТРИБУТУ БЕЗПОСЕРЕДНЬО В КЛАС:
setattr(obj, name, value) - прийматиме 3 параметри.
        
        1) object - Class Person
        2) ім'я атрибуту - position
        3) Value - значення Атрибуту

		setattr(Person, 'money', 11000)
		>>> weakref__' of 'Person' objects>, '__doc__': None, 'money': 'Ivan' }


### ВИДАЛЕННЯ ЗНАЧЕННЯ АТРИБУТУ КЛАСУ

del - видалення атрибуту класу, звертання відбувається за класом та його атрибутом: 'del Сlass.name'
	  del - КОМАНАДА

		del Person.money
		>>> ...  None, 'position': 'Manager'} 

delattr(object) - вбудована функція, що видаляє Atrribute безпосередньо з object-Class 
		 
		# створили клас
		Class Person:
			name = 'Ivan'
			position = 'Manager'
			money = 9500

		# видалимо Атрибут за допомогою delattr(object)
		delattr(Person, money)
		>>> {'__module__': '__main__', 'name': 'Ivan', 'position': 'Manager', '__dict__': <attribute '....- Ivana немає
 
	ВИДАЛЯТИ МОЖНА ТАКОЖ І ЦІЛИЙ ОБ'ЄКТ: МЕТОД/КЛАС:

		class ComplexNumber:

    		def __init__(self, r=0, i=0):
		        self.real = r
		        self.imag = i

    		def getData(self, real, imag):
        		return (f'{real}+{imag}j')
        		#print('{}+{}'.format(self.real, self.imag))


		del ComplexNumber.getData - !!! ВИДАЛЕННЯ ЦІЛОГО ЕКЗЕМПЛЯРА КЛАСУ - БЕЗ КРУГЛИХ ДУЖОК (ТОБТО БЕЗ ВИКЛИКУ)



# ЗВЕРТАННЯ ДО АТРИБУТІВ КЛАСУ
Class_name.__dict__  - щоб продивитися всі окремі атрибути, якими володіє клас, дані виведуться у форматі mappingproxy(),
					   яка дуже схожа на dict() - винесуться усі атрибути Класу.
    
	print(Person.__dict__)
	>>>  {'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None, }
        

getattr(Person, 'name') - функція, яка виконує ЗВЕРТАННЯ ДО АТРИБУТІВ КЛАСУ,   
		1) перший параметр - об'єкт котрий ми хочемо перевірити на наявність атрибутів, найшвидше Class
        
        2) другий параметр - сам атрибут, що перевіряється, якщо такий є
            !!! назва Atrribute повинна бути в форматі STR - 'name', 'age', 'money' etc...

        3) якщо ж такого немає, то ми можемо добавити його, і його значення, що і повернеться
           значення атрибуту повернеться в результаті звернення до цього атрибуту

        print(getattr(Person, 'name'))
		>>> Ivan

Звертання через клас:
		
		class Point:
    		x = 1; y = 1
    
    	def setCoords(self, x, y):
        	self.x = x
        	self.y = y


		pt = Point()

		Point.setCoords(pt, 5, 10) # ЕКВІВАЛЕНТНІ РЯДКИ - ЗВЕРТАННЯ ЧЕРЕЗ КЛАС
		pt.setCoords(5, 10) # ЕКВІВАЛЕНТНІ РЯДКИ 


# ЗМІНА ЗНАЧЕНЬ АТРИБУТІВ КЛАСУ:
Person.name = 'Misha' # тобто Міша змінить Івана, так як Іван вже міститься в нашому класу
>>> ... 'money': 9500}


 ###########################ООП НАСЛІДУВАННЯ // OOP INHERITANCE ############################
		
		# опишемо знову class Car():
		class Car:
		    model = 'BMW'
		    engine = 1.6

		# створимо 2 екземпляри класу Car():
		a1 = Car() # батьківський клас обовязково повинен бути з дужками як метод
		a2 = Car()

		# додамо деякі значення до класу a1 = Car()

		# 1ий метод - АССАЙН:
		a1.color = 'yellow'
		# 2ий метод - setattr
		setattr(a1, 'color', 'yellow')
		print(a1.__dict__)

		'''
		    !!! ВАЖЛИВОЮ ДЕТАЛЛЮ, ПРИ ДОДАВАННІ АТРИБУТУ
		    ДО ЕКЗЕМПЛЯРУ КЛАСУ: МЕТОД __dict__ - ПОВЕРНЕ
		    СПИСОК САМЕ ТИХ АТРИБУТІВ, ЯКІ Є ВЖЕ ДОЧІРНІМИ
		    НЕ УНАСЛІДУВАНІ ВІД БАТЬКІВСЬКОГО КЛАСУ
		'''
		# далі змінимо, батьківський Атрибут 'model' з 
		# BMW на 'Tesla'
		setattr(a1, 'model', 'Tesla')
		print(a1.__dict__)
		## як насілідок dict() дочірніх Атрибутів:
		## вже буде мати  значення: {'color': 'yellow', 'model': 'Tesla'}

		'''
		    a1 - дочірній екземпляр class Car
		    МІСТИТЬ В СОБІ АТРИБУТ - model,
		    ЩО БУВ ВСТАНОВЛЕНИЙ ОКРЕМО, ЯК АТРИБУТ ДОЧІРНЬОГО
		    ЕКЗЕМПЛЯРУ class Car().

		    !!! ПРИ ВИКЛИКУ: в 1ШУ ЧЕРГУ БУДЕ ПОВЕРТАТИСЬ,
		    AТРИБУТ 'model' - дочірнього екземпляру!!!

		    !!! як бачимо в dict() дочірніх атрибутів,
		        Атрибут 'engine' - відсутній.
		        ПРОТЕ АТРИБУТ engine ВЛАСТИВИЙ БАТЬКІВСЬКОМУ КЛАСУ
		        І ЯКЩО МИ ЗВРНЕМОСЬ ДО АТРИБУТУ engine - ТО ВІН ВИВЕДЕТЬСЯ 
		        БЕЗ ПРОБЛЕМ, ОСКІЛЬКИ ПІДТЯГНЕТЬСЯ З БАТЬКІВСЬКОГО КЛАСУ 

		'''
		print(a1.engine)
		#>>> 1.6

		## ЗААССАЙНИМО АТРИБУТ ДЛЯ ЕКЗЕМПЛЯРА a2:
		a2.seats = 4
		print(a2.__dict__)
		#>>> {'seats': 4}

		## спробуємо звернутися до цього атрибуту,
		## проте в екземплярі класу a1:
		try:
		    print(a1.seats)
		except AttributeError:
		    print('Потрібно надати батьківському або екземпляру батьківського класу a1 - \
		    атрибуту seats, він наразі відсутній')

		'''
		    ЯКЩО ЗВЕРНЕМОСЬ ДО АТРИБУТУ, КОТРИЙ
		    ВЛАСТИВИЙ 1НОМУ З ДОЧІРНІХ КЛАСІВ,
		    ПРОТЕ НЕ ВЛАСТИВИЙ 2ОМУ ДОЧІРНЬОМУ А ТАКОЖ
		    БАТЬКІВСЬКОМУ:
		    викине AttributeError: 'Car' object has no attribute 'seats'

		    !!! ТОМУ ДЛЯ ВИКЛИКУ АТРИБУТА З ДОЧІРНЬОГО КЛАСУ, ПОТРІБНО
		    СТВОРИТИ/ЗААССАЙНИТИ ЙОГО В ДОЧІРНЬОМУ АБО БАТЬКІВСЬКОМУ КЛАСІ
		'''

		# створимо цей Атрибут в батьківському класі
		setattr(Car, 'seats', 4)
		print(Car.seats)
		# або через Ассайн
		Car.seats = 5

		'''
    		ВИКЛИЧЕМО АТРИБУТ В ДОЧІРНЬОМУ КЛАСІ A1
    		ОСКІЛЬКИ АТРИБУТ ПРИСВОЇТЬСЯ, БАТЬКІВСЬКОМУ КЛАСУ 
    		ТО ВІН ПЕРЕДАСТЬСЯ І ДОЧІРНЬОМУ A2

    		!!! АТРИБУТИ ПРИСВОЄНІ БАТЬКІВСЬКОМУ КЛАСУ,
        	БЕЗ ПРОБЛЕМ ВИКЛИКАЮТЬСЯ В ДОЧІРНЬОМУ 
        	ЕКЗЕМПЛЯРАХ КЛАСУ
		'''

		print(a1.seats)
		#>> виведеться 5.
		# seats присвоїться в дочірній екземпляр a1




### ФУНКЦІЯ ВСЕРЕДИНІ КЛАСУ:
## відсутність наслідування

# cтворимо клас
class Car:

    model = 'BMW'
    engine = 1.6

    # Ці Атрибути не унаслідуються функцією drive(),
    # ОСКІЛЬКИ ФУНКЦІЯ drive() - порожня, НЕ МІСТИТЬ ПАРАМЕТРУ
    # тому їх потрібно буде помістити
    # всередину функції

    #V_zero = 5
    #T = 60
    #a = 1.6

    def drive():
        # return model - 'NameError: name 'model' is not defined' - відбудеться, тому що
        # функція drive() - немає параметра, НЕ УНАСЛІДУЄ ВІД ГОЛОВНОГО КЛАСУ Car ніяких особливостей

        V_zero = 5
        T = 60
        a = 1.6

        S = (V_zero * T) + ((a*T**2)/2) # формула визначення шляху
        return f'{S} metres'


print(Car.drive()) # функція з дужками означатиме: ВИКОНАННЯ ЦІЄЇ ФУНКЦІЇ
print(Car.drive) # функція без дужок означатиме: ЗВЕРТАННЯ ДО ОБ'ЄКТА ЩО ЗБЕРІГАЄТЬСЯ ЗГІДНО ІМЕНІ ЦІЄЇ ФУНКЦІЇ

	Звертання до функції:

		print(Car.drive) # функція без дужок означатиме: ЗВЕРТАННЯ ДО ОБ'ЄКТА ЩО ЗБЕРІГАЄТЬСЯ ЗГІДНО ІМЕНІ ЦІЄЇ ФУНКЦІЇ

		'''
		    1) Car.drive - функція без дужок означатиме:
		        ЗВЕРТАННЯ ДО ОБ'ЄКТА, ЩО ЗБЕРІГАЄТЬСЯ
		        ЗГІДНО ІМЕНІ ЦІЄЇ ФУНКЦІЇ. Повернеться об'єкт в памяті
		        закріплений за іменем цієї функції: <function Car.drive at 0x7f8507a940d0>

		    2) getattr(Car, 'drive') - Атрибут, 'drive'- обовязково в лапках: <function Car.drive at 0x7f8507a940d0>
		     закріплений за іменем цієї функції: <function Car.drive at 0x7f8507a940d0>
		'''	

		#Звертання до фунції відбувається звичним способом як і до стандартного об'єкта

		1 - ASSIGHN
		print(Car.drive)
		#>>> <function Car.drive at 0x7f52ae1b30d0>

		2 функція getattr() - функція, яка виконує звертання до атрибутів класу
		print(getattr(Car, 'drive'))
		#>>> <function Car.drive at 0x7f52ae1b30d0>

	ВИКОНАННЯ ФУНКЦІЇ
	
	'''
	    ВИКОНАННЯ ФУНКЦІЇ - ПРОСТАВИТИ () ДУЖКИ: Car.function()

	    1) Car.drive() - функція з дужками означатиме:
	          ВИКОНАННЯ ЦІЄЇ ФУНКЦІЇ, всередині класу Car

	    !!! 2) функція getattr(object, fucntion) () - обовязково дужки, щоб 
	            відбувся виклик функції - 1919 рядок
	'''

	1ий спосіб - ASSIGHN
	  print(Car.drive()) # функція з дужками означатиме: ВИКОНАННЯ ЦІЄЇ ФУНКЦІЇ


	2ий спосіб - функція getattr()
	  print(getattr(Car, 'drive') ()) # 2ий ВАРІАНТ ВИКОНАННЯ ЦІЄЇ ФУНКЦІЇ

## ДЕКОРАТОР
		class Car:
    		model = 'BMW'
    		engine = 1.6

    	def drive():
        	print('Lets go')

	'''
    !!! ПРИ НЕОЗНАЧЕНОМУ АССАЙНЕННІ ФУНКЦІЇ 
        ВСЕРЕДИНІ КЛАСУ - function(), така функція зможе викликатися тільки
        через батьківський клас Car()
        
        Car.drive()

        ПРОТЕ НІЯК ЧЕРЕЗ ДОЧІРНІЙ КЛАС - a1 (тільки звертання,
        тоді повернеться - bound method Car.drive)

        !!! ЯКЩО ХОЧЕМО ВИКЛИКАТИ ФУНКЦІЮ ЧЕРЕЗ ДОЧІРІНЙ КЛАС,
            ПОТРІБНО ВИКОРИСТОВУВАТИ ДЕКОРАТОР

		@staticmethod - дозволяє викликати порожню функцію,
		через ЕКЗЕМПЛЯР КЛАСУ, якщо такий не містить її в свому тілі, 
		а успадкував від батьківського класу
	'''

		# ДЕКОРАТОР НА ПРИКЛАДІ:
		# cтворимо клас

		class Car:

		    model = 'BMW'
		    engine = 1.6

		    @staticmethod
		    def drive():
		        print('Let\'s go')#- 'NameError: name 'model' is not defined' - відбудеться, тому що
		        # функція drive() - немає параметра, НЕ УНАСЛІДУЄ ВІД ГОЛОВНОГО КЛАСУ Car ніяких особливостей

		instance1 = Car() # instance1 - екземпляр #1

		print(instance1.drive())


## ПАРАМЕТР self - НАДАННЯ МЕТОДАМ ТА ФУНКЦІЯМ ВСЕРЕДИНІ КЛАСУ МОЖЛИВОСТІ БУТИ ВИКЛИКАНИМИ - З ЕКЗЕМПЛЯРІВ КЛАСУ
		
		параметр self - можливість методів бути викликаними з екземплярів класу class
		параметр self - обовязковий Атрибут синтаксису Python

		Концепція роботи self:

			Припустимо є 2 прості класи СlassA та СlassB:

				class ClassA:                                        					class ClassB:
					a = 10; b = 20									     					x = 0.5; y = 1.5

					def method(self):                                    					def method1(self):                                
						return "Hello"															return "Hello"

																	     					def method2(self):
																								return 'World'

				instance1 = ClassA()													instance2 = ClassB
		


		Тепер, коли ми створюємо будь-який екземпляр класу СlassA чи СlassB:     	|   ІНФОРМАЦІЯ ПРО СТВОРЕННЯ instance2 ПІДЕ У ВСІ МЕТОДИ,

				instance1 = classA(),                                               |   ЩО МІСТЯТЬ by_default ПАРАМЕТР self

				параметр self передасться, всім функціям, що містять                |   ВИРАЗ: 
				в свому тілі цей параметр.                                          |				СlassB.method1(instance1)

				self буде містити інформацію про всі екземпляри класу classA,       |                          ||
				створені поза межами цього класу.                                   |                
                                                                                                       instance.method1()
				всі методи, що містять параметр self, тепер можуть бути викликані   |
				з допомогою екземплярів класу                                       |	PYHON ЗАМІСТЬ ЗМІННОЇ self АВТОМАТИЧНО ЗАПИШЕ,
																						В КОЖЕН МЕТОД КОТРИЙ МАЄ ЦЕЙ ПАРАМЕТР, instance1
																						(ІНФОРМАЦІЮ ПРО instance1)

																						ЗА НАС ЦЕ ВСЕ РОБИТЬ ІНТЕРПРЕТАТОР

																						ЦЕ ЯКРАЗ Є БАЗОВОЮ КОНЦЕПЦІЄЮ ООП

		'''
		    ПАРАМЕТР self, як аргумент функції 

		    ЗГІДНО СИНТАКСИСУ ПАЙТОН - 
		    БУДЬ-ЯКИЙ МЕТОД/ФУНКЦІЯ СТВОРЕНА,
		    В ТІЛІ КЛАСУ class, повинна приймати параметр self

		    self - keyword. За цим параметром - отримуємо доступ до атрибутів(даних)
		        та методів класу в Python.
		'''

		# cтворимо клас Point
		class Point:
		    x = 1; y = 1

		    def setCoords(self):
		        return 'It\'s ok'

		pt = Point()
		print(pt.setCoords()) # без переданого параметра self - метод setCoords не повернеться 

		#>>> 'It\'s ok'      

		## ПАРАМЕТР self
		'''
		    ФУНКЦІЯ ПАРАМЕТРА self:
		'''

		# cтворимо екземпляр класу Point
		# дочірній екземпляр instance

		instance = Point()
		print(instance.x) # викликали батьківський атрибут x, через дочірній екземпляр instance

		'''
		    ОТОЖ. ТЕПЕР НАДАВШИ ЦІЙ ФУНКЦІЇ ПАРАМЕТРУ self
		    МИ МОЖЕМО ВИКЛИКАТИ ЇЇ ЧЕРЕЗ ДОЧІРНІ ЕКЗЕМПЛЯРИ КЛАСУ
		'''

		# СПОСІБ №1 - getattr()
		print(getattr(instance, 'setCoords') ())

		# СПОСІБ №2 - ASSIGHN
		print(instance.setCoords())


		'''
		    ОПИС №1:
		    instance.setCoords(),
		    setCoords() - при виклику цього методу,
		    параметр self (що є ПАРАМЕТРОМ МЕТОДУ setcoords()) -- def setCoords(self):
		                                                                        |
		                                                                        |
		                                                                        \/
		    буде ссилатися на параметр викл доч екземп -----> instance.setCoords()
		    таким чином параметр self - автоматично стане параметром - instance.setCoords() == instance.setCoords(self)

		    https://prnt.sc/wevttl

		'''

		ДАЛІ --->:

			через self - можемо перевизначити змінні всередині цього методу

			class Point:
    			x = 1; y = 1
    
    			def setCoords(self, x, y):
        			self.x = x
        			self.y = y
        			#self.a = x

        			return x*y

        			!!! self - ссилається на той екзмпляр класу, з якого викликається метод, в якому він переданий

					|_______________
								   \|/	
						pt1 = Point() # створили #1 екземпляр класу
					|______________\|/	
						pt2 = Point() # створили #2 екземпляр класу
					|______________\|/	
						pt3 = Point() # створили #3 екземпляр класу
						


					pt = Point()
					#pt.x = 5 - оскільки ми перевизначили змінні x, y вcередині методу setCoords
					#pt.y = 10 - оскільки ми перевизначили змінні x, y вcередині методу setCoords
 
					# Point.setCoords(5, 10) # ВИНИКНЕ ПОМИЛКА, ОСКІЛЬКИ ПОТРІБНО ДОВНЕСТИ ПАРАМЕТР - ЕКЗЕМПЛЯР pt - класу point()
					Point.setCoords(pt, 5, 10) # еквівалент
					pt.setCoords(5, 10) # еквівалент

					#>>> x*y == 5*10 = 50

		3) ПАРАМЕТР, ЯКОМУ ПРИСВОЇЛИ self всередині методу, можна використовувати в іншому методі

				class A:

					def method1(self):
						lst = list(range(10))
						self.lst = lst
						return lst

					def method2(self):
						return [i**2 for i in self.lst]

					#>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


### Конструктор 

'''
    INIT - потрібен для того щоб заінізіалізувати,
           атрибути класу,  які будуть ПЕРЕДАВАТИСЯ НА ДОЧІРНІ КЛАСИ
           АБО ДОЧІРНІ ЕКЗЕМПЛЯРИ КЛАСУ

            для прикладу у var1, Class Distance - УСПАДКУЄ УНАСЛІДУВАНІ 
            ВІД КЛАСУ Runner - атрибути,

            В  var#1 - НЕМАЄ НЕОБХІДНОСТІ ЗАСТОСОВУВАТИ АТРИБУТИ 
            В ЕКЗЕМПЛЯРІ КЛАСУБ ТАК ЯК ВОНИ ПО ЗАМОВУЧУВАННІ ЗАІНІЦІАЛІЗОВАНІ

             В  var#2 - НЕОБХІДНО ЗАСТОСОВУВАТИ АТРИБУТИ
            TypeError: __init__() missing 3 required positional arguments: 'V_zero', 'a', and 'T'


            !!! якщо НЕОЗНАЧЕНА ВІЛЬНА ЗМІННА ВЖЕ Є В КОНСТРУКТОРІ,
                ТО ЇЇ ПОТРІБНО ПРЕЕДАВАТИ ВЖЕ ПРИ ІНТАНЦІАЦІЇ В ПРИ ФОРМУВАННІ
                ЕКЗМПЛЯРА КЛАСУ:

                def __init__(self, V_zero, a = a, T = T) - в даному випадку V_zero

'''

		
		# var#1  
		class Runner:

		    V_zero = 0; a = 1.2; T = 180

		    def __init__(self, V_zero = V_zero, a = a, T = T):
		        self.V_zero = V_zero
		        self.T = T
		        self.a = a

		class Distance(Runner):
			def distance(self):
				S = self.V_zero * self.T + (self.a * self.T**2)/2 #!!! ЯКЩО Б self не було, то це означатиме, що змінні потрібно буде описати в тілі методу distance()
				return f'{S} metres'

		exempliar = Distance(0, 1.3, 180)
		print(exempliar.distance())
		#rint(round((exempliar.distance()), 1))


		# var#2
		# винесли параметр в екземпляр класу
		class Runner:

		    V_zero = 0; a = 1.2; T = 180

		    def __init__(self, V_zero = V_zero, a = a, T = T):
		        self.V_zero = V_zero
		        self.T = T
		        self.a = a

		class Distance(Runner):
			def distance(self, V_zero, a, T):
				S = V_zero * T + (a * T**2)/2
				return f'{S} metres'

		exempliar = Distance()
		print(exempliar.distance(0, 1.3, 180)) # якщо параметри забрати з методу,
										       # то вони підтягнуться як АТРИБУТИ ОСНОВНОГО КЛАСУ by_default


		# var#3
		class Runner:

		    V_zero = 0; a = 1.2; T = 180

		    def __init__(self, V_zero, a, T):
		        self.V_zero = V_zero
		        self.T = T
		        self.a = a

		class Distance(Runner):
			def distance(self):
				S = self.V_zero * self.T + (self.a * self.T**2)/2 # якщо параметри будуть без self, то потрібно буде
				return S                                          # протсавити їх у тіло методу distance, і передати 
				                                                  # тоді надати туж кількість параметрів, як атрибути в екземлярі класу звертанні
				                                                  # до distance

		exempliar = Distance(1, 1, 150)
		print(round((exempliar.distance()), 1))


		АНАЛОГІЧНЕ ПОЯСНЕННЯ - https://www.youtube.com/watch?v=dx0HVOSPJ7k&list=PLCDQgr9-oP0y6cnLL8A4EOvEAmb-jUsVX&index=9&ab_channel=mentorL%26K
		Liybov Koliasa



Magic Methods:
## Конструктор __init__:


__init__, - АСААЙНЕННЯ параметрів БАТЬКІВСЬКОГО КЛАСУ, які будуть ПЕРЕДАВАТИСЯ НА ДОЧІРНІ КЛАСИ АБО ДОЧІРНІ ЕКЗЕМПЛЯРИ КЛАСУ	
	TypeError: __init__() missing 3 required positional arguments: 'length', 'width', and 'height' - найпоширеніша помилка при використанні конструктора 

	
		# OOP - __init__

		''''
		    __init__ - шаблон передачі змінних,
		    які передасть юзер в нашу програму (клас).

		    Тобто __init__ - консруктор, який вказує,
		    що саме потрібно передавати в якості аргументів (об'єктів)
		    класу

		    # https://younglinux.info/oopython/init.php

		    метод всередині класу - вже перевизначає,
		    конструкцію нашого класу
		'''

		# var1 - в __init__ - задали, котрі саме атрибути
		# потрібно буде внести, в якості параметрів класу 
		class Person:

		    def __init__(self, s, n):
		        self.name = n
		        self.surname = s

		p1 = Person('Sam', 'Smith')
		print(p1.name, p1.surname)
		#>>> Sam Fisher


		# var2 - в __init__ - передали готовий параметр, тому якщо
		# не передати цей параметр, він підтягнеться з __init__ автоматично 
		class Person:

		    def __init__(self, s, n='Fisher'):
		        self.name = n
		        self.surname = s

		p1 = Person('Sam')
		print(p1.name, p1.surname)
		#>>> Sam Fisher


		# var3 
		# з допомогою цього класу для прикладу,
		# можна заініціалізувати основні атрибути і
		# використовувати їх вже в інших класах 
		class Person:

		    s = 'Adams'; n = 'Corey';

		    def __init__(self, s=s, n=n):
		        self.name = n
		        self.surname = s


		instance = Person('Sam', 'Fisher') # якщо передати ці параметри то вони замінять заінціалізовнаі by_default
		print(instance.name, instance.surname)


		print(getattr(p1, 'name')) #>>> Sam - витягне аргумент через екземпляр класу
		print(getattr(p1, 'surname')) #>>> Fisher - витягне аргумент через екземпляр класу




		# var4 - задали конструктор класу Runner
		# зассайнили нульові змінні, __init__
		# виступив конструктором нульових змінних
		# дл того щоб їх можна було задати в 
		# instances класу Runner 

		class Runner:

		    def __init__(self, V_zero=0, T=0, a=0):
		        self.V_zero = V_zero
		        self.T = T
		        self.a = a

		    def distance(self, V_zero, T, a):
		        S = V_zero * T + (a * T**2 * 0.5)
		        return S

		    # ex2
		    #def distance(self, V_zero=0, T=0, a=0):
		        #S = V_zero * T + (a * T**2 * 0.5)
		        #return S

		exempliar = Runner(1, 1.6, 180)      
		#print(round((exempliar.distance()), 1)) ex2, потрібно надати атрибутам значення

		exempliar = Runner()
		print(round((exempliar.distance(1, 1.6, 180)), 1))


		# var4.1 - можна реалізувати задавши стандартні
		# атрибути класу
		# тоді вже від імені різних методів
		# вибирати для котрого які саме параметри
		# задавати
		class Runner:

		    V_zero = 0; T = 180; a = 0.025;

		    def __init__(self, V_zero=V_zero, T=T, a=a):
		        self.V_zero = V_zero
		        self.T = T
		        self.a = a

		    def distance(self, V_zero=V_zero, T=T, a=a):
		        S = V_zero * T + (a * T**2 * 0.5)
		        return S

		# var1
		auto_instance = Runner()
		print(auto_instance.distance())
		# >>> 405.0

		# var2
		instance_input = Runner()
		print(instance_input.distance(1, 105, 0.25))
		# >>> 1483.125



__del__ - деструктор. Окремий вбудований маgic method в пайтон котрий видалить instance або atrribute.

	class Person:

		def __init__(self, n, s, q=1):   
		    self.name = n
		    self.surname = s
		    self.qualification = q

		def show_info(self):
		    # return f'Employee info: name - {self.name}, surname - {self.surname}, qualification - {self.qualification}'
		    return 'Employee info: name - %s, surname - %s, qualification - %d' % (self.name, self.surname, self.qualification)
		    
	class Dismiss(Person):

	    def __del__(self):
	        print('Good bye mr. %s %s' % (self.name, self.surname))


		## creating 3 objects
		person1 =  Person('Tim', 'Morrison')
		person2 = Person('Stacey', 'Ashcroft')
		person3 = Person('Mike', 'Johnson')

		## display info
		print(person1.show_info())
		print(person2.show_info())
		print(person3.show_info())


		## dismiss instance
		dismiss = Dismiss(person2.name, person2.surname)
		del dismiss


		#Employee info: name - Tim, surname - Morrison, qualification - 1
		#Employee info: name - Stacey, surname - Ashcroft, qualification - 1
		#Employee info: name - Mike, surname - Johnson, qualification - 1
		#Good bye mr. Stacey Ashcroft







MAGIC METHODS:

	'''
    Магічні методи це методи, 
    double underscore methods:
    dunder methods:

    __str__: відповідають за текстове відображення нашого об'єкта 
             в UI., те як об'єкт бачить користувач.

    __repr__: відповідають за текстове відображення
              нашого об'єкта в системі (як його бачать програмісти, 
              системний код).

    Відповідають за текстове відображення нашого об'єкта 
    в UI.

    відображає те як цей об'єкт бачить користувач,
    !!! без __str__ нам підтягнеться технічна інформація про,
        об'єкт у вигляді:

        <__main__.Lion object at 0x7ff5266cbe50>

'''


__repr__ - represent. відповідають за текстове відображення, нашого об'єкта в системі (як його бачать програмісти, системний код).
		   наш обє'кт у вигляді, текстового формату даних, в який можна помістити тех інформацію котра виведеться:
		   Наш клас містить наступну інформацію для девелоперів: Leo

    	   Проте, __repr__ відобразить інфу для юзера тільки всередині системи,
           для UI потрібен __str__


		   class Lion:

    		   def __init__(self, name):
        	   self.name = name

    	    def __repr__(self):
        		return f'Наш клас містить наступну інформацію для девелоперів: {self.name} '


			instance = Lion('Leo')
			print(instance)

  

__str__ - дозволяє, вивести на екран ініціалізований об'єкт. наприклад з конструктора __init__.

			class Point:

			def __init__(self, x=10, y=25, z=40):
			    self.x = x
			    self.y = y
			    self.z = z
    
    		def __str__(self):
        		return '%d, %d, %d' % (self.x, self.y, self.z)

        		#>>> 10, 25, 40	

        	# перевизначили клас, додавання комплексних чисел
        	Комплексні числа: С = (x, iy) ## наприклад (3, 5)

        	def __add__(self, other):
        		x = (self.x + other.x)
        		y = (self.y + other.y)
        		z = (self.z + other.z)
        		return Point(x, y, z)



		SPECIAL FUNCTIONS:
		Використовуючи спеціальні магічні функції, ми можемо зробити наш клас сумісним із вбудованими функціями.
		Для прикладу перевизначити клас __add__ щоб оперувати додванням об'єктів, які звичайні built-in functions або methods піднімлять помилку

__add__ -  метод __add__ - для перевизначення класу, а саме, що перетворення змінних, обробивши їх формулою, або іншим алгоритмом
		
		    def __add__(self, other):
        		x = self.x + other.x
        		y = self.y + other.y
        		z = self.z + other.z

        		return Point(x, y, z)

        		p1 = Point(2, 4, 6)
				p2 = Point(3, 5, 7)
				print(p1 + p2)

        		#>>> (5, 9, 11)
__radd__ - той же метод __add__ - при якому наш об'єкт стоїть зправа
		

			class TestClass:

			    def __init__(self, name, balance):
			        self.name = name
			        self.balance = balance

			    def __add__(self, other):

					# ДЛЯ ДОДАВАННЯ ЗНАЧЕНЬ 2ОХ КЛАСІВ
			        if isinstance(other, (TestClass)):
			            return self.balance + other.balance  ## other.balance - бо ця змінна означена в методі __add__(self, other)

			        # ДЛЯ ДОДАВАННЯ ДЕЯКОГО INT ЗНАЧЕННЯ ДО ПЕРШОГО КЛАСУ self.
			        elif isinstance(other, (int, float)):
			            return other + self.balance  # intove значення яке проставляється як атрибут класу

			        else:
			            return 'Error'
			    
			    def __radd__(self, other):
			        print('__radd__call')
			        return self + other


		a = TestClass('Smith', 500)
		r = TestClass('Carpenter', 600)

		print(100+r)
		>>> 100 + 600                     # де 600 == other


__mul__ - множення аргументів через множник "*"ґ


			class Mult:

			    def __init__(self, surname, balance):
			        self.surname = surname
			        self.balance = balance

			    def __mul__(self, other):
			        ##1 int
			        if isinstance(other, (int, float)):
			            return self.balance * other ### ЧИСЛО ЯКЕ ЗНАХОДИТЬСЯ СПРАВА

			        ##2 str
			        elif isinstance(other, (str)):
			            return self.balance * other ## МНОЖЕННЯ МІЖ int змінною та str типами даних

			        ##3 instance * instance
			        elif isinstance(other, Mult):
			            return other.balance * self.balance  ## МНОЖЕННЯ МІЖ 2ОМА ЗМІННИМИ

			        else:
			            return 'error'


			##3 instance * instance
			mult1 = Mult('Smith', 2000)
			change1 = Mult('shiftmake', 2.5)
			print(mult1*change1)

			### ТАКОЖ МОЖНА МНОЖИТИ НА БУДЬ-ЯКИЙ МНОЖНИК
			##1 int
			print(mult1*4.5)
			#>>>9000

			### ТАКОЖ МОЖНА ПОМНОЖИТИ НА БУДЬ-ЯКИЙ 'str' тип даних
			##2 str
			c = Mult('staff', 5)
			print(c*'this_is_str')


		### РЕАЛІЗУВАТИ ЦЕ МОЖНА ТАКОЖ ЧЕРЕЗ МАГІЧНИЙ МЕТОД __add__ - просто прописавши у ньому множення

				class Mult:

		    def __init__(self, surname, balance):
		        self.surname = surname
		        self.balance = balance

		    def __add__(self, other):
		        if isinstance(other, (int, float)):
		            return self.balance * other ### ЧИСЛО ЯКЕ ЗНАХОДИТЬСЯ СПРАВА

		        elif isinstance(other, Mult):
		            return other.balance * self.balance  ## МНОЖЕННЯ МІЖ 2ОМА ЗМІННИМИ

		        else:
		            return error
		            

				mult1 = Mult('Smith', 1000)
				change1 = Mult('shiftmake', 5)
				print(mult1 + change1)
				>>> 5000


__sub__ - АНАЛОГІЧНО __mul__

__truediv__- АНАЛОГІЧНО __mul__


__getattr__ -  приймає один уявний аргумент, який згодом можна буде повернути від екземпляра класу, одразу створивши його
			- cтоврює порожню ячейку для атрибуту поза класом, котрий можна буде створити і назвати як нам до вподоби
			- створює значення - з вільною ячейкою для назви атрибуту
			
			## приклад№1:
			class Count():
    			def __init__(self,mymin,mymax):
        			self.mymin=mymin
        			self.mymax=mymax

        	x = Count(4, 6)
			print(x.mymin) ## видасть4
			print(x.mymax) ## видасть6
			print(x.sum) ## видасть AttriButeError так як цього атрибуту немає
			
			## приклад№2:
			class Count():
    			def __init__(self,mymin,mymax):
        			self.mymin=mymin
        			self.mymax=mymax 

        		def __getattr__(self, item):
        			self.__dict__[item]=10
        			return self.item

        	x = Count(4, 6)
			print(x.mymin) ## видасть4
			print(x.mymax) ## видасть6
			print(x.sum) ## створить новий атрибут, під значення 10











OVERLOADING OPERATORS:

Addition: p1 + p2   p1.__add__(p2)

Subtraction: p1 - p2  p1.__sub__(p2) 

Multiplication: p1 * p2  p1.__mul__(p2)

Power: p1 ** p2  p1.__pow__(p2)
 
Division: p1 / p2  p1.__truediv__(p2)
 
Floor Division: p1 // p2  p1.__floordiv__(p2)

Reminder (modulo): p1 % p2  p1.__mod__(p2) 



# ВАРІАНТ РОЗМІЩЕННЯ АТРИБУТІВ ВСЕРЕДИНІ БАТЬКІВСЬКОГО КЛАСУ - ТА ВИКОРИСТАННЯ ЇХ В ДОЧІРНІХ КЛАСАХ ТА ЕКЗЕМПЛРАХ КЛАСУ
		
		class classA:

	    	x = 4; y = 8

	    	def __init__(self, x = x, y = y):
	        	self.x = x
	        	self.y = y
	    
	    	def execution(self, x, y):
	        	return x * y

			exempliar = classA()
			print(exempliar.execution(4, 8))



# отримання доступу до атрибуту класу - з body, класу
		
		якщо змінна x - заініціалізована в __init__()
										   
		class Simple:

		    x = 10;
		    y = 20;
		    z = 30

		    def __init__(self, x = x, y = y, z = z):
		        self.x = x
		        self.y = y
		        self.z = z

		instance = Simple()

			print(instance.x) # через екз класу
			print(instance.y)
			print(instance.z)
		>>> 10
			20
			30

			print(getattr(instance, 'x')) # через ООП
			print(getattr(instance, 'y'))
			print(getattr(instance, 'z'))
		>>> 10
			20
			30	


		instance = Simple()


		## перевірка може бути тільки на ТИП
		if isinstance(instance, Simple):
		    print(isinstance(instance, Simple))
		else:
		    print(0)

		>>> True



		# звертання до атрибутів класу
		class ClassA:

 
ЗВЕРТАННЯ ЧЕРЕЗ БАТЬКІВСЬКИЙ КЛАС :         									Сlass.method(par1, par2)

	
	### ЗВЕРТАННЯ ЧЕРЕЗ БАТЬКІВСЬКИЙ ClassA
	class ClassA:

	    arg1 = 5
	    arg2 = 10

	    def methodA(arg1, arg2):
	        return arg1*arg2

	'''
	    при звертанні до ЕКЗЕМПЛЯРУ КЛАСА methodA,
	    в такому випадку потрібно буде звертатися 
	    через батьківський клас ObjectA,
	'''
	ObjectB = ClassA() # створили екземпляр класу A - objectB
	print(ClassA.methodA(10, 5))


ЗВЕРТАННЯ ЧЕРЕЗ ЕКЗЕМПЛЯи КЛАСУ:                                                instance = ClassA
																				instance.method(par1, par2)
		

	    '''
	        Звертання до атрибутів КЛАСУ
	    '''
	    
	    a = 10; b = 50 # атрибути ClassA - дані що містить СlassA, котрими ми будемо розпоряджатися

	    def function(self):
	        return 'Do something'

		# звертання до атрибуту класу через екземпляр класу
		instance1 = ClassA()
		print(instance1.__class__.a)

# отримання доступу безпосередньо з __init__:
		
		#VAR Liybov Koliasa:
		class Parrot:

    	species = 'bird'

    	def __init__(self,  name, age=0): # ПАРАМЕТР age - містить значення by_default()
        	self.name = name
        	self.age = age  

		# instantiation of instances:
		# потрібно передати аргумент name - бо він в нас неозначений
		blue = Parrot('Kesha')
		print(blue.name)
		#>>> Kesha

		red = Parrot('Gosha')
		print(red.name)        АБО print(f'Red parrot is {red__class__.name}')  АБО print(f'Red parrot is {red.name}')


		!!!! ВАЖЛИВА ХАРАКТЕРИСТИКА ООП:

			red__class__.name буде тотожне поняттю red.name (оскільки Python автоматично отримає інфу про instance - при інстанціації цього екземпляру від батьівського класу Parrot)
			ВІДБУВАЄТЬСЯ ЦЕ ЗА РАХУНОК ПАРАМЕТРА self






## НУЛЬОВІ ПАРАМЕТРИ В КОНСТРУКТОРІ:
		'''
		    !!! якщо парметри в конструкторі __init__ зазаначені як:
		        
		        __init__(self, x = 0, y = 0):

		        В такому випадку МЕТОД КЛАСА - МОЖНА БУДЕ ВИКЛИКАТИ,
		        без ПАРАМЕТРІВ: pt = Point(), проте повинні бути передані 
		        як ПАРАМЕТРИ ЕКЗЕМПЛЯРА КЛАСУ

		        якщо не присвоїти x, y - 0ві значення,
		        то ОБОВЯЗКОВОЮ УМОВОЮ БУДЕ ПЕРЕДАЧА
		        ПАРАМЕТРІВ В pt = Point(4, 8)
		        А ТАКОЖ 

		'''

		class Point:
		    
		    def __init__(self, x = 0, y = 0):
		        
		        self.x = x
		        self.y = y

		    def setCoords(self, x, y):
		        
		        self.a = x
		        self.b = y
		        return x * y

		pt = Point()
		print(pt.setCoords(4))
		# можна передавати тільки 1ин атрибут, інший буде by_default


		class Point:
		    
			def __init__(self, x = 0, y = 0):        
				self.x = x
				self.y = y

			def setCoords(self, x, y):
				return x * y

		pt = Point()
		print(pt.setCoords(4, 8))
		#обовязково передавати 2 атрибути, by_default - немає


### Buit-In Fucntions in OOP:
!!! ## перевірка може бути тільки на ТИП 
	1) <class by_default> - тип даних str, int, tuple....
	2) <class '__main__.Point'> - тип або клас створений нами самими (ТАК ЯК КЛАС ЦЕ НАМИ ВЛАСНЕ СТВОРЕНИЙ ТИП)

isinstance(object, type) - фунція, як перевіряє чи належить даний об'єкт іншому об'єкту, є даними іншого класу або екземпляру класу
		
		isinstance коротко: is this an  instance --- тобто чи це об'єкт
		
		var1: - з її допомогою можна також перевірити чи належить об'єкт до певного типу (певного типу даних) як із варіантом type()

		x = isinstance(5, int)
		#>>> True

		var2:
		class myObj:
  			name = "John"

			y = myObj()

			x = isinstance(y, myObj) # myObj - є екземпляром класу myObj
			# >>> True

		var3:
		Крім того, isinstance() за порівнянням з type() дозволяє перевірити дані на приналежності, хоча б одному типу із кортежу, переданого у якості другого аргументу

		a = (5, 10)

		isinstance(a,(float, int, str, tuple))
		>>> True

		isinstance(a,(float, int, str))
		>>> False








приклад простого класу
Example 2: oct() for custom objects
class Person:
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print('The oct is:', oct(person))


















HEX таблиця (hexadecimal encoding)

		'''
		    Шістнадцяткова система числення - 'hex', скорочено від слова 'hexadecimal'
		    Позиційна система числення, ЯКА ЗРУЧНО ДАЄ МОЖЛИВІСТЬ ЗАПИСАТИ БУДЬ-ЯКИЙ СТАН БАЙТА, ПРИ ЦЬОМУ НЕ ЗАЛИШАЄТЬСЯ ЛИШНІХ - НЕ ВИКОРИСТАНИХ В ЗАПИСІ ЦИФР
		                                                                                                            ДЛЯ ПРИКЛАДУ: 'A5E' (де A по факту 10)
		   
		    Представляє собою інформацію у вигляді кода яка записана у символи вибраних з шістнадцяти символів системи числення: 
		        
		        0-9 Арабські цифри: 0 1 2 3 4 5 6 7 8 9 (10цифр включно з нулем)
		        A-F Перші шість літер латинського алфавіту: A B C D E F
		            Букви латинського алфавіту по своїй суті є також наступними цифрами після 9: А-10, B-11, C-12, D-13, E-14, F-15 (0-15)
		        
		        Разом 16 символів: 10 арабських цифр та 6 латинських букв - утворюють 16 цифр системи кодування
		'''
		HEX число можна записати для прикладу також наступним чином:

		0x2AF3 або 2AF3(16) - для компютерних мов програмування зручніше застосовувати саме такий формат з 0x

		0
		1
		2
		3
		4
		5
		6
		7
		8
		9
		A-10
		B-11
		C-12
		D-13
		E-14
		F-15
		Шістнадцяткова система числення

	0x - ідентифікатор шістнадцяткової системи числення





Modules random:

	random() - згенерує довільне число від 0 до 1.

			print(random.random())
			>>> 0.35621508377000977 
			>>> etc

	randint(0, 10) - згенерує довільне число в межах від 0 до 10.
			
			rint(random.random())
			>>>> 7
			>>>> 0





Method	Description

	seed()	Initialize the random number generator
	getstate()	Returns the current internal state of the random number generator
	setstate()	Restores the internal state of the random number generator
	getrandbits()	Returns a number representing the random bits
	randrange()	Returns a random number between the given range
	randint()	Returns a random number between the given range
	choice()	Returns a random element from the given sequence
	choices()	Returns a list with a random selection from the given sequence
	shuffle()	Takes a sequence and returns the sequence in a random order
	sample()	Returns a given sample of a sequence
	random()	Returns a random float number between 0 and 1
	uniform()	Returns a random float number between two given parameters
	triangular()	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
	betavariate()	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
	expovariate()	Returns a random float number based on the Exponential distribution (used in statistics)
	gammavariate()	Returns a random float number based on the Gamma distribution (used in statistics)
	gauss()	Returns a random float number based on the Gaussian distribution (used in probability theories)
	lognormvariate()	Returns a random float number based on a log-normal distribution (used in probability theories)
	normalvariate()	Returns a random float number based on the normal distribution (used in probability theories)
	vonmisesvariate()	Returns a random float number based on the von Mises distribution (used in directional statistics)
	paretovariate()	Returns a random float number based on the Pareto distribution (used in probability theories)
	weibullvariate()	Returns a random float number based on the Weibull distribution (used in statistics)




Json:

sorted() - сортування даних в list of dicts за вказаним значенням key (в парі key/value):

		## в даному вмпадку Bob1 - знаходиться на 2 ому місці                       ######### <---
		data = [{'name': 'Bob2', 'rate': 0.78, 'languages': ['English', 'French']}, {'name': 'Bob1', 'rate': 25, 'languages': ['French']}, {'name': 'Bob3', 'rate': 78, 'languages': ['Germany']}]
		data = sorted(data, key=lambda i: i['name'])
		print(data)

		### list of dicts - відсотрований у правильному порядку Bob1/Bob2/Bob3
		data = [{'name': 'Bob1', 'rate': 25, 'languages': ['French']}, {'name': 'Bob2', 'rate': 0.78, 'languages': ['English', 'French']}, {'name': 'Bob3', 'rate': 78, 'languages': ['Germany']}]
						### --->                                        ### --->                                                              ### --->




FILES:







TESTING:
self.assertIsInstance - https://stackoverflow.com/questions/38874561/asserting-if-a-string-is-a-valid-int








