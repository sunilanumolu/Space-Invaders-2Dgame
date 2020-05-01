import pygame
import random
from os import path
import time

WIDTH = 480
HEIGHT = 480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


img_dir = path.join(path.dirname(__file__), "img")


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(enemy_img, (60, 60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 28
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(self.rect.height)
        self.speedx = 2
        self.ayush = 8000

    def update(self):
        if self.rect.right > WIDTH:
            self.speedx = -2
        if self.rect.left < 0:
            self.speedx = 2

enemy_img = pygame.image.load(path.join(img_dir, "ship0.png")).convert()
change_img = pygame.image.load(path.join(img_dir, "ship3.png")).convert()
