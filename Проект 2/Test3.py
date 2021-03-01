import pygame
import pytmx
import os
import sys

global position
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("data/Country_Music_Bed_16 (online-audio-converter.com).wav")
sound.play()
pygame.display.set_caption('Game')
screen_size = width, height = (672, 608)
screen = pygame.display.set_mode(screen_size)
all_sprites = pygame.sprite.Group()
map1 = pytmx.load_pygame('maps/map1.tmx')
coin = 0
FPS = 100


def render():
    width1 = map1.width
    height1 = map1.height
    tile_size = map1.tilewidth
    for y1 in range(height1):
        for x1 in range(width1):
            image = map1.get_tile_image(x1, y1, 0)
            screen.blit(image, (x1 * tile_size, y1 * tile_size))


def terminate():
    pygame.quit()
    sys.exit()


def end_screen5():
    intro_text = ["",
                  "Ты зашёл так далеко, но",
                  "к сожалению время закончилось,",
                  "и все уже узнали об этих местах!",
                  "Поищи другие земли, и попробуй снова.",
                  "За всю игру ты собрал:" + " " + str(coin) + " " + "алмазов."]

    fon = pygame.transform.scale(load_image('end.jpg'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 175
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                terminate()
            elif event1.type == pygame.KEYDOWN or \
                    event1.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


def end_screen1():
    intro_text = ["", "",
                  "Как жаль что твой путь закончился,",
                  "даже не начавшись.",
                  "Надеюсь в следующий раз тебе повезёт больше",
                  "За всю игру ты собрал:" + " " + str(coin) + " " + "алмазов."]

    fon = pygame.transform.scale(load_image('end.jpg'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 175
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                terminate()
            elif event1.type == pygame.KEYDOWN or \
                    event1.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


def start_screen():
    intro_text = ["", "",
                  "                      ПРАВИЛА ИГРЫ",
                  "Ты ковбой, который узнал что на неизведанных ранее",
                  "территориях присутствуют несусветные богатства.",
                  "Поспеши их забрать, пока остальные об это не узнали.",
                  "На это у тебя есть 60 секунд.Удачи!"]

    fon = pygame.transform.scale(load_image('start.jpg'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 175
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                terminate()
            elif event1.type == pygame.KEYDOWN or \
                    event1.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


def win_screen():
    intro_text = ["", "",
                  "Так держать! Вы успели собрать все драгоценности",
                  'на этой территории, и уйти незамеченным.',
                  "В общем счёты вы забрали:"
                  + " " + str(coin) + " " + "бриллиантов.",
                  ""]

    fon = pygame.transform.scale(load_image('win.png'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 175
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('grey'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                terminate()
            elif event1.type == pygame.KEYDOWN or \
                    event1.type == pygame.MOUSEBUTTONDOWN:
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
hero_image = load_image('3.png')
hero = pygame.sprite.Sprite(all_sprites)
hero.image = hero_image
hero.rect = hero.image.get_rect()
hero.rect.x = 32
hero.rect.y = 32
start_screen()
two = True
three = True
four = True
five = True
six = True
seven = True
seconds = 0
f1 = pygame.font.Font(None, 25)
start_ticks = pygame.time.get_ticks()
while run:
    pygame.time.delay(FPS)
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    if seconds > 59 and coin < 20:
        run = False
        end_screen1()
    elif seconds > 59 and 19 < coin < 100:
        run = False
        end_screen5()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    coordinate = x, y = (hero.rect.x // 32), (hero.rect.y // 32) + 1
    if (x - 1) >= 0 and map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 38 and keys[pygame.K_LEFT] \
            and map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 48 and \
            map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 39 and \
            map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 29 \
            and map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 47 \
            and map1.tiledgidmap[map1.get_tile_gid(x - 1, y, 0)] - 1 != 44:
        hero.rect.left -= speed
    if (x + 1) < 21 and map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 36 and keys[pygame.K_RIGHT] \
            and map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 40 and \
            map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 49 \
            and map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 27 \
            and map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 45 \
            and map1.tiledgidmap[map1.get_tile_gid(x + 1, y, 0)] - 1 != 44:
        hero.rect.left += speed
    if (y - 1) > 0 and map1.tiledgidmap[map1.get_tile_gid(x, y - 1, 0)] - 1 != 46 and keys[pygame.K_UP] \
            and map1.tiledgidmap[map1.get_tile_gid(x, y - 1, 0)] - 1 != 45 \
            and map1.tiledgidmap[map1.get_tile_gid(x, y - 1, 0)] - 1 != 47 \
            and map1.tiledgidmap[map1.get_tile_gid(x, y - 1, 0)] - 1 != 44:
        hero.rect.top -= speed
    if (y + 1) < 19 and map1.tiledgidmap[map1.get_tile_gid(x, y + 1, 0)] - 1 != 28 and keys[pygame.K_DOWN] \
            and map1.tiledgidmap[map1.get_tile_gid(x, y + 1, 0)] - 1 != 27 and \
            map1.tiledgidmap[map1.get_tile_gid(x, y + 1, 0)] - 1 != 29 \
            and map1.tiledgidmap[map1.get_tile_gid(x, y + 1, 0)] - 1 != 44:
        hero.rect.top += speed
    print(map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1)
    print(coordinate)
    if coin < 5:
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 53 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 89 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 80:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 5
            coin += 1
    if 4 < coin < 12:
        if two:
            map1 = pytmx.load_pygame('maps/map2.tmx')
            two = False
            sound.stop()
            sound.play()
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 53 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 89 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 80:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 7
            coin += 1
    if 11 < coin < 20:
        if three:
            map1 = pytmx.load_pygame('maps/map3.tmx')
            three = False
            sound.stop()
            sound.play()
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 107 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 89 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 80:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 1
            coin += 1
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 125:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 9
            coin += 1
    if 19 < coin < 40:
        if four:
            hero.rect.x = 320
            hero.rect.y = 320
            map1 = pytmx.load_pygame('maps/map4.tmx')
            four = False
            sound.stop()
            sound.play()
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 89 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 116 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 134 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 80:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 5
            coin += 1
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 71:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 33
            coin += 1
    if 39 < coin < 100:
        if five:
            map1 = pytmx.load_pygame('maps/map5.tmx')
            hero.rect.x = 320
            hero.rect.y = 300
            five = False
            sound.stop()
            sound.play()
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 8 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 107 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 197 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 188 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 26 or \
                map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 53:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 5
            coin += 1
        if map1.tiledgidmap[map1.get_tile_gid(*coordinate, 0)] - 1 == 17:
            map1.layers[0].data[coordinate[1]][coordinate[0]] = 1
            coin += 1
    if 99 < coin:
        win_screen()
        run = False

    render()

    text1 = f1.render('Прошло:' + ' ' + str(seconds), True,
                      (0, 0, 0))
    screen.blit(text1, (290, 295))
    print(coin)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
