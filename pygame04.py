#按f全屏
import pygame
from sys import exit
from pygame.locals import *

pygame.init()

background_image = 'image/816282.jpg'

screen = pygame.display.set_mode((960,720),0,32)
background = pygame.image.load(background_image).convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((960,720),FULLSCREEN,32)
                else:
                    screen = pygame.display.set_mode((960,720),0,32)

    screen.blit(background,(0,0))
    pygame.display.update()
