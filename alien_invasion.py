""" 外星人入侵 """
import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 650))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game()
