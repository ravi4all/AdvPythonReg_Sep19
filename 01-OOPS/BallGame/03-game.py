import pygame
import random
import math
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
        self.moveX = 2
        self.moveY = 2
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - 50:
            self.moveX = -2
        elif self.x < 50:
            self.moveX = 2
        elif self.y > height - 50:
            self.moveY = -2
        elif self.y < 50:
            self.moveY = 2

# balls = []
# for i in range(3):
#     ball = Ball()
#     balls.append(ball)

ball_1 = Ball()
ball_2 = Ball()
# ball_2.x = 800
ball_2.y = 200

FPS = 100
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    pygame.draw.circle(screen, ball_1.color, (ball_1.x, ball_1.y), 50)
    ball_1.update()

    pygame.draw.circle(screen, ball_2.color, (ball_2.x, ball_2.y), 50)
    ball_2.update()

    if ball_1.moveX == 2 and ball_2.moveX == -2:
        d = abs((ball_1.x + 50) - (ball_2.x - 50))
        print(d)
        if d == 0:
            ball_1.moveX = -2
            ball_2.moveX =  2
    elif ball_1.moveX == -2 and ball_2.moveX == 2:
        d = abs((ball_1.x - 50) - (ball_2.x + 50))
        print(d)
        if d == 0:
            ball_1.moveX = 2
            ball_2.moveX = -2
    elif ball_1.moveY == -2 and ball_2.moveY == 2:
        d = abs((ball_1.y - 50) - (ball_2.y + 50))
        print(d)
        if d == 0:
            ball_1.moveY = 2
            ball_2.moveY = -2
    elif ball_1.moveY == 2 and ball_2.moveY == -2:
        d = abs((ball_1.y + 50) - (ball_2.y - 50))
        print(d)
        if d == 0:
            ball_1.moveY = -2
            ball_2.moveY = 2

    # if ball_1.x + 50 == ball_2.x + 50 and  ball_1.y + 50 == ball_2.y + 50:
    #     print(ball_1.x,ball_1.y,ball_2.x,ball_2.y)

    # for i in range(len(balls)):
    #     pygame.draw.circle(screen, balls[i].color, (balls[i].x, balls[i].y), 50)
    #     balls[i].update()


    pygame.display.update()
    clock.tick(FPS)