# Final Project by Lily King, v0.0

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((2000, 1200))
pygame.display.set_caption("Lucky's unlucky tail")
clock = pygame.time.Clock()

tileScreen = pygame.image.load('img/finalProject/Title_Screen.gif')
# probery have the cards be something seperade and be maybe be random

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(tileScreen,(0,0))
    
    pygame.display.update()
    clock.tick(60)