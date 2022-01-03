
'''
    ===========================================================
    Dictionary comprehensions
    ===========================================================
	
	Dict comprehension should be written in a specific pattern
	:single value iteration pattern: 
		{key: value for key, value in iterbale (value1, value2, value3)}

	:key-value iteration pattern:
	{key: value for key, value in iterbale_pairs [(key, value), (key1, value1) ...]}

	:link: https://www.programiz.com/python-programming/dictionary-comprehension

    .. note:: 
		Pluses of dc:
		- shorten the process of dictionary intialization

		Minuses:
		- may provoke to run the code slower
		- can decrease the readability of the code
    '''

fruits = ['apple', 'banana' , 'cherry']
prices = [50, 60, 40]

dict1 = {k: v for k, v in zip(fruits, prices)}
### >>> {'apple': 50, 'banana': 60, 'cherry': 40}

# filtering with a certain
dict2 = {k: v for k, v in zip(fruits, prices) if k!='apple'}
### >>> {'banana': 60, 'cherry': 40}

dict3 = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# miltiply if conditional statements
filtered = { k: v for k, v in dict3.items() if v % 2 != 0 if v < 50}

# if else conditions
filtered2 = {k: ('old' if v > 40 else 'young')
	for (k, v) in dict3.items()}

### >>> {'jack': 'young', 'michael': 'old', 'guido': 'old', 'john': 'young'}

if __name__ == "__main__":
	print(dict1)
	print(dict2)
	print(filtered)
	print(filtered2)

