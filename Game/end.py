import pygame
import time

#I created this file a while back befor I learned about a proper code structer
#but it works so I see no need to convert it at this time.

def animate():
    pygame.display.flip()

Black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode([640,640])
font = pygame.font.Font(None, 50)

while True:
    animate()
    end_text = font.render("Thanks for playing.",0 , (255, 0, 0))
    screen.blit(end_text,[150,320])
    pygame.display.flip()
    

    time.sleep(2)
    pygame.quit()
