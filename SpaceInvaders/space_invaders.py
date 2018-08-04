import sys
import pygame

from SpaceInvaders.settings import Settings
from SpaceInvaders.ship import Ship
import SpaceInvaders.game_functions as gf


def run_game():
    """ Initialises game """
    pygame.init()
    si_settings = Settings()
    screen = pygame.display.set_mode((si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(screen, si_settings)


    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(si_settings, screen, ship)

run_game()