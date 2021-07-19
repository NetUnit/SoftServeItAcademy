

class Database():

    ''' Add more fields here '''

    db_fields = ['Raspberry Pi', 'Turing Pi'];

    def __init__(self, db_fields=db_fields):
        self.db_fields = db_fields
    
    @staticmethod
    def get_fields(db_fields=db_fields):
        return ' '.join(db_fields)



