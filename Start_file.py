x = 300
y = 55
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
import sys
import pygame
import time
import prepare
from Game.menue import GameMain

class StartUp:
    def __init__(self):
        self.screenSize = (640, 640)
        self.waite = 2600

    def showStartScreen(self):
        self.screen = pygame.display.set_mode(self.screenSize)

    def run(self):
        while True:
            Play = GameMain()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.time.delay(self.waite)
            Play.New()
            
    def init(self):
        pygame.init()
        pygame.display.set_caption("The Challenge!")
        startmusic = prepare.SFX['musicS']
        startmusic.play()

    def New(self):
        self.init()
        self.showStartScreen()
        self.run()

setUp = StartUp()

setUp.New()
            
            
        

