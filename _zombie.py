import pygame
import random
from path import Path
from vector import Vector2D
import tools

class Zombie(pygame.Rect):
    def __init__(self):
        # Position in Space{
        res = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.spawn_points = [(0, 0), (res[0], res[1]), (res[0], 0), (0, res[1])]
        self.pos = self.left, self.top = random.choice(self.spawn_points)
        self.size = self.width, self.height = (10, 10)
        self.r = round(self.width/2)
        # }

        # Physics{
        self.vel = [0, 0]
        self.speed = 1
        self.dest = None
        #}

        # Pathing{
        self.path = Path()
        self.current_node = 0
        # }
        super().__init__(self.pos, self.size)

    def pathFollowing(self):
        if self.path.getNodes() != []:
            nodes = self.path.getNodes()
            next_node = nodes[currentNode]
            if tools.distance(self.pos, self.dest) <= 10:
                currentNode += 1
                if currentNode >= len(nodes):
                    currentNode -= 1
        return next_node


    def draw(self, s):
        pygame.draw.ellipse(s, (41, 255, 61), self, self.r)


    def update(self, dest):
        self.dest = dest
            