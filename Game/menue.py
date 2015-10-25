import pygame, random
import time
from Game.objects import*
from Game.main import GameStuff
import prepare

class GameMain:
    def __init__(self):
        self.screenSize = (640, 640)

    def init(self):
        pygame.init()
        self.time_animate = pygame.time.get_ticks()
        self.time_animate2 = pygame.time.get_ticks()
        self.Bg = LabClass()
        self.B = BClass()
        self.Bar = BarClass()
        self.Bg2 = BKClass()
        self.screen = pygame.display.set_mode(self.screenSize)
        music = pygame.mixer.music.load(prepare.MUSIC['musicC'])
        pygame.mixer.music.play(-1,0.0)
        self.Menue = True
        self.Startgame = False
        self.remove = False
        

    def animate(self):
        self.screen.blit(self.Bg.image, self.Bg.rect)
        self.screen.blit(self.Bar.image, self.Bar.rect)
        self.screen.blit(self.Bg2.image, self.Bg2.rect)
        self.screen.blit(self.B.image, self.B.rect)
        pygame.display.flip()

    def run(self):
        while True:
            Start = GameStuff()
            self.animate()
            while self.Menue :
                self.animate()
                x, y = pygame.mouse.get_pos()
                if (x in range(229,391)) and (y in range(470,530)):
                    self.B.image = prepare.GFX["MouseOn"]
                else:
                    self.B.image = prepare.GFX["startbutton"]
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            if ( x in range(229,391)) and (y in range(470,530)):
                                self.B.image = prepare.GFX["push"]
                                pygame.mixer.music.fadeout(1000)
                                self.Menue = False
                                now = pygame.time.get_ticks()
                                self.time_animate = now
                                self.Startgame = True
                        if event.type == pygame.QUIT:
                            pygame.quit()
            while self.Startgame:
                self.animate()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.stop()
                            import Game.end.py
                self.Bg2.B.speed = self.B.turn(2)
                self.Bg2.move(self.Bg2.B.speed)
                now = pygame.time.get_ticks()
                if now-self.time_animate > 1800:
                    self.Startgame = False
                    self.now2 = pygame.time.get_ticks()
                    self.time_animate2 = self.now2
                    self.remove = True
            while self.remove:
                self.animate()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.stop()
                            import Game.end.py
                self.Bar.B.speed = self.B.turn(-2)
                self.B.speed = self.B.turn(-2)
                self.Bar.move(self.Bar.B.speed)
                self.B.move(self.B.speed)
                now = pygame.time.get_ticks()
                if now-self.time_animate2 > 1400:
                    Start.New()
                    
                

    def New(self):
        self.init()
        self.run()

