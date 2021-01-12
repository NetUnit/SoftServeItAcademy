# codewars task8 - 'Three sticks'- 7kyu KATA


'''
    Red Knight is chasing two pawns. Which pawn will be caught, and where?

    Input / Output
    Input will be two integers:

    N vertical position of Red Knight (0 or 1).
    P horizontal position of two pawns (between 2 and 1000000).
    Output has to be a tuple (python, haskell, Rust, prolog, C#), an array (javascript), an object (java), or a structure (C) with:

    "Black" or "White" - which pawn was caught
    Where it was caught (horizontal position)

    Notes:
        Red Knight will always start at horizontal position 0.
        The black pawn will always be at the bottom (vertical position 1).
        The white pawn will always be at the top (vertical position 0).
        The pawns move first, and they move simultaneously.
        Red Knight moves 2 squares forward and 1 up or down.
        Pawns always move 1 square forward.
        Both pawns will start at the same horizontal position.
'''


# USING LISTS, range() Var2 - RELEWANT WITH CODEWARS
def red_knight(N, P):
    pawn_sequence = [range(P, 2000000+1)]
    # need to double (outpace 2x when the last item in range)
    red_knight = [(range(0, 2000000+1, 4)), (range(2, 2000000+1, 4))]
    red_knight = [(range(0, 2000000+1, 4)), (range(2, 2000000+1, 4))]

    if pawn_sequence[0][P] in red_knight[0] and N == 0:
        return ('White', pawn_sequence[0][P])
    elif pawn_sequence[0][P] in red_knight[1] and N == 0:
        return ('Black', pawn_sequence[0][P])
    elif pawn_sequence[0][P] in red_knight[0] and N == 1:
        return ('Black', pawn_sequence[0][P])
    elif pawn_sequence[0][P] in red_knight[1] and N == 1:
        return ('White', pawn_sequence[0][P])
    else:
        pass


# з котрої саме позиції по осі Y буде рухатися red knight
N = int(input('Type the Red Knight position Y: should be 0 or 1: '))
# старт початку ходу пішки з початку
P = int(input('Type the start of pawns: should be between 0-1000000: '))
print(red_knight(N, P))


# Var2 USING TUPLES - NON RELEWANT WITh CODEWARS - Execution Timed Out (12000 ms)
def red_knight(nums):
    # nums[0] - should be N
    # nums[1] - should be P
    # creation of pawns steps sequence
    # x - longtitude
    # y - altitude

    step = nums[1]
    pawns_arr = []
    for step in range(0, 1000000+1):
        pawns_arr.append([nums[1]+step, nums[1]+step])

    # creation of horse steps sequence
    #nums = (0, x) or (1, x)
    # x - longtitude
    # y - altitude

    knight_arr = []
    for step in range(0, 1000000+1):
        if nums[0] - 1 == -1:
            knight_arr.append([step*4, nums[0]])
            knight_arr.append([2+step*4, nums[0]+1])

        elif nums[0] - 1 == 0:
            knight_arr.append([step*4, nums[0]])
            knight_arr.append([2+step*4, nums[0]-1])
        else:
            return ('N - should take 0, 1')

    zipped = list(zip(pawns_arr, knight_arr))
    for x, y in zipped[:]:
        if x[0] == y[0] and y[1] != 1:
            x.remove(x[0])
            x.insert(0, 'White')
            return tuple(x)
        elif x[0] == y[0] and not y[1] != 1:
            x.remove(x[0])
            x.insert(0, 'Black')
            return tuple(x)
        else:
            pass


nums = tuple(map(int, input('Enter two numbers, through space: ').split()))
print(red_knight(nums))


# Var3 - USING TUPLES - NON RELEWANT WITh CODEWARS - Execution Timed Out (12000 ms)
def red_knight(nums):

    # creation of pawns steps sequence
    # x - longtitude
    # y - altitude

    pawns_arr = list()
    for step in range(0, 1000000+1):
        pawns_arr.append((nums[1]+step, nums[1]+step))

    # print(type(pawns_arr[0]))
    # print(pawns_arr)
    # return pawns_arr

    # creation of horse steps sequence
    #nums = (0, x) or (1, x)
    # x - longtitude
    # y - altitude

    knight_arr = list(tuple())
    #knight_arr = list()
    for step in range(0, 1000000+1):
        if nums[0] - 1 == -1:
            knight_arr.append((step*4, nums[0]))
            knight_arr.append((2+step*4, nums[0]+1))

        elif nums[0] - 1 == 0:
            knight_arr.append((step*4, nums[0]))
            knight_arr.append((2+step*4, nums[0]-1))
        else:
            return ('N - should take 0, 1')

    zipped = list(zip(pawns_arr, knight_arr))
    for x, y in zipped[:]:
        if x[0] == y[0] and y[1] != 1:
            result = 'White'.split() + [int(i)
                                        for i in str(x[0]).split()]  # using LC
            return tuple(result)
        elif x[0] == y[0] and not y[1] != 1:
            result = 'Black'.split() + \
                                   list(
                                       map(int, str(x[0]).split()))  # using map
            return tuple(result)
        else:
            pass

    return zipped


nums = tuple(map(int, input('Enter two numbers, through space: ').split()))
print(red_knight(nums))


# Var4 - NON RELEWANT WITH CODEWARS - Execution Timed Out (12000 ms)
def red_knight(N, P):
    try:
        color = {0: 'White', 1: 'Black'}

        # pawn_sequence_white = (tuple(range(P, 20+1)[P]), colors[N])) або pawn_sequence_white = (tuple(range(P, 20+1)[P]), 0)
        pawn_sequence_white = (tuple(range(P, 2000000+1))[P], 0)
        # місце де буде спіймана, чорна/біла пішка
        pawn_sequence_black = (tuple(range(P, 2000000+1))[P], 1)

        # хід red knight з початку з X - 0, Y = 0 WHTES CELLS ONLY STARTED FROM 0
        red_knight_white_st0 = (tuple(range(0, 2000000+1, 4))[1:], 0)
        # хід red knight з початку з X - 0, Y = 0     BLACK CELLS ONLY STARTED FROM 0
        red_knight_black_st0 = (tuple(range(2, 2000000+1, 4)), 1)

        # хід red knight з початку з X - 0, Y = 1        WHITES CELLS ONLY STARTED FROM 1
        red_knight_white_st1 = (tuple(range(2, 2000000+1, 4)), 0)
        # хід red knight з початку з X - 0, Y = 0    BLACK CELLS ONLY STARTED FROM 1
        red_knight_black_st1 = (tuple(range(0, 2000000+1, 4))[1:], 1)

        if N == 0:
            elements_in_white_0start = list(set.intersection(*map(set, [pawn_sequence_white, red_knight_white_st0]))), list(
                set.intersection(*map(set, [pawn_sequence_white, red_knight_white_st0[0]])))
            elements_in_black_0start = list(set.intersection(*map(set, [pawn_sequence_black, red_knight_black_st0]))), list(
                set.intersection(*map(set, [pawn_sequence_black, red_knight_black_st0[0]])))

            match1 = []
            for x in elements_in_white_0start:
                for y in x:
                    match1.append(y)

            match2 = []
            for x in elements_in_black_0start:
                for y in x:
                    match2.append(y)

            return (color[match1[0]], match1[1]) if len(match1) > len(match2) else (color[match2[0]], match2[1])

        elif N == 1:
            elements_in_white_1start = list(set.intersection(*map(set, [pawn_sequence_white, red_knight_white_st1]))), list(
                set.intersection(*map(set, [pawn_sequence_white, red_knight_white_st1[0]])))
            elements_in_black_1start = list(set.intersection(*map(set, [pawn_sequence_black, red_knight_black_st1]))), list(
                set.intersection(*map(set, [pawn_sequence_black, red_knight_black_st1[0]])))

            match1 = []
            for x in elements_in_white_1start:
                for y in x:
                    match1.append(y)

            match2 = []
            for x in elements_in_black_1start:
                for y in x:
                    match2.append(y)

            return (color[match1[0]], match1[1]) if len(match1) > len(match2) else (color[match2[0]], match2[1])

        else:
            return 'Please select correct positions for the red knight (0, 1), pawns (2-1000000)'

    except:
        return 'Please select correct positions for the red knight (0, 1), pawns (2-1000000)'


print(red_knight(1, 1000000))
