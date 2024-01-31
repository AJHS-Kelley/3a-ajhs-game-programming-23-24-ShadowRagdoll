import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('img/ultPy/Sky.png')
ground_surface = pygame.image.load('img/ultPy/ground.png')
text_surface = test_font.render('My game', False, 'Green')

snail_surface = pygame.image.load('img/ultPy/Hand.png')
snail_x_pos = 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
   
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.blit(hand_surface,(600,250))

    pygame.display.update()
    clock.tick(60)

