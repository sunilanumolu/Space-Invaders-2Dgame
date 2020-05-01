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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (30, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -0.75

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top < 20:
            self.kill()

bullet_img = pygame.image.load(path.join(img_dir, "flame.png")).convert()
