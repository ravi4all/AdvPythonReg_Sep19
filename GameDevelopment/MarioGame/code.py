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
    def __init__(self):
        super().__init__()
        # standing - 79,33,17,17
        spritesheet = Spritesheet(player_sprite)
        self.image = spritesheet.getImage(97,34,15,17)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(115,33,14,17)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(131,33,17,17)
        self.walking_frames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 - 250, HEIGHT / 2 + 70)
        self.pos = 0
        self.moveX = 0
        self.walkingFramesActive = True

    def update(self, *args):
        self.pos += 1

        frame = (self.pos // 30) % len(self.walking_frames)
        self.image = self.walking_frames[frame]

        self.rect.x += self.moveX


player_sprite = pygame.image.load('images/mario.png')

all_sprites = pygame.sprite.Group()
player = Player()
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