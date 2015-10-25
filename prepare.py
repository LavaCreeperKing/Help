import pygame
import os
import tools

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(300,55)
SCREENSIZE = (640,640)
SCREEN = pygame.display.set_mode(SCREENSIZE)
MUSIC = tools.load_all_music(os.path.join("GAME", "resources", "music"))
SFX   = tools.load_all_sfx(os.path.join("GAME", "resources", "sound"))
GFX   = tools.load_all_gfx(os.path.join("GAME", "resources", "graphics"))
