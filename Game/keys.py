import pygame
import time

class KAClass:
    def __init__(self):
        self.KA = 0
        self.evt_key = pygame.key.get_pressed()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Game.end.py
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.KA = 1
                elif event.key == pygame.K_ESCAPE:
                    import Game.end.py
                elif self.evt_key is not pygame.K_a or pygame.K_ESCAPE:
                    self.KA = 2

class KEClass:
    def __init__(self):
        self.KE = 0
        self.evt_key = pygame.key.get_pressed()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Game.end.py
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.KE = 1
                elif event.key == pygame.K_ESCAPE:
                    import Game.end.py
                elif self.evt_key is not pygame.K_a or pygame.K_ESCAPE:
                    self.KE = 2
                    

        
        

         
        
        

    
