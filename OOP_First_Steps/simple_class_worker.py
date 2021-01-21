'''
    3 types of data representation,
	depend on format methods
'''


class Name:

	name = 'John'
	lastname = 'Smith'
	balance = 4500

	def __init__(self, name=name, lastname=lastname, balance=balance):
		self.name = name
		self.lastname = lastname
		self.balance = balance

	def balance_for_person(self, name=name, lastname=lastname, balance=balance):
		return 'Місячна зарплата для {0} {1}, складає {2}'.format(self.name, self.lastname, self.balance)

# parametr by default when 
# not being setup here
name_selection = Name('Sam', 'Cooper', 4250)
print(name_selection.balance_for_person())


# var2 - setting paarametres through
# calling the instance
class Name:

	name = 'John'
	lastname = 'Smith'
	balance = 4500

	def __init__(self, name=name, lastname=lastname, balance=balance):
		self.name = name
		self.lastname = lastname
		self.balance = balance

	def balance_for_person(self, name, lastname, balance):
		return 'Місячна зарплата для {0} {1}, складає {2}'.format(name, lastname, balance)

name_selection = Name()
print(name_selection.balance_for_person('Bradley', 'Johnson', 6500))


# var3 - return data
# through % operator
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