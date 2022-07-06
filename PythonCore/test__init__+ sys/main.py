# from functions.arithmetic import add, sub
import sys
import os


from functions import (
    add,
    sub,
    filtered_items
)

'''
    with an __init__.py file 
    imported functions from functions dir
    will be considered as python packages

    from python3.3 version __init__.py
    
    ** sys - The sys module in Python provides various
    functions and variables that are used to manipulate
    different parts of the Python runtime environment. 
    Allows operating on the interpreter as it provides access
    to the variables and functions that interact strongly with
    the interpreter

    sys.path are installation-dependent
    :returns: current paths to installed python packages

    sys.argv is a list in Python that contains all the command-line
    arguments passed to the script
    :returns: current path to main file included

    sys.path.append('/usr/lib/python3.9')
    Additional option: we can put the module file in any directory of
    our choice and then modify sys.path at run-time so that it contains
    that directory. For example, in this case, adding other working packages

'''

a = 10

if __name__ == "__main__":
    print(add(1, 2, 3, 4))
    print(sub(1, 2, 3, 4))

    sequence1 = ['warm', 'humid', 'indoor', '25']
    sequence2  = ['hot', 'humid', 'outdoor', '25']

    print(filtered_items(sequence1, sequence2))

    # *** sys methods ***
    print(sys.argv)
    print(sys.path)


