import pygame
from pygame.locals import *
from sys import exit
import time
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,screen,gc):
        super().__init__()
        self.gc = gc
        #载入背景
        self.screen =screen
        #飞机图片
        self.image =pygame.image.load('images/1.png')
        #位置矩形
        self.rect = self.image.get_rect()
        self.scr_rect = screen.get_rect()
        #定位
        self.rect.centerx = self.scr_rect.centerx
        self.rect.bottom = self.scr_rect.bottom
        #定义两个变量
        self.right = False
        self.left = False
        self.speed = gc.ship_speed
    def ship_func(self):
        if self.right :
            self.rect.x += self.speed
            if self.rect.right > self.scr_rect.width:
                self.rect.right = self.scr_rect.width
        if self.left :
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
    def blitme(self):
        self.screen.blit(self.image,self.rect)
