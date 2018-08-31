import pygame
from pygame.sprite import Sprite
class Foeship(Sprite):
    def __init__(self,screen,gc):
        super(Foeship,self).__init__()
        self.gc = gc
        #窗口
        self.screen = screen
        #敌机
        self.image = pygame.image.load('images/diji.png')
        #位置矩形
        self.rect = self.image.get_rect()
        self.scr_rect = self.screen.get_rect()
        #定位
        self.rect.centerx = self.scr_rect.centerx
        self.rect.top = self.scr_rect.top
        #速度
        self.speed = gc.foeship_speed
        self.down_speed = gc.foeship_down_speed

    def check_status(self):
        if self.rect.x<0:
            return True
        if self.rect.right>self.scr_rect.width:
            return  True

    def update(self):
        self.rect.x += self.gc.foeship_speed*self.gc.foeship_dir

        pass
    # def fship_fuc_right(self):
    #     if self.right_foe :
    #         self.rect.x += self.speed
    #         if self.rect.right > self.scr_rect.width:
    #             self.rect.right -= self.scr_rect.width
    #     if self.left_foe :
    #         self.rect.x -= self.speed
    #         if self.rect.x < 0:
    #             self.rect.x = 0
    #     self.screen.blit(self.surface,self.rect)
    # def check_edges(self):
    #     """Return True if alien is at edge of screen."""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.right >= screen_rect.right:
    #         return True
    #     elif self.rect.left <= 0:
    #         return True
    # def fship_fuc_right(self):
    #     # def fship_fuc_left(self):
        #     self.rect.x -= self.speed
        #
        #         return self.rect.x
    # def fship_fuc(self,a):
    #
    #
    #
    #     if self.rect.x<0 :
    #         a = a
    #
    #     if self.rect.right >= self.scr_rect.width:
    #         a = -a
    #     return a
    # def fship_tu(self,a):
    #     self.rect.x += (self.speed * a)
        # if self.rect.right >= self.scr_rect.width:
        #     self.rect.right -= self.speed
        # elif self.rect.x < 0:
        #     self.rect.x += self.speed
            # fship_fuc_left(self)

