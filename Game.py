'''


@author: Grayson
'''

import pygame, sys, os, math
from pygame.locals import *
from random import randint

class Game:
    ############VARIABLS##########
    WINDOWWIDTH = 1024
    WINDOWHIGHT =  768
    GAMENAME = "BomberMan"
    FRAMERATE = 60
    BGCOLOR = (255,255,255)
    playing = False
    
    ##############CONSTRUCTER##########
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(
            (self.WINDOWWIDTH,self.WINDOWHIGHT))
        pygame.display.set_caption(self.GAMENAME)
        
    def main(self):
        ###########GAME LOOP##########
        while self.playing:
            delta = self.clock.tick(self.FRAMERATE)
                    
            ###########EVENT HANDLING###########
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.quit()
    def quit(self):
        pygame.quit()
        sys.exit()
if __name__=="__main__":
    game = Game()
    game.main        