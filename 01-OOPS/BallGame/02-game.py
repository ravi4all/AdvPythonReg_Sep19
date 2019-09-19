import pygame
import random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

class Ball():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.moveX = random.randint(1,3)
        self.moveY = random.randint(1,3)
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - 50:
            self.moveX = -random.randint(1,3)
        elif self.x < 50:
            self.moveX = random.randint(1,3)
        elif self.y > height - 50:
            self.moveY = -random.randint(1,3)
        elif self.y < 50:
            self.moveY = random.randint(1,3)

ballsList = []
for i in range(4):
    ball = Ball()
    ballsList.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    for i in range(len(ballsList)):
        pygame.draw.circle(screen, ballsList[i].color, (ballsList[i].x, ballsList[i].y), 50)
        ballsList[i].update()

    pygame.display.update()