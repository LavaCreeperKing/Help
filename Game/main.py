import pygame
from Game.objects import*
from Game.keys import*
from Game.levelStuff import LevelClass
from Game.choose import Choose
import prepare

class GameStuff:
    def __init__(self):
        self.screenSize = (640, 640)
        self.levelGet = LevelClass()
        self.Level = self.levelGet.level

    def init(self):
        pygame.init()
        self.gamemusic = prepare.SFX['Play']
        self.gamemusic.play(-1)
        self.screen = pygame.display.set_mode(self.screenSize)
        self.font = pygame.font.Font(None, 30)
        self.getKey = Choose()
        self.v = self.getKey.value
        print(self.v)
        self.levelGet = LevelClass()
        self.Level = self.levelGet.level
        self.correct = self.levelGet.correct
        self.level_text = self.font.render("Level: " +str(self.Level), 1, (0, 0, 0))
        self.correct_text = self.font.render("Correct: " +str(self.correct)+"/20", 1, (0, 0, 0))
        self.Bg = LabClass()
        self.Key = keyClass()
        self.time_timeout = pygame.time.get_ticks()
        self.choose = True
        self.KA = False
        self.KE = False
        self.key1 = False
        self.key2 = False
        self.check = False

    def animate(self):
        self.screen.blit(self.Bg.image, self.Bg.rect)
        self.screen.blit(self.Key.image, self.Key.rect)
        self.screen.blit(self.level_text,[10,10])
        self.screen.blit(self.correct_text,[10,30])
        pygame.display.flip()

    def timeout(self):
        self.Level = self.levelGet.level
        self.timenow = pygame.time.get_ticks()
        if self.Level <= 3:
            if self.timenow-self.time_timeout > 2500:
                self.die()

    def die(self):
        self.gamemusic.stop()
        self.Key.image = prepare.GFX["clear"]
        self.Bg.image = prepare.GFX["shock"]
        self.animate()
        time.sleep(1)
        self.Bg.image = prepare.GFX["lab"]
        self.animate()
        time.sleep(0.5)
        import Game.end
        

    def run(self):
        while True:
            self.v = self.getKey.value
            self.level_text = self.font.render("Level: " +str(self.Level), 1, (0, 0, 0))
            self.correct_text = self.font.render("Correct: " +str(self.correct)+"/20", 1, (0, 0, 0))
            self.KAKey = KAClass()
            self.KEKey = KEClass()
            self.animate()
            while self.choose:
                self.getKey.chooseKey()
                if self.getKey.key1 == True:
                    self.choose = False
                    self.now = pygame.time.get_ticks()
                    self.time_timeout = self.now
                    self.key1 = True
                if self.getKey.key2 == True:
                    self.choose = False
                    self.now = pygame.time.get_ticks()
                    self.time_timeout = self.now
                    self.key2 = True
            while self.key1:
                self.Key.image = prepare.GFX["KA"]
                self.animate()
                self.KAKey.run()
                self.timeout()
                if self.KAKey.KA == 1:
                    self.levelGet.add()
                    self.levelGet.get_level()
                    self.Level = self.levelGet.level
                    self.correct = self.levelGet.correct
                    self.Key.image = prepare.GFX["clear"]
                    self.animate()
                    self.getKey.key1 = False
                    self.key1 = False
                    self.choose = True
                elif self.KAKey.KA == 2:
                    self.die()
            while self.key2:
                self.Key.image = prepare.GFX["KE"]
                self.animate()
                self.KEKey.run()
                self.timeout()
                if self.KEKey.KE == 1:
                    self.levelGet.add()
                    self.levelGet.get_level()
                    self.Level = self.levelGet.level
                    self.correct = self.levelGet.correct
                    self.Key.image = prepare.GFX["clear"]
                    self.animate()
                    print("mainlevel =" +str(self.Level))
                    self.getKey.key2 = False
                    self.key2 = False
                    self.choose = True
                elif self.KEKey.KE == 2:
                    self.die()

                
    def New(self):
        self.init()
        self.animate()
        self.run()
                
        
    
        
    
        




