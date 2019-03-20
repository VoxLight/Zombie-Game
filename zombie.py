import pygame
import random

class Zombie(pygame.Rect):
    def __init__(self):
        # Position in Space{
        res = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.size = self.width, self.height = (10, 10)
        self.spawn_points = [(0, 0), (res[0]-self.width, res[1]-self.height),
                             (res[0]-self.height, 0), (0, res[1]-self.width)]
        self.pos = self.left, self.top = random.choice(self.spawn_points)
        self.r = round(self.width/2)
        # }

        # Pathing{
        self.difficulty = random.random()*0.1
        self.MAX_SPEED = False
        self.MAX_DIFF = 3
        self.speed = [0, 0]
        self.tracing = False
        # }

    def move(self, vel):
        self.x += vel[0]
        self.y += vel[1]

    def draw(self, s):
        color = (41, 255, 61)
        pygame.draw.ellipse(s, color, self, self.r)
        if (not (self.dest == None)) and self.tracing:
            pygame.draw.line(s, (41, 199, 61), self.center, self.dest, 1)

    def check_speed(self, speed):
        for i in range(len(speed)):
            if speed[i] >= self.MAX_DIFF:
                speed[i] = self.MAX_DIFF
            elif speed[i] <= -self.MAX_DIFF:
                speed[i] = -self.MAX_DIFF

    def update(self, dest):
        self.dest = dest
        for i in range(len(self.dest)):
            if self.dest[i] >= self.center[i]:
                self.speed[i] += self.difficulty
            elif self.dest[i] <= self.center[i]:
                self.speed[i] -= self.difficulty
            if self.MAX_SPEED:
                self.check_speed(self.speed)

        self.move(self.speed)
