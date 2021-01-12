# codewars task8 - Roman Numerals Encoder - 6kyu KATA


'''
   Create a function taking a positive integer as its
   parameter and returning a string containing the 
   Roman Numeral representation of that integer.

   Modern Roman numerals are written by expressing 
   each digit separately starting with the left most
   digit and skipping any digit with a value of zero.
   In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC;

   resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII;
   or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

   !!! NOTIFICATION:
        nothing is given about 400 - it's out of range,
        so that the encoder should return CD, in our case

        online roman decoderhttps://roman-numerals.info/1490

    I didn't use any module here,
    only type 'for' loop
'''


# NON-RELEVANT WITH CODEWARS
def solution(n):
    str_lst = []

    def thousands(solution):
        for i in range(int(n)//1000):
            if int(n)//1000 >= 0 and (int(n)//1000) < 4:
                str_lst.append('M')
                pass
            elif int(n)//1000 == 0:
                return str_lst.append('M')
            else:
                pass

        return str_lst

    thousands(solution)

    def five_hundreds(solution):

        if len(n) >= 4:
            for i in range(int(n[1:])//500):
                if int(n[1:])//500 > 0 and int(n[1:])//500 < 4 and int(n[1]) != 9:
                    str_lst.append('D')
                elif int(n[1:])//500 > 0 and int(n[1]) == 9:
                    str_lst.append('CМ')
                else:
                    pass
        else:
            for i in range(int(n)//500):
                if int(n)//500 > 0 and int(n)//500 < 4 and int(n[0]) != 9:
                    str_lst.append('D')
                elif int(n)//500 > 0 and int(n[0]) == 9:
                    str_lst.append('CМ')
                else:
                    pass

    five_hundreds(solution)

    def hundreds_(solution):

        if len(n) >= 4:
            for i in range((int(n[1:])//100)+1):
                if i in (1, 2, 3) and int(n[1:])//100 <= 3:
                    str_lst.append('C')

                # special condition for 350-500 Values
                elif int(i) == 3 and 350 <= int(n[1:]) < 400:
                    str_lst.append('L')

                # special condition for 400-449 Values including CD
                elif int(i) == 4 and 400 <= int(n[1:]) < 450:
                    str_lst.append('CD')

                # special condition for 450-499 Values and not 90
                elif int(i) == 4 and 450 <= int(n[1:]) < 500 and int(n[2]) != 9:
                    str_lst.append('CD')
                    str_lst.append('L')

                # special condition for 450-499 Values including CD
                elif int(i) == 4 and 450 <= int(n[1:]) < 500:
                    str_lst.append('CD')

                # special condition for 500-899 Values
                elif i in (6, 7, 8) and int(n[1:])//100 > 5 and int(n[1:])//100 != 9:
                    str_lst.append('C')
                else:
                    pass
        else:
            for i in range((int(n)//100)+1):
                if i in (1, 2, 3) and int(n)//100 <= 3:
                    str_lst.append('C')

                # special condition for 350-500 Values
                elif int(i) == 3 and 350 <= int(n) < 400:
                    str_lst.append('L')

                # special condition for 400-449 Values including CD
                elif int(i) == 4 and 400 <= int(n) < 450:
                    str_lst.append('CD')

                # special condition for 450-499 Values and not 90
                elif int(i) == 4 and 450 <= int(n) < 500 and int(n[1]) != 9:
                    str_lst.append('CD')
                    str_lst.append('L')

                # special condition for 450-499 Values including CD
                elif int(i) == 4 and 450 <= int(n) < 500:
                    str_lst.append('CD')

                # special condition for 500-899 Values
                elif i in (6, 7, 8) and int(n)//100 > 5 and int(n)//100 != 9:
                    str_lst.append('C')
                else:
                    pass

    hundreds_(solution)

    def fifties_(solution):
        if len(n) >= 4:
            for i in range(int(n[2:])//50):
                if int(n[2:])//50 > 0 and int(n[1]) != 4 and int(n[2]) != 9:
                    str_lst.append('L')

                elif int(n[2:])//50 > 0 and int(n[2]) == 9:
                    str_lst.append('XC')
                else:
                    pass

        elif len(n) == 3:
            for i in range(int(n[1:])//50):
                if int(n[1:])//50 > 0 and int(n[0]) != 4 and int(n[1]) != 9:
                    str_lst.append('L')
                elif int(n[1:])//50 > 0 and int(n[1]) == 9:
                    str_lst.append('XC')
                else:
                    pass

        elif len(n) == 2:
            for i in range(int(n)//50):
                if int(n)//50 > 0 and int(n[0]) != 9:
                    str_lst.append('L')
                elif int(n)//50 > 0 and int(n[0]) == 9:
                    str_lst.append('XC')
                else:
                    pass

    fifties_(solution)

    def tenths_(solution):

        if len(n) >= 4:
            for i in range((int(n[2:])//10)+1):
                if i in (1, 2, 3) and int(n[2:])//10 < 4:
                    str_lst.append('X')

                elif int(i) == 4 and int(n[2:])//10 < 5:
                    if int(n[2]) != 9:
                        for a in range(((int(n[2:]))-30)//5):
                            if a == 1 and int(n[2]) == 4:
                                str_lst.append('XL')
                            else:
                                pass
                elif i in (6, 7, 8) and int(n[2:])//10 > 5 and int(n[2:])//10 != 9:
                    str_lst.append('X')
                else:
                    pass

        elif len(n) == 3:
            for i in range((int(n[1:])//10)+1):
                if i in (1, 2, 3) and int(n[1:])//10 < 4:
                    str_lst.append('X')

                elif int(i) == 4 and int(n[2:])//10 < 5:
                    if int(n[1]) != 9:
                        for a in range(((int(n[1:]))-30)//5):
                            if a == 1 and int(n[1]) == 4:
                                str_lst.append('XL')
                            else:
                                pass
                elif i in (6, 7, 8) and int(n[1:])//10 > 5 and int(n[1:])//10 != 9:
                    str_lst.append('X')
                else:
                    pass

        elif len(n) == 2:
            for i in range((int(n)//10)+1):
                if i in (1, 2, 3) and int(n)//10 < 4:
                    str_lst.append('X')

                elif int(i) == 4 and int(n)//10 < 5:
                    if int(n) != 9:
                        for a in range(((int(n))-30)//5):
                            if a == 1 and int(n[0]) == 4:
                                str_lst.append('XL')
                            else:
                                pass

                elif i in (6, 7, 8) and int(n)//10 > 5 and int(n)//10 != 9:
                    str_lst.append('X')
                else:
                    pass
        else:
            pass

    tenths_(solution)

    def fifth(solution):
        for i in range(int(n[-1])//5):
            if int(n[-1]) % 5 == 0:
                str_lst.append('V')
            else:
                pass

    fifth(solution)

    def absolute_(solution):
        for i in range(1):
            if int(n[-1]) == 0:
                continue
            elif int(n[-1]) == 1:
                str_lst.append('І')
            elif int(n[-1]) == 2:
                str_lst.append('ІІ')
            elif int(n[-1]) == 3:
                str_lst.append('ІІІ')
            elif int(n[-1]) == 4:
                str_lst.append('ІV')
            elif int(n[-1]) == 6:
                str_lst.append('VІ')
            elif int(n[-1]) == 7:
                str_lst.append('VІІ')
            elif int(n[-1]) == 8:
                str_lst.append('VІІІ')
            elif int(n[-1]) == 9:
                str_lst.append('ІX')
            else:
                pass

    absolute_(solution)

    return ''.join(str_lst)


n = input('Type the text U r going to check: ')
print(solution(n))


# RELEVANT WITH CODEWARS
def solution(n):

    ints = (1000, 900,  500, 400, 100,  90,
            50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD', 'C', 'XC',
            'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(n / ints[i])
        result.append(nums[i] * count)
        n -= ints[i] * count

    # return(ints[i])
    return ''.join(result)


n = int(input('Type the text U r going to check: '))
print(solution(n))
