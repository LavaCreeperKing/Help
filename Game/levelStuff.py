import pygame
import prepare

class LevelClass:
    def __init__(self):
        self.levelsound = prepare.SFX['levelUp']
        self.level = 1
        self.correct = 0
        self.key1 = False
        self.key2 = False
        self.KA = False
        self.KE = False
        
    def get_level(self):
        if self.correct == 20:
            self.level =self.level + 1
            self.levelsound.play()
            self.correct = 0

    def add(self):
        self.correct = self.correct + 1
        
        
        

         
        
        

    
