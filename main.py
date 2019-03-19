import sys, pygame
from math import sqrt
pygame.init()

# Consts
size = width, height = 1366, 768
destination = (0, 0) 
speed = (0, 0)
black = 0, 0, 0
alive = True

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

def hypo(a, b):
    return round(sqrt(a**2 + b**2), 2)

def distance(xy1, xy2):
    a = abs(xy1[0] - xy2[0])
    b = abs(xy1[1] - xy2[1])
    return hypo(a, b)

while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            alive = False
            continue
        if event.type == pygame.MOUSEBUTTONDOWN and event.__dict__['button'] == 3:
            destination = event.__dict__['pos']

    ballx, bally = ballrect.x, ballrect.y
    if not distance((ballx, bally), destination) <= 10:
        if ballrect.x > destination[0] and ballrect.y > destination[1]:
            speed = (-2, -2)

    ballrect = ballrect.move(speed)


    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()