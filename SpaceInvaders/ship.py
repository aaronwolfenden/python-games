import pygame


class Ship():
    """ Contains all information relating to the ship """
    def __init__(self, screen, si_settings):
        """ Initialising the ship """
        self.screen = screen
        self.si_settings = si_settings

        # Load The Ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start Each New Ship At Bottom Of The Screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flag """
        # Update the ship's center value and not the rect
        if self.moving_right:
            self.center += self.si_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.si_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """ Draw the ship at the current location """
        self.screen.blit(self.image, self.rect)