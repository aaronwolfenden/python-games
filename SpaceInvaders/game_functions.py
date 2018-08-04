import sys

import pygame

from SpaceInvaders.bullet import Bullet


def check_events(si_settings, screen, ship, bullets):
    """ Responses to keypress and mouse events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, si_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, si_settings, screen, ship, bullets):
    """ Respond to key presses """
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(si_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """ Respond to key releases"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """ Update images on the screen and flip to the new screen. """
    # Redraws the screen during each pass through the loop
    screen.fill(ai_settings.bg_colour)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Makes the most recently drawn screen visible
    pygame.display.flip()
