import pygame
import os
import sys
import pygame_textinput

from random import choice

import field

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# size = WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('Танки')

tank = load_image('green_tank.png')
enemy_tanks = [load_image('yellow_tank.png'), load_image('blue_tank.png'), load_image('grey_tank.png'),
          load_image('pink_tank.png'), load_image('brown_tank.png'), load_image('ppink_tank.png'),
          load_image('purple_tank.png'), load_image('green_blue_tank.png'), load_image('light_blue_tank.png')]
not_player = choice(enemy_tanks)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemy_group, all_sprites)
        self.image = player_image
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

        def get_coord(self):
            return (self.x, self.y)

        def move_player(self, x, y):
            pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
