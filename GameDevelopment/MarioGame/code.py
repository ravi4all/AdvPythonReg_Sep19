import pygame
from pygame.locals import *
from os import path

WIDTH = 1200
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

img_dir = path.join(path.dirname(__file__), 'img')

class Spritesheet(pygame.sprite.Sprite):

    def __init__(self, file_name):
        super().__init__()
        self.spriteSheet = file_name

    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(BLACK)

        return image

class Player(pygame.sprite.Sprite):
    walking_frames = []
    stadingFrame = []
    m = 7
    v = 7
    def __init__(self):
        super().__init__()
        spritesheet = Spritesheet(player_sprite)

        self.image = spritesheet.getImage(80,34,16,16)
        self.stadingFrame.append(self.image)

        self.image = spritesheet.getImage(97,34,14,16)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(115,34,14,16)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(131,34,15,16)
        self.walking_frames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 - 250, HEIGHT / 2 + 185)
        self.pos = 0
        self.moveX = 0
        self.leftWalk = False
        self.rightWalk = False
        self.jump = False
        self.underBlock = False

    def update(self, *args):
        self.pos += 8
        self.image = self.stadingFrame[0]

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.rightWalk = True
        elif keypressed[pygame.K_LEFT]:
            self.leftWalk = True
        elif keypressed[pygame.K_UP]:
            self.jump = True
        else:
            self.rightWalk = False
            self.leftWalk = False

        self.rect.x += self.moveX

        if self.rightWalk:
            frame = (self.pos // 30) % len(self.walking_frames)
            self.image = self.walking_frames[frame]

        elif self.jump:
            f = self.m * self.v
            if self.rect.x + 40 > coins.rect.x and self.rect.x < coins.rect.x + coins.w * 3:
                self.v -= 1
                self.rect.y -= f * 0.6
                hit = pygame.sprite.groupcollide(coinGroup, playerGroup, False, False)
                if self.rect.y < coins.rect.y + coins.h * 3 or hit:
                    self.rect.y = HEIGHT / 2 + 180
                    self.v = 7
                    self.jump = False
            else:
                self.v -= 1
                self.rect.y -= f
                if self.rect.y >= 500:
                    self.rect.y = HEIGHT / 2 + 180
                    self.v = 7
                    self.jump = False

        self.image = pygame.transform.scale(self.image, (50, 53))

class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        spritesheet = Spritesheet(backgroundSprite)
        self.x,self.y,self.w,self.h = 0, 0, 3392, 224
        self.image = spritesheet.getImage(self.x,self.y,self.w,self.h)
        self.rect = self.image.get_rect()
        self.rect.y = -70
        self.moveX = 0

    def update(self, *args):
        self.image = pygame.transform.scale(self.image, (self.w * 3, self.h*3))
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 15
        else:
            self.moveX = 0

        self.rect.x -= self.moveX

class Coins(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        spritesheet = Spritesheet(tileset)
        self.x,self.y,self.w,self.h = 80,112,15,15
        self.image = spritesheet.getImage(self.x,self.y,self.w,self.h)
        self.rect = self.image.get_rect()
        self.rect.x = 255 * 3
        self.rect.y = 136 * 3 - 70
        self.moveX = 0

    def update(self, *args):
        self.image = pygame.transform.scale(self.image, (self.w * 3, self.h * 3))
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 15
        else:
            self.moveX = 0

        self.rect.x -= self.moveX

player_sprite = pygame.image.load('images/mario.png')
backgroundSprite = pygame.image.load("images/world_1.png")
tileset = pygame.image.load("images/coinBlocks_bricks.png")

all_sprites = pygame.sprite.Group()
player = Player()
background = Background()
coins = Coins()

playerGroup = pygame.sprite.Group()
playerGroup.add(player)

coinGroup = pygame.sprite.Group()
coinGroup.add(coins)

all_sprites.add(coins)
all_sprites.add(background)
all_sprites.add(player)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

main()