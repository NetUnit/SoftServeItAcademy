class Hosts:
    '''
        Transfer to db this data afterwards
    '''

    _restricted = [
        '78', '80', '168', '176',
        '212', '213', '193', '195'
    ]

    def __init__(self, _restricted=_restricted):
        self. _restricted = _restricted
