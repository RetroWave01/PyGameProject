import pygame
import pytmx
import os
import sys

global position
pygame.init()
pygame.display.set_caption('Game')
screen_size = width, height = (672, 608)
screen = pygame.display.set_mode(screen_size)
all_sprites = pygame.sprite.Group()
map1 = pytmx.load_pygame('maps/map1.tmx')
coin = 0
lvl = 1
FPS = 100


def render1():
    width = map1.width
    height = map1.height
    tile_size = map1.tilewidth
    for y1 in range(height):
        for x1 in range(width):
            image = map1.get_tile_image(x1, y1, 0)
            screen.blit(image, (x1 * tile_size, y1 * tile_size))


def render2():
    width = map1.width
    height = map1.height
    tile_size = map1.tilewidth
    for y1 in range(height):
        for x1 in range(width):
            image = map1.get_tile_image(x1, y1, 0)
            screen.blit(image, (x1 * tile_size, y1 * tile_size))


def terminate():
    pygame.quit()
    sys.exit()


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


speed = 32
widthhero = 500
heighthero = 10
run = True
hero_image = load_image('idle1.png')
hero = pygame.sprite.Sprite(all_sprites)
hero.image = hero_image
hero.rect = hero.image.get_rect()
hero.rect.x = 64
hero.rect.y = 64
start_screen()
ci = True
while run:
    pygame.time.delay(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    coordinate = x, y = (hero.rect.x // 32), (hero.rect.y // 32) + 1
    if (x - 1) >= 0 and map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 38 and keys[pygame.K_LEFT] \
            and map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 48 and \
            map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 39:
        hero.rect.left -= speed
    if map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 36 and keys[pygame.K_RIGHT] \
            and map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 40 and \
            map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 49:
        hero.rect.left += speed
    if map1.tiledgidmap[map1.get_tile_gid(x, y - 1, 0)] - 1 != 46 and keys[pygame.K_UP]:
        hero.rect.top -= speed
    if map1.tiledgidmap[map1.get_tile_gid(x, y + 0.5, 0)] - 1 != 28 and keys[pygame.K_DOWN]:
        hero.rect.top += speed
    print(map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1)
    print(coordinate)
    if coin <= 8:
        map1 = pytmx.load_pygame('maps/map1.tmx')
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 53:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 5
            coin = coin + 1
        print(coin)
    elif 8 < coin < 12:
        if ci:
            map1 = pytmx.load_pygame('maps/map2.tmx')
            ci = False
        render2()
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 53:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 5
            coin = coin + 1
        print(coin)
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()
