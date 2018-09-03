import pygame

class Chess:
    def __init__(self,screen,gc):
        self.screen = screen
        self.gc = gc
        self.movemoent = []
        self.color = (0,0,0)
    def add_coin(self):
        for m in self.movemoent:
            pygame.draw.circle(self.screen,m[1],m[0],16)
