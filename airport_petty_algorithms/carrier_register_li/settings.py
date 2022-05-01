import os

class PathFinder():
    '''
        This is settings.py file
    
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