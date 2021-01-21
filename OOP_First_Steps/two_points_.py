import math


'''
    Formula = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1))** 0.5 


    using zip+lc+formula:
        1) will return zipped list of coords: [x1, y1, z1], [x2, y2, z2] = [(x1, x2), (y1, y2), (z1, z2)] 
            zip object <zip object at 0x7f0353b52280> - 
            to get the data from a zip wrapper we can use: list/tuple/set
        
		2) execution of mathematic calculation (x1-x2)**2 for each argument in zipped list
			through the list comprehension

            (x1 - x2)**2 = [(x1-x2)**2 for x2, x1 in zipped_list]

            Will receive the next data: [a, b, c] (де a = (x1 - x2)**2)

        3) using sum to calculate all the elements: (a + b + c)
            math.sqrt(sum[a, b, c]) де sum(a, b, c) - using sqrt() method from math module and sum()


        The solution is also a numpy module.
        !!! This way demands the next formula np.linalg.norm(p1-p2): 
'''
'''
# using zip+lc+formula
def dist(p1,p2):
    if len(p1) == len(p2):
        
        #1) дія1
        zipped_list = list(zip(p1, p2)) # [x1, y1, z1], [x2, y2, z2] = [(x3 = x2 - x1), (y3 = y2 - y1), (z3 = z2 - z1)]
        return zipped_list
        
        #2) дія2
        calculated_zipped_list = [(a-b)**2 for a, b in zipped_list] # [(x3)**2, (y3)**2, (z3)**2]
        return calculated_zipped_list
        
        #3) дія3
        calculation = math.sqrt(sum(calculated_zipped_list))
        return round(calculation, 3)

    else:
        return -1


p1 = list(map(int, input('Type the coords of the first point, through space: ').split()))
p2 = list(map(int, input('Type the stcoords of the first point, through space: ').split()))

print(dist(p1,p2))
'''


class Distance:

	p1 = list(map(int, input('Type the coords of the first point, through space: ').split()))
	p2 = list(map(int, input('Type the stcoords of the first point, through space: ').split()))


	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def calculation(self, p1, p2):
		zipped_list = list(zip(p1, p2))



p1 = list(map(int, input('Type the coords of the first point, through space: ').split()))
p2 = list(map(int, input('Type the stcoords of the first point, through space: ').split()))

zipped_list = list(zip(p1, p2))
print(zipped_list)


# [(40, 30), (30, 20), (20, 10)]
for a, b in zipped_list:
	a = (a - b)**2
	print(a)
