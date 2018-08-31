import pygame
from pygame.locals import *
from sys import exit
import time
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,screen,gc,ship):
        super().__init__()
        self.screen = screen#窗口对象
        self.scr_rect = screen.get_rect()#窗口矩形对象
        #创建子弹得矩形Rect()对象
        #Rect(left,top,width,height)->Rect
        self.rect = Rect(0,0,gc.bullet_width,gc.bullet_height)
        #获取飞船位置
        self.ship_loca = ship.rect
        self.gc = gc
        #获取子弹得速度
        self.buttle_speed = gc.bullet_speed
        #设置子弹得位置与飞船重合
        self.rect.centerx = self.ship_loca.centerx
        self.rect.centery = self.ship_loca.centery

    def update(self):

        if self.rect.y < 0:
            self.kill()

        self.rect.y -= self.buttle_speed
        self.screen.fill((255,80,0),self.rect)
