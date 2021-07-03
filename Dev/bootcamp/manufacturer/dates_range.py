import datetime

class Dates:
    '''
        Setup date range of manufacturer's foundation here
    '''
    start_date = datetime.date(1850, 1, 1);
    end_date = datetime.date.today();

    def __init__(self, start_date=start_date, end_date=end_date):
        self.start_date = start_date
        self.end_date = end_date

