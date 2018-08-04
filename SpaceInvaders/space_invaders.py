import sys
import pygame

from SpaceInvaders.settings import Settings
from SpaceInvaders.ship import Ship
import SpaceInvaders.game_functions as gf
from pygame.sprite import Group


def run_game():
    """ Initialises game """
    pygame.init()
    si_settings = Settings()
    screen = pygame.display.set_mode((si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(screen, si_settings)
    # Group to store bullets in
    bullets = Group()

    while True:
        gf.check_events(si_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(si_settings, screen, ship, bullets)


run_game()