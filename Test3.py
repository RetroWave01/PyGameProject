import pygame
import pytmx

pygame.init()
pygame.display.set_caption('Game')
perem = width, height = (672, 608)
screen = pygame.display.set_mode(perem)
surf = pygame.Surface(perem)
map = pytmx.load_pygame('maps/map1.tmx')


def render():
    width = map.width
    height = map.height
    tile_size = map.tilewidth
    for y in range(height):
        for x in range(width):
            image = map.get_tile_image(x, y, 0)
            surf.blit(image, x * tile_size, y * tile_size)


speed = 10
x = 9
y = 9
widthhero = 40
heighthero = 60
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 10:
        x -= speed
    if keys[pygame.K_RIGHT] and x < width - widthhero - 10:
        x += speed
    if keys[pygame.K_UP] and y > 10:
        y -= speed
    if keys[pygame.K_DOWN] and y < height - heighthero - 10:
        y += speed
    screen.fill('Black')
    render()
    pygame.draw.rect(screen, (0, 255, 255), (x, y, widthhero, heighthero))
    pygame.display.update()
pygame.quit()
