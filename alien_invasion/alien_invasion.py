# coding:utf-8

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:
        screen.fill(ai_settings.bg_color)
        ship.bliteme()
        gf.check_event()
        pygame.display.flip()


run_game()
