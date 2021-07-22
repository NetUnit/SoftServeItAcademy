import sys
sys.path.append(".")

from db_items import Database
import copy
import re
from functools import reduce


################################# *** RegEx *** ################################# 
def case_insensitive_input(db_fields, user_input, *args, **kwargs):

    '''
        Using RegEx
        :getting the class attrs through __dict__ method
        :getting the class attrs through (getattr() func alternatively)
        :returns list of items but only matched of one word
    '''

    pattern = re.compile(user_input.lower())

    i = 0
    matched_items = []
    for item in db_fields:
        result = any(pattern.findall(db_fields[i].lower()))
        if result:
            matched_items.append(db_fields[i])
        else:
            pass
        i += 1

    return matched_items

## 1 using getattr() function for getting class attrs
# db_fields = Database()
# db_fields = getattr(db_fields, 'db_fields')

## 2 getting the class attrs through __dict__ method
db_fields = dict(Database.__dict__).get('db_fields')

# make a trial and enjoy a search *_*V)
if __name__ == "__main__":
    print(case_insensitive_input(db_fields, input('Search Items..: ')))


################################# *** iteration + lambda *** ################################# 
def case_insensitive_input(user_input, *args, **kwargs):

    '''
        using classmethod
        in case when db_fields parameter is str data
        :returns list of products but matched within all typed words
    '''

    # convert db_field to lowercase and split to a single word
    lowercase_and_list = lambda *args: (
        ' '.join([' '.join(i) for i in args]).lower().split())
    # convert user_input to lowercase and split to a single word
    lowercase_and_split = lambda *args: (
        ' '.join(list(map(str, args))).lower().split())
    # getting database attrs
    obj_db_fields = dict(Database.__dict__).get('db_fields')
    return obj_db_fields
    db_fields = lowercase_and_list(obj_db_fields)
    user_input = lowercase_and_split(user_input)
    
    match = [word for word in user_input if word in db_fields]
    
    matched_items = list()
    
    for item in obj_db_fields:
        for word in match: # match --->  user input
            if word.capitalize() in item:
                matched_items.append(item)

    filtered_lst  = matched_items[:]
    return tuple(
        filter(lambda x: matched_items.remove(x) is None 
        and matched_items.count(x) == 0, filtered_lst)
        )


# make a trial and enjoy a search *_*V)
if __name__ == "__main__":
    print(case_insensitive_input(input('Search Items..: ')))
