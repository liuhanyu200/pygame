import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.image = pygame.image.load('./images/ship.png')
        self.rect = self.image.get_rect()
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def bliteme(self):
        self.screen.blit(self.image, self.rect)
