#Imports
import pygame, sys
from pygame.locals import *
import random, time
#Initialzing
pygame.init()
#Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()
#Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")
#Create a white screen
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
class Enemy(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
def move(self):
    global SCORE
    self.rect.move_ip(0,SPEED)
    if (self.rect.top > 600):
        SCORE += 1
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
class Player(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
def move(self):
    pressed_keys = pygame.key.get_pressed()
    if self.rect.left > 0:
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
    if self.rect.right < SCREEN_WIDTH:        
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
class Coin(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
def move(self):
    global COINS_COLLECTED
    self.rect.move_ip(0, SPEED)
    if (self.rect.top > 600):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
class Text(pygame.sprite.Sprite):
    def init(self, text, x, y, font, size, color):
        super().init()
        self.font = pygame.font.SysFont(font, size)
        self.color = color
        self.text = text
        self.image = self.font.render(str(text), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Setting up Sprites
P1 = Player()
E1 = Enemy()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
for i in range(10):
    coin = Coin()
    coins.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)