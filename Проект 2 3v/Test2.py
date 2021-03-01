import pygame
import pytmx
import os
import sys

global position
pygame.init()
pygame.display.set_caption('Game')
screen_size = width, height = (672, 608)
screen = pygame.display.set_mode(screen_size)
map1 = pytmx.load_pygame('maps/map1.tmx')
map2 = pytmx.load_pygame('maps/map2.tmx')
all_sprites = pygame.sprite.Group()
num = 0
FPS = 50


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


def terminate():
    pygame.quit()
    sys.exit()


def get_tile_id():
    return map1.tiledgidmap(map1.get_tile_gid(*coordinate, 0))


def is_free():
    return get_tile_id(coordinate)


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


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
hero.rect.x = 6
hero.rect.y = 9
start_screen()
while run:
    pygame.time.delay(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    coordinate = x, y = (hero.rect.x // 32) + 2, (hero.rect.y // 32) + 3
    print(coordinate)
    if keys[pygame.K_LEFT]:
        hero.rect.left -= speed
    if keys[pygame.K_RIGHT]:
        hero.rect.left += speed
    if keys[pygame.K_UP]:
        hero.rect.top -= speed
    if keys[pygame.K_DOWN]:
        hero.rect.top += speed
    print(coordinate)
    if num == 0:
        render1()
        all_sprites.draw(screen)
        pygame.display.flip()
    else:
        render2()
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()
