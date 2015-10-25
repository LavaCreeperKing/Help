import pygame
import time
import random
import prepare
import Game


class Choose:
    def __init__(self):
        self.G = Game.main.GameStuff()
        self.level = self.G.Level
        self.value = 'choose'
        self.key1 = False
        self.key2 = False
        self.KA = False
        self.KE = False

    def chooseKey(self):
        self.level = self.G.Level
        if self.level == 1:
            time.sleep(0.5)
            print(self.level)
            type = random.choice(["KA", "KE"])
            if type=="KA":
                self.key1 = True
            if type=="KE":
                self.key2 = True
        elif self.level == 2:
            print("level = 2")
            
        

         
        
        

    
