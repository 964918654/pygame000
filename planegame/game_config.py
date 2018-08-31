class Game_Config:
    def __init__(self):
        self.game_title = '飞机大战'
        self.background_image = 'images/images/bgimg.jpg'
        self.screen_width = 800
        self.screen_height = 900
        self.ship_speed = 10
        self.bg_color = (230,230,230)
        self.bullet_width = 8
        self.bullet_height = 8
        self.bullet_speed = 10
        self.max_bullet = 10
        self.foeship_speed = 2
        self.foeship_dir = 1
        self.foeship_down_speed = 20
        self.foeship_downdir = 0
        self.ship_life = 3
        self.score = 0
        self.game_active = False
    @property
    def screen_size(self):
        return self.screen_width , self.screen_height