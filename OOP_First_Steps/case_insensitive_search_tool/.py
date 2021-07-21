import sys
sys.path.append(".")

from items import Database


# alternatively without classmethod entering the class atttributes
# db_fields = dict(Database.__dict__).get('db_fields')

# alternatively using getattr() function
# db_fields = Database()
# db_fields = getattr(db_fields, 'db_fields')


# def case_insensitive_input(db_fields, user_input, *args, **kwargs):
    

    # ''' (['Raspberry Pi', 'Turing Pi'],) args in this case when the list
    #     has been retrieved from the DB
    # '''


#     # convert parameter to lowercase and split to a single word
#     def lowercase_and_split(*args):
#         args = ' '.join(list(map(str, args)))
#         return args.lower().split()


#     # search for word match and return capitalized words of matches
#     # as attrs of the object
#     db_fields = lowercase_and_split(db_fields)
#     user_input = lowercase_and_split(user_input)
    
#     match = [word for word in user_input if word in db_fields]
#     return list(map(lambda word: word.capitalize(), match))


# # print(' '.join(list(map(str, db_fields))).lower().split())


# # # # tests
# if __name__ == "__main__":
#     for searched_field in db_fields:
#         print(case_insensitive_input(searched_field, input('Search Items..: ')))


# using classmethod
db_fields = Database.get_fields()

def case_insensitive_input(db_fields, user_input, *args, **kwargs):

    # convert parameter to lowercase and split to a single word
    def lowercase_and_split(*args):
        
        args = ' '.join(list(map(str, args)))
        return args.lower().split()

    # search for word match and return capitalized words of matches
    # as attrs of the object
    db_fields = lowercase_and_split(db_fields)
    user_input = lowercase_and_split(user_input)
    
    match = [word for word in user_input if word in db_fields]
    return list(map(lambda word: word.capitalize(), match))

# make a trial and enjoy a search *_*V)
if __name__ == "__main__":
    print(case_insensitive_input(db_fields, input('Search Items..: ')))