#方向键移动图片
import pygame
from pygame.locals import *
from sys import exit

background_image = 'image/1.png'
screen = pygame.display.set_mode((900,600),0,32)
background = pygame.image.load(background_image).convert()
screen_rect = screen.get_rect()#获得窗口位置得矩形
background_rect = background.get_rect()
background_rect.centerx = screen_rect.centerx
background_rect.centery = screen_rect.centery


move_x,move_y = 0 , 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_y = 0
            move_x = 0
    background_rect.x += move_x
    background_rect.y += move_y
    if background_rect.x<0:
        background_rect.x = 0
    elif background_rect.y<0:
        background_rect.y = 0
    elif background_rect.right> screen_rect.width:
        background_rect.right = screen_rect.width
    screen.fill((0,0,0))
    screen.blit(background,background_rect)

    pygame.display.update()