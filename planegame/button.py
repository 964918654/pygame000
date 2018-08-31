import pygame
class Button:
    def __init__(self,screen,gc):
        self.font = pygame.font.SysFont('simsunnsimsun', 50)
        self.start_surface = self.font.render('开始', True, (0, 0, 0), (255, 255, 255))
        self.start_font_rect = self.start_surface.get_rect()
        self.start_font_rect.centerx = screen.get_rect().centerx
        self.start_font_rect.centery = screen.get_rect().centery
        self.screen = screen
        self.gc = gc
    def blitme(self):
        self.screen.blit(self.start_surface, self.start_font_rect)
        pygame.display.flip()