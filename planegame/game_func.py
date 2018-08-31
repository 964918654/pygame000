import pygame
import time
from pygame.locals import *
from sys import exit
from bullet import Bullet
from foeship import  Foeship
from pygame.sprite import Group
from ship import Ship
from button import Button
from scoreboard import Scoreboard


def check_event(screen,gc,foeships,ship,bullets,button,ships):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == MOUSEBUTTONDOWN and button.start_font_rect.x <= event.pos[0] <= (
                button.start_font_rect.width + button.start_font_rect.x) and button.start_font_rect.y <= event.pos[
            1] <= (
                button.start_font_rect.height + button.start_font_rect.y):
            check_play_button(screen, gc, foeships, ship, bullets,ships)

        if event.type == pygame.KEYDOWN:
            key_down(event, screen, gc, ship, bullets)
        if event.type == pygame.KEYUP:
            key_up(event, ship)


def key_down(event,screen,gc,ship,bullets):

    if event.key == K_LEFT:
        ship.left = True
    if event.key == K_RIGHT:
        ship.right = True
    if event.key == K_SPACE:
        if len(bullets) < gc.max_bullet:
            b = Bullet(screen,gc,ship)
            bullets.add(b)
def key_up(event,ship):
    if event.key == K_LEFT:
        ship.left = False
    if event.key == K_RIGHT:
        ship.right = False

def mkfoes(screen,gc,foeships,ship):
    foeship = Foeship(screen, gc)
    foeship_width = foeship.rect.width
    screen_width = gc.screen_width
    screen_height = gc.screen_height
    space = screen_width-foeship_width*2
    count_foes = space//(foeship_width*2)
    ship_height = ship.rect.height
    foeship_height = foeship.rect.height
    h_space = screen_height - ship_height *7
    aline_row = h_space//(foeship_height*2)
    for row in range(aline_row):
        for count in range (count_foes):
            foeship = Foeship(screen, gc)
            foeship.rect.x = foeship_width +foeship_width*2*count
            foeship.rect.y = foeship_height+foeship_height*1.3*row
            foeships.add(foeship)
def check_foe(gc,foeships):
    '''检查是否移动到边缘'''
    for foeship in foeships.sprites():
        if foeship.check_status():
            change_foeship_dir(gc,foeships)

            break
def change_foeship_dir(gc,foeships):
    gc.foeship_dir = -gc.foeship_dir
    gc.foeship_downdir += 1
    for foeship in foeships.sprites():
        foeship.rect.y = foeship.rect.y + foeship.down_speed * foeship.gc.foeship_downdir

def check_bullets_foeships(screen,gc,bullets,foeships,ship,scoreboard):
    r = pygame.sprite.groupcollide(bullets, foeships, True, True)

    if r:
        gc.score += 1
        #print(gc.score)
        if not len(foeships):
            mkfoes(screen,gc,foeships,ship)

            gc.foeship_downdir = 0
            gc.foeship_down_speed += 5
def check_ship_foeships(screen,gc,bullets,foeships,ship,ships):
    r = pygame.sprite.spritecollideany(ship,foeships)
    if r :
        game_reset(screen,gc,foeships,bullets,ship,ships)

def check_foeships(screen,gc,foeships,bullets,ship,ships):
    for foeship in foeships.sprites():
        if foeship.rect.bottom >= foeship.scr_rect.bottom:
            game_reset(screen,gc,foeships,bullets,ship,ships)
            break

def game_reset(screen,gc,foeships,bullets,ship,ships):
    gc.ship_life -= 1
    for s in ships:
        s.kill()
        break
    print(len(ships))
    gc.foeship_downdir = 0
    foeships.empty()
    mkfoes(screen,gc,foeships,ship)

    bullets.empty()

    ship.rect.centerx = screen.get_rect().centerx

def show_lifes(screen,gc,ships):
    for life in range(gc.ship_life):
        ship = Ship(screen,gc)

        ship.rect.y = 0
        ship.rect.x = ship.rect.width*life

        ships.add(ship)
def set_screen(screen,gc,ship,foeships,scoreboard,bullets,button,ships):
    #填充背景
    screen.fill(gc.bg_color)
    #画飞机
    ship.blitme()
    #画敌机
    foeships.draw(screen)
    # 渲染生命
    ships.draw(screen)
    #积分板
    scoreboard.blitme()
    #子弹
    bullets.update()
    #按钮
    if not gc.game_active:
        button.blitme()
    #刷新界面
    pygame.display.flip()
def check_play_button(screen,gc,foeships,ship,bullets,ships):
    if not gc.game_active:
        pygame.mouse.set_visible(False)  # 隐藏鼠标

        gc.game_active = True

        foeships.empty()
        bullets.empty()
        ships.empty()
        mkfoes(screen, gc, foeships, ship)
        show_lifes(screen, gc, ships)

