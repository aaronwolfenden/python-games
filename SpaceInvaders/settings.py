class Settings():
    """ Stores all game related settings """

    def __init__(self):
        """ Initialises game settings """
        # Screen Settings
        self.screen_width = 500 #1920
        self.screen_height = 500 #1080
        self.bg_colour = 230, 230, 230

        # Ship Settings
        self.ship_speed_factor = 1.5
