import pygame
import os
import sys
import pygame_textinput

from random import choice

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)
# pygame.FULLSCREEN
pygame.display.set_caption('Танки')

clock = pygame.time.Clock()
FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('IMAGE', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    intro_text = ["ТАНКИ",
                  "Добро пожаловать в игру!",
                  "Введите имя игрока"]

    fon = pygame.transform.scale(load_image('fon1.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 45)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


# textinput = pygame_textinput.TextInput()


def load_level(filename):
    filename = "TEXT/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


bricks = [load_image('brick1.png'), load_image('brick2.png'), load_image('brick3.png'),
          load_image('brick4.png'), load_image('brick5.png'), load_image('brick6.png'),
          load_image('brick7.png'), load_image('brick8.png'), load_image('brick9.png')]
brick = choice(bricks)
tile_images = {'wall': brick, 'empty': load_image('empty.png'), 'water': load_image('water.png')}
player_image = load_image('green_tank.png', -1)

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '?':
                Tile('water', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


running = True
while running:
    # textinput.update(pygame.event.get())
    # screen.blit(textinput.get_surface(), (100, 300))
    # pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            terminate()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = False
    start_screen()
    pygame.display.flip()
    clock.tick(FPS)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

    def get_coord(self):
        return (self.x, self.y)

    def move_player(self, x, y):
        self.x += x
        self.y += y
        self.rect = self.image.get_rect().move(tile_width * self.x, tile_height * self.y)


player = None

a = ['?', '.']


def move(st, x, y):
    x1, y1 = player.get_coord()
    for i in range(len(level)):
        level[i] = level[i].replace('@', '.')

    if st.lower() == 'down':
        if level[x1 + x][y1 + y] in a:
            player.move_player(x, y)
    if st.lower() == 'up':
        if level[x1 + x][y1 + y] in a:
            player.move_player(x, y)
    if st.lower() == 'left':
        if level[x1 + x][y1 + y] in a:
            player.move_player(x, y)
    if st.lower() == 'right':
        if level[x1 + x][y1 + y] in a:
            player.move_player(x, y)


level = load_level('map6.txt')
player, level_x, level_y = generate_level(level)
screen.fill((0, 0, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move("down", 0, 1)
            if event.key == pygame.K_UP:
                move("up", 0, -1)
            if event.key == pygame.K_LEFT:
                move("left", -1, 0)
            if event.key == pygame.K_RIGHT:
                move("right", 1, 0)
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
