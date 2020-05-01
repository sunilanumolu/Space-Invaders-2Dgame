import pygame
import random
from os import path
import time


WIDTH = 480
HEIGHT = 480
FPS = 80

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE_INVADERS")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


from bullet import Bullet
from life import Lifer
from mob import Mob
from player import Player


font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


img_dir = path.join(path.dirname(__file__), "img")
background = pygame.image.load(path.join(img_dir, "space4.jpg")).convert()
background_img = pygame.transform.scale(background, (0, 0))
background_rect = background_img.get_rect()
change_img = pygame.image.load(path.join(img_dir, "ship3.png")).convert()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
lifers = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


c = 0
d = 0
score = 0
T1 = pygame.time.get_ticks()
running = True


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets)
            if event.key == pygame.K_s:
                player.live(all_sprites, lifers)
            if event.key == pygame.K_q:
                running = False

    T2 = pygame.time.get_ticks()
    all_sprites.update()

    if c is 0:
        if T2 - T1 > 2000:
            m = Mob()
            c = 1
            d = 0
            all_sprites.add(m)
            mobs.add(m)
    if d is 0:
        if T2 - T1 > 8000:
            T1 = T2
            c = 0
            m.kill()
    else:
        if T2 - T1 > 13000:
            T1 = T2
            c = 0
            m.kill()
    fits = pygame.sprite.groupcollide(mobs, lifers, False, True)
    for fit in fits:
        d = 1
        fit.image = pygame.transform.scale(change_img, (60, 60))
        fit.image.set_colorkey(BLACK)
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 10
        T1 = T2
        c = 0
    pp = player
    m = mobs
    h = pygame.sprite.spritecollide(pp, m, False, pygame.sprite.collide_circle)
    if h:
        running = False
    screen.fill(GREEN)
    screen.blit(background_img, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 20, 240, 5)
    draw_text(screen, str((T2 - T1) / 1000), 20, WIDTH - 30, HEIGHT - 80)

    pygame.display.flip()

pygame.quit()


print("Your Score is", score)
