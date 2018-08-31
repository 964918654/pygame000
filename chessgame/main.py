import pygame
import os
from game_config import Game_Config
import game_func as gf
from chess import Chess
def main():
    #初始化pygame
    pygame.init()
    #初始化mixer
    pygame.mixer.init()
    #创建配置文件对象
    gc = Game_Config()
    #设置屏幕大小和标题
    pygame.display.set_caption(gc.gametitle)
    screen = pygame.display.set_mode(gc.backsize)
    #设置定时器，用于固定时间刷新屏幕，而不是一直不停的刷新，浪费CPU资源
    FPS = 30
    clock = pygame.time.Clock()
    #加载背景图片
    background = pygame.image.load(gc.background_image).convert()
    #创建chess对象
    chess = Chess(screen,gc)
    #主循环
    while gc.running:
        #设置屏幕刷新频率
        clock.tick(FPS)
        #检测事件
        gf.check_event(gc,chess)
        #画出棋盘
        #screen.blit(background,(0,0))
        gf.draw_background(screen,background,gc)
        #添加棋子
        chess.add_coin()
        #判断游戏是否结束
        gf.game_is_over(gc,chess)
        #刷新屏幕
        pygame.display.flip()


if __name__ == '__main__':
    main()