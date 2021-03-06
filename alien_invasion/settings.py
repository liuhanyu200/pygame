import random


class Settings():
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 0.5
        # 子弹设置
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 0.5
