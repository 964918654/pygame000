import pygame
from sys import exit
import time
from game_config import Game_Config
from ship import Ship
import game_func as gf
from pygame.sprite import Group
from foeship import  Foeship
from button import Button
from scoreboard import Scoreboard
def main():
    #初始化
    pygame.init()
    #创建配置文件对象
    gc = Game_Config()
    #标题
    pygame.display.set_caption(gc.game_title)
    #设置游戏窗口

    screen = pygame.display.set_mode(gc.screen_size)
    #背景图片
    button = Button(screen, gc)
    #background = pygame.image.load(gc.background_image).convert()
    #创建ship对象
    ship = Ship(screen,gc)
    # foeship = Foeship(screen,gc)
    bullets = Group()
    foeships = Group()
    ships = Group()
    #gf.mkfoes(screen, gc, foeships, ship)
    #gf.show_lifes(screen, gc, ships)

    while True:#创建游戏主循环

        scoreboard = Scoreboard(screen, gc)
        #检查事件
        gf.check_event(screen,gc,foeships,ship,bullets,button,ships)

        if gc.game_active:
            # 飞船动作更新
            ship.ship_func()
            # 发射子弹更新位置
            bullets.update()
            foeships.update()
            gf.check_foe(gc, foeships)
            gf.check_bullets_foeships(screen, gc, bullets, foeships, ship, scoreboard)
            gf.check_foeships(screen,gc,foeships,bullets,ship,ships)
            gf.check_ship_foeships(screen, gc, bullets, foeships, ship, ships)
        gf.set_screen(screen,gc,ship,foeships,scoreboard,bullets,button,ships)
        #如果死了，gameover
        if gc.ship_life < 0:
            font = pygame.font.SysFont(None,50)
            #创建字典得surface
            font_surface = font.render('GAME OVER',True,(0,0,0),(230,230,230))
            #设置字典得矩形
            font_rect = font_surface.get_rect()
            font_rect.centerx = screen.get_rect().centerx
            font_rect.y = 0
            #在屏幕中显示

            gc.game_active = False
            pygame.mouse.set_visible(True)
            screen.blit(font_surface, font_rect)
            #刷新窗口
            pygame.display.flip()
        # 刷新窗口

        #程序暂时休眠
        time.sleep(0.002)

# if __name__ =='__main__':
main()