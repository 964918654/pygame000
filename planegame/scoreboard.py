import pygame

class Scoreboard:
    def __init__(self,screen,gc):
        super(Scoreboard,self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.gc = gc
        self.score_str = str(gc.score)
        self.text_color = (20,20,30)
        self.font = pygame.font.SysFont(None,48)
        self.font_surface = self.font.render(self.score_str,True,(0,255,0),None)
        self.rect = self.font_surface.get_rect()
        self.rect.right = screen.get_rect().width
        self.rect.y = 0
    #def prep_score(self):

    def blitme(self):
        # print(self.score_str,self.gc.score,self.font_surface)
        self.screen.blit(self.font_surface,self.rect)
        pygame.display.flip()