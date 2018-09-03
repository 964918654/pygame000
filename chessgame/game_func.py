import pygame


#事件检测
def check_event(gc,chess):
    for event in pygame.event.get():
       #检测是否关闭窗口
        if event.type == pygame.QUIT:
            gc.running = False
        #当鼠标按下时
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #1.获取鼠标位置
            pos = event.pos
            #2.计算鼠标点击所在网格点的位置
            #print(pos)#打印获取的鼠标坐标
            gc.grid_x = int(round(pos[0]/gc.GRID_WIDTH))
            gc.grid_y = int(round(pos[1]/gc.GRID_WIDTH))
            grid = (gc.grid_x*gc.GRID_WIDTH,gc.grid_y*gc.GRID_WIDTH)
            #print(grid)#打印计算后坐标具体位于棋盘的第N行N列
            #3.添加棋子(在主程序中运行，这里是将坐标和颜色添加到一个列表中)
            chess.movemoent.append((grid,chess.color))
            #获取方形列表中棋子对应位置的颜色
            gc.color_metrix[gc.grid_x][gc.grid_y] = chess.color
            print(gc.color_metrix[gc.grid_x][gc.grid_y])

#画出棋盘
def draw_background(screen,background,gc):
    #加载背景图片
    screen.blit(background, (0, 0))

    #画网格线，棋盘为19行19列的
    #1.画出边框，GRID_WIDTH = backwidth//20
    rect_lines = [((gc.GRID_WIDTH,gc.GRID_WIDTH),(gc.GRID_WIDTH,gc.backheight - gc.GRID_WIDTH)),
                  ((gc.GRID_WIDTH,gc.GRID_WIDTH),(gc.backwidth - gc.GRID_WIDTH,gc.GRID_WIDTH)),
                  ((gc.GRID_WIDTH,gc.backheight - gc.GRID_WIDTH),(gc.backwidth - gc.GRID_WIDTH,gc.backheight - gc.GRID_WIDTH)),
                  ((gc.backwidth - gc.GRID_WIDTH,gc.GRID_WIDTH),(gc.backwidth-gc.GRID_WIDTH,gc.backheight-gc.GRID_WIDTH))]
    #print(rect_lines)
    for line in rect_lines:
        pygame.draw.line(screen,(0,0,0),line[0],line[1],2)
        #print(line[0])
    #2.画出中间的网格线
    for i in range(17):
        #画垂直的网格线
        pygame.draw.line(screen,(0,0,0),(gc.GRID_WIDTH*(2+i),gc.GRID_WIDTH),
                         (gc.GRID_WIDTH*(2+i),gc.backheight - gc.GRID_WIDTH))
        #画水平的网格线
        pygame.draw.line(screen,(0,0,0),(gc.GRID_WIDTH,gc.GRID_WIDTH*(2+i)),
                         (gc.backheight - gc.GRID_WIDTH,gc.GRID_WIDTH*(2+i)))

    #3.画出棋盘中的五个点
    cicle_coord = [
        (gc.GRID_WIDTH*4,gc.GRID_WIDTH*4),
        (gc.backwidth-gc.GRID_WIDTH*4,gc.GRID_WIDTH*4),
        (gc.backwidth-gc.GRID_WIDTH*4,gc.backheight-gc.GRID_WIDTH*4),
        (gc.GRID_WIDTH*4,gc.backheight-gc.GRID_WIDTH*4),
        (gc.GRID_WIDTH*10,gc.GRID_WIDTH*10)
    ]
    for cc in cicle_coord:
        pygame.draw.circle(screen,(0,0,0),cc,5)
#判断游戏结束,五子连珠即为游戏结束
def game_is_over(gc,chess):
    hori = 1 # 水平
    verti = 1 # 垂直
    slash = 1 # '/'方向
    backslash = 1 # '\'方向
    #判断水平方向
    #left
    left = gc.grid_x - 1
    while left>0 and gc.color_metrix[left][gc.grid_y] == chess.color:
        hori += 1
        left -= 1
    #right
    right = gc.grid_x + 1
    while right<20 and gc.color_metrix[right][gc.grid_y] == chess.color:
        hori += 1
        right += 1
    #判断垂直方向
    #up
    up = gc.grid_y - 1
    while up>0 and gc.color_metrix[gc.grid_x][up] == chess.color:
        up -= 1
        verti += 1
    #down
    down = gc.grid_y + 1
    while down<20 and gc.color_metrix[gc.grid_x][down] == chess.color:
        down += 1
        verti += 1
    #判断‘/’方向
    left = gc.grid_x - 1
    up = gc.grid_y -1
    while left>0 and up>0 and gc.color_metrix[left][up] == chess.color:
        left -= 1
        up -= 1
        slash += 1

    right = gc.grid_x + 1
    down = gc.grid_y + 1
    while right<20 and down<20 and gc.color_metrix[right][down] == chess.color:
        right += 1
        down += 1
        slash += 1
    #判断'\'方向
    left = gc.grid_x - 1
    down = gc.grid_y + 1
    while left>0 and down<20 and gc.color_metrix[left][down] == chess.color:
        left -= 1
        down += 1
        backslash += 1

    right = gc.grid_x + 1
    up = gc.grid_y - 1
    while right<20 and up>0 and gc.color_metrix[right][up] == chess.color:
        right += 1
        up -= 1
        backslash += 1

    if max([hori,verti,slash,backslash]) == 5:
        gc.running = False

def move(screen,gc):


