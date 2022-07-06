print(
    'This Code runs everytime when some import is being done'
)

from .arithmetic import *
from .filters import *

'''
    we dont need to access functions inside the arithmetic folder explicitly
    when doing imports

    .. note::
        once imports have been imlemented in __init__.py
        (unpacked inside the functions folder)
        those can be easily accessed inside main.py only just
        by referring to functions folder now

'''