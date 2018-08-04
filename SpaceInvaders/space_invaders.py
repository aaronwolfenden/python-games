import sys
import pygame

from SpaceInvaders.settings import Settings
from SpaceInvaders.ship import Ship
import SpaceInvaders.game_functions as gf

def run_game():
    """ Initialises game """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(screen)


    while True:


        screen.fill(ai_settings.bg_colour)
        ship.blitme()

        pygame.display.flip()


run_game()