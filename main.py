import sys, pygame
from math import sqrt
pygame.init()

# Consts
size = width, height = 1366, 768
speed = [0, 0]
black = 0, 0, 0
alive = True
mouse_is_down = False
difficulty = 1


#clock
clock = pygame.time.Clock()

timer = 0


screen = pygame.display.set_mode(size)

class Zombie(pygame.Rect):
    def __init__(self, bound, size):
        self.left, self.top = bound
        self.width, self.height = size
        super().__init__(bound, size)

zombie = Zombie((100, 100), (100, 100))
destination = zombie.center

def hypo(a, b):
    return round(sqrt(a**2 + b**2), 2)

def distance(xy1, xy2):
    a = abs(xy1[0] - xy2[0])
    b = abs(xy1[1] - xy2[1])
    return hypo(a, b)

while alive:
    if timer >= 5000:
        print(f"Difficulty increased by 1")
        timer = 0
        #difficulty += 1
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            alive = False
            continue
        if event.type == pygame.MOUSEBUTTONDOWN and event.__dict__['button'] == 3:
            mouse_is_down = True
        elif event.type == pygame.MOUSEBUTTONUP and event.__dict__['button'] == 3:
            mouse_is_down = False
 

    if mouse_is_down:
        destination = pygame.mouse.get_pos()
        print(destination)

    ballx, bally = zombie.centerx, zombie.centery
    if not distance((ballx, bally), destination) <= zombie.width:
        if ballx > destination[0]:
            speed[0] = -difficulty*2
        elif ballx < destination[0]:
            speed[0] = difficulty*2
        if bally < destination[1]:
            speed[1] = difficulty
        elif bally > destination[1]:
            speed[1] = -difficulty
    else:
        if not speed == [0, 0]:
            alive = False
            continue
        speed = [0, 0]

    zombie = zombie.move(speed)


    screen.fill(black)
    pygame.draw.line(screen, (255, 255, 255), zombie.center, destination, 5)
    pygame.draw.circle(screen, (255, 0, 0), destination, 5, 5)
    pygame.draw.rect(screen, (40, 255, 61), zombie, 50)
    pygame.display.flip()
    clock.tick(60)
    timer += clock.get_time()