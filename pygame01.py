import pygame
from pygame.locals import *
from sys import exit
from pygame.sprite import Group,Sprite
#背景图片，鼠标图标
background_image =  'image/816282.jpg'
mouse_image = 'image/1.png'

#初始化pygame，为使用硬件做准备
pygame.init()
#创建窗口
screen = pygame.display.set_mode((800,600),FULLSCREEN,32)
#设置窗口标题
pygame.display.set_caption('this is a window')

#加载并转换图像


font = pygame.font.SysFont('simsunnsimsun',50)
start_surface = font.render('开始',True,(0,0,0),(255,255,255))
start_font_rect = start_surface.get_rect()
start_font_rect.centerx = screen.get_rect().centerx
start_font_rect.centery = screen.get_rect().centery
screen.blit(start_surface,start_font_rect)

# background = pygame.image.load(background_image).convert()
# mouse_cursor = pygame.image.load(mouse_image).convert_alpha()

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and start_font_rect.x <= event.pos[0] <= (start_font_rect.width+start_font_rect.x) and start_font_rect.y <= event.pos[1] <= (start_font_rect.height+start_font_rect.y):
            print(event.type)
            #screen.blit()
            screen.fill((0, 0, 0))
            break
        if event.type == QUIT:    #接收到退出事件后退出程序
            exit()
      #  screen.blit(background,(0,0)) #画上背景图

        # x,y = pygame.mouse.get_pos() #获取鼠标位置
        # #计算光标左上角位置
        # x -= mouse_cursor.get_width()/2
        # y -= mouse_cursor.get_height()/2
        # #画上光标
        # screen.blit(mouse_cursor,(x,y))

        #刷新画面
        pygame.display.update()