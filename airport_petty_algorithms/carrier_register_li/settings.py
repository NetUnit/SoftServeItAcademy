import os

class PathFinder():
    '''
        ===========================================================
        This class represents basic roots to media files
        ===========================================================
        Attrs:
            :param cwd: current working directiory
            :param rt_sticker: root to rt sticker fuel selection
            :param jet_sticker: -//- jet a-1 sticker fuel selection
            :param clock_image: -//- clock img when date picker
            :param tank_image: -//-  fuel truck img when date picker

        .. note::
            * params are str type 
    '''

    def __init__(self):
        cwd = os.getcwd()
        self.rt_sticker = os.path.join(
            cwd, 'rt-sticker.jpg'
        )

        self.jet_sticker = os.path.join(
            cwd, 'jet-a-1-sticker.jpg'
        )

        self.clock_image = os.path.join(
            cwd, 'clock.png'
        )

        self.tank_image = os.path.join(
            cwd, 'fuel_track.png'
        )

        self.cwd = cwd

path_finder = PathFinder()
RT_STICKER = path_finder.rt_sticker
JET_STICKER = path_finder.jet_sticker
CLOCK_IMAGE = path_finder.clock_image
TANK_IMAGE = path_finder.tank_image

# *** COLORS *** #
WHITE = (255/255, 255/255, 255/255, 1)
SIGNAL_WHITE = (240/255, 240/255, 240/255, 0)
PURE_WHITE = (240/255, 240/255, 240/255, 1)
TRAFFIC_GREY = (83/255, 83/255, 83/255, 1)
MINT_GREEN = (155/255, 255/255, 152/255, 0.8)
BLACK = (0/255, 0/255, 0/255, 0.7)
ASDA_GREEN = (125/255, 194/255, 66/255, 1)
FOX_RED = (222/255, 44/255, 31/255, 1)
