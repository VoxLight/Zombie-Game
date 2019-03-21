import pygame

class Player(pygame.Rect):
    def __init__(self):
        # Position in Space {
        res = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.pos = self.left, self.top = (round(res[0]/2), round(res[1]/2))
        self.size = self.width, self.height = (40, 40)
        self.r = round(self.width/2)
        self.dest = self.center
        # }

        # Physics {
        self.difficulty = 0.4
        self.MAX_SPEED = False
        self.MAX_DIFF = 5
        self.friction = 0.2
        self.speed = [0, 0]
        self.tracing = False
        # }

        super().__init__(self.center, self.size)

    def draw(self, s):
        pygame.draw.ellipse(s, (1, 80, 255), self, self.r)
        if (not (self.dest == None)) and self.tracing:
            pygame.draw.line(s, (255, 255, 255), self.center, self.dest, 3)
            pygame.draw.ellipse(s, (255, 0, 0), pygame.Rect((self.dest[0]-6, self.dest[1]-6), (12, 12)))
            

    def move(self, vel):
        self.x += vel[0]
        self.y += vel[1]

    def check_speed(self, speed):
        for i in range(len(speed)):
            if speed[i] >= self.MAX_DIFF:
                speed[i] = self.MAX_DIFF
            elif speed[i] <= -self.MAX_DIFF:
                speed[i] = -self.MAX_DIFF

    def update(self, dest):
        if not dest == None:
            self.dest = dest
            for i in range(len(self.dest)):
                if self.dest[i] >= self.center[i]:
                    self.speed[i] += self.difficulty
                elif self.dest[i] <= self.center[i]:
                    self.speed[i] -= self.difficulty
                if self.MAX_SPEED:
                    self.check_speed(self.speed)

        for i in range(len(self.speed)):
            if self.speed[i] < 0:
                self.speed[i] += self.friction
            elif self.speed[i] > 0:
                self.speed[i] -= self.friction


        self.move(self.speed)
