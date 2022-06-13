def add(*args):
    return sum(args)

def sub(*args):
    first = args[0]
    for i in range(len(args)+1):
        first -= i
    last = first
    return last
