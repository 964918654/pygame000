class Game_Config:
    def __init__(self):
        self.background_image = 'images/back.png'
        self.backwidth = 720
        self.backheight = 720
        self.gametitle = '五子棋'
        self.running = True
        self.GRID_WIDTH = self.backwidth//20
        self.color_metrix = [[None]* 20 for i in range(20)]
        self.grid_x = 0
        self.grid_y = 0
    @property
    def backsize(self):
        return self.backwidth,self.backheight