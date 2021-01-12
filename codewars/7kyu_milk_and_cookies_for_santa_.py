import re
import datetime
from datetime import date
from datetime import datetime

# codewars task8 - 'Milk and Cookies for Santa'- 7kyu KATA


'''
    It's almost Christmas Eve, so we need to prepare some milk and cookies for Santa!
    Wait... when exactly do we need to do that?

    Time for Milk and Cookies

    Complete the function function that accepts a Date object, 
    and returns true if it's Christmas Eve (December 24th), 
    false otherwise.

    In this function we are using returned by re.search() expression
    <re.Match object> as BOOL Value, when find any result - the function will 
    return True, if not - it'll return False.

    NOT USED ANY DATE MODULE HERE

    !!! for regex it should be always str data format !!!

    in general 4 basic patterns has been put to this function:
        1) tuple format date: (2013, 12, 24)
        2) local version of date and time: Mon Dec 12 17:41:00 2018
        3) local version of date 12/24/18
        4) ISO-8601 format 2020-12-24
'''


# RELEVANT WITH CODEWARS
def time_for_milk_and_cookies(dt):
    # it'll create tupple, convert it to str an slice of excessive things like commas
    # inverted commas, parentheses
    date_ = ''.join((str(dt)).strip('()')).replace(',', '').replace("'", '')

    try:
        # conditiion 1 - standart date
        # 2013, 12, 24
        result1 = re.search(r"(12)\s{0,}(24)", date_)

        # condition 2 - local version of date and time
        # for values like Mon Dec 12 17:41:00 2018
        result2 = re.search(r"(Dec)\s{0,}(12)", date_)

        # condition 3 - local version of date
        # for values like 12/24/18
        result3 = re.search(r"12/24", date_)

        # condition 4, ISO-8601 format type string, should be str
        # '2020-12-24' - YYYY-MM-DD
        result4 = re.search((r'\d{4}-12-24'), str(dt))

        return True if result1 or result2 or result3 or result4 else False
    except:
        return False


dt = tuple(map(str, input(
    'Select the date please in the next format: YYYY-MM-DD: ').split()))
print(time_for_milk_and_cookies(dt))


# RELEVANT WITH CODEWARS #1 the simplest 
def to_isoformat_(dt):
    return True if '12-24' in dt.isoformat() else False


dt = date(2002, 12, 24)
print(to_isoformat_(dt))


# RELEVANT WITH CODEWARS (NOT MINE)
class date:
    def __init__(self, year, month, day):
        self.month = month
        self.day = day


def time_for_milk_and_cookies(dt):
    if dt.month == 12 and dt.day == 24:
        return True
    else:
        return False


dt = date(2002, 24, 12)
print(time_for_milk_and_cookies(dt))


# RELEVANT WITH CODEWARS (NOT MINE)
'''
    this expression is corrrect because even if the 12/24 are placed in a reverse
    order it'll raise the 'ValueError: month must be in 1..12', when month is 24
'''


def time_for_milk_and_cookies(dt):
    dt = str(dt)
    return True if dt.__contains__("12") and dt.__contains__("24") else False


dt = date(2002, 24, 12)
print(time_for_milk_and_cookies(dt))
