
# All Default Things

import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((123,42,34))

pygame.display.update()

# --------------

class Circle:
    def __init__(self, r, color, pos):
        self.radius = r
        self.color = color
        self.position = pos
        self.thickness = 5
        self.surface = screen # -where we are drawing it

    def drawCircle(self, r):
        self.c = pygame.draw.circle(self.surface, self.color, self.position, r, self.thickness) # -drawing a circle in pygame
    
    def increaseC(self, r):
        self.radius += r # -increasing values is +=
        self.c = pygame.draw.circle(self.surface, self.color, self.position, self.radius, self.thickness)

ball = Circle(25, "white", (300,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.drawCircle(10)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            ball.increaseC(10)
            pygame.display.update()