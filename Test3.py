import pygame
import pytmx
import os
import sys

global position
pygame.init()
pygame.display.set_caption('Game')
perem = width, height = (672, 608)
screen = pygame.display.set_mode(perem)
map1 = pytmx.load_pygame('maps/map1.tmx')
map2 = pytmx.load_pygame('maps/map2.tmx')
all_sprites = pygame.sprite.Group()
num = 0


def get_position():
    pass


def render1():
    width = map1.width
    height = map1.height
    tile_size = map1.tilewidth
    for y in range(height):
        for x in range(width):
            image = map1.get_tile_image(x, y, 0)
            screen.blit(image, (x * tile_size, y * tile_size))


def render2():
    width = map2.width
    height = map2.height
    tile_size = map2.tilewidth
    for y in range(height):
        for x in range(width):
            image = map2.get_tile_image(x, y, 0)
            screen.blit(image, (x * tile_size, y * tile_size))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


speed = 5
widthhero = 40
heighthero = 60
run = True
hero_image = load_image('idle1.png')
hero = pygame.sprite.Sprite(all_sprites)
hero.image = hero_image
hero.rect = hero.image.get_rect()
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.rect.left -= speed
    if keys[pygame.K_RIGHT]:
        hero.rect.left += speed
    if keys[pygame.K_UP]:
        hero.rect.top -= speed
    if keys[pygame.K_DOWN]:
        hero.rect.top += speed
    if num == 0:
        render1()
        all_sprites.draw(screen)
        pygame.display.flip()
    else:
        render2()
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()
