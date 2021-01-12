'''
    In this class we get an inquiry to set-up
    self condition sfor growing tulips.

    Based on assessment of typed conditions, 
    the algorithm reckon whether those r good or
    proper/partially good/improper.
'''


# OOP - Task 10 - Create conditions to tulips
class Tulips:

    decent = ['humid', 'warm', 'indoor', '25']
    tolerated = ['hot', 'indoor', 'humid', '30']
    irrelevant = ['dry', 'hot', 'outdoor', '35']

    def __init__(self, decent=decent, tolerated=tolerated, irrelevant=irrelevant):
        self.decent = decent
        self.tolerated = tolerated
        self.irrelevant = irrelevant

    def selection(self, decent=decent, tolerated=tolerated, irrelevant=irrelevant):
        inquiry_lst = list(
            map(str, input('Please select conditions for growing tuplips: ').split()))
        # return inquiry_lst
        # >>> inquiry_lst = ['warm', 'humid', 'indoor', '25']

        common1 = list(set.intersection(*map(set, [decent, inquiry_lst])))
        common2 = list(set.intersection(*map(set, [tolerated, inquiry_lst])))
        common3 = list(set.intersection(*map(set, [irrelevant, inquiry_lst])))

        print(common1, common2, common3)
        try:
            if len(common1) > 3.5:
                return f'These weather conditions are: decent for growing tulips.'

            elif 2.5 < len(common2) < 3.5:
                return f'These weather conditions are: tolerated for growing tulips,\
pay attention to the temeprature though'
            elif 0 < len(common3) < 2.5:
                return f'These weather conditions are: irrelevant, it\'s too hot,\
the air may be excessively dry and plants don\'t need so much of the sun'
            else:
                raise TypeError('Ooops. Bad input')
        except:
            return 'Please provide a relevant information. \n\
Identify weather conditions for tulips'


instance = Tulips()
print(instance.selection())
