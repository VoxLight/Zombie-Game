import random
from math import sqrt
import pygame
pygame.init()

size = screenw, screenh = 1366, 768
screen = pygame.display.set_mode(size)

pos1 = (random.randint(0, screenw), random.randint(0, screenh))
pos2 = (random.randint(0, screenw), random.randint(0, screenh))


def hypo(a, b):
    return round(sqrt(a**2 + b**2), 2)

def distance(xy1, xy2):
    a = abs(xy1[0] - xy2[0])
    b = abs(xy1[1] - xy2[1])
    return hypo(a, b)

print(__name__)
if __name__ == "__main__":

    

    while not (pygame.QUIT in [e.type for e in pygame.event.get()]):
    

        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), pos1, pos2, 2)
        pygame.display.flip()
        
        if pygame.MOUSEBUTTONDOWN in [e.type for e in pygame.event.get()]:
            pos1 = (random.randint(0, screenw), random.randint(0, screenh))
            pos2 = (random.randint(0, screenw), random.randint(0, screenh))
            print(f"The distance of this line is {distance(pos1, pos2)}")


