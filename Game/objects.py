import pygame
import prepare


class BClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = prepare.GFX["startbutton"]
        self.rect = self.image.get_rect()
        self.rect.center = [310, 500]
        self.speed = [0, 13]
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -1: self.angle = -1
        if self.angle >  1: self.angle =  1
        center = self.rect.center
        self.image = prepare.GFX["startbutton"]
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 70 - abs(self.angle) * 2]
        return speed 

    def move(self, speed):
        self.rect.centery = self.rect.centery + self.speed[0]
        if self.rect.centery < -49:
            self.rect.centery = -53
        if self.rect.centery > 499:
            self.rect.centery = 500

class BKClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = prepare.GFX["Start"]
        self.rect = self.image.get_rect()
        self.rect.center = [320,320]
        self.B = BClass()
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -1: self.angle = -1
        if self.angle >  1: self.angle =  1
        center = self.rect.center
        self.image = prrpare.GFX["startbutton"]
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 70 - abs(self.angle) * 2]
        return speed 

    def move(self, speed):
        self.rect.centerx = self.rect.centerx + self.B.speed[0]
        if self.rect.centerx < 320: self.rect.centerx = 320
        if self.rect.centerx > 935:
            self.rect.centerx = 935

class BarClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = prepare.GFX["Bar"]
        self.rect = self.image.get_rect()
        self.rect.center = [320, 500]
        self.B = BClass()
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -1: self.angle = -1
        if self.angle >  1: self.angle =  1
        center = self.rect.center
        self.image = prepare.GFX["startbutton"]
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 70 - abs(self.angle) * 2]
        return speed 

    def move(self, speed):
        self.rect.centery = self.rect.centery + self.B.speed[0]
        if self.rect.centery < -49: self.rect.centery = -53
        if self.rect.centery > 499:
            self.rect.centery = 500
		
class LabClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = prepare.GFX["lab"]
        self.rect = self.image.get_rect()
    
class GUI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = prepare.GFX["test"]
        self.rect = self.image.get_rect()

class keyClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = prepare.GFX["clear"]
        self.rect = self.image.get_rect()
        self.rect.center = [550,450]

class OK_BClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = prepare.GFX["clear"]
        self.rect = self.image.get_rect()
        self.rect.center = [320,320]






