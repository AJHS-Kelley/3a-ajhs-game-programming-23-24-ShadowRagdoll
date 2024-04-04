# Final Project by Lily King, v0.0

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Lucky's unlucky tail")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # draw all our elements
    # update everything
    pygame.display.update()