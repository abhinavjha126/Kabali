import random
import sys
import pygame
from pygame.locals import *

FPS=32
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=SCREENHEIGHT*0.8
GAME_SPRITES={}
GAME_SOUND={}
PLAYER="/Users/saurabh/Downloads/GAME/Player.png"
BACKGROUND="/Users/saurabh/Downloads/GAME/Background.png"
PIPE="/Users/saurabh/Downloads/GAME/Pipe.png"

def welcome_screen():
    """
    DISPLAYS WELCOME SCREEN
    """
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENHEIGHT-GAME_SPRITES["player"].get_height())
    messagex=int(SCREENWIDTH-GAME_SPRITES["message"].get_width())
    messagey=int(SCREENHEIGHT*0.13)
    basex=0
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.type==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and(event.type==K_ESCAPE or event.type==K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES["background"],(0,0))
                SCREEN.blit(GAME_SPRITES["player"],(playerx,playery))
                SCREEN.blit(GAME_SPRITES["message"],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES["base"],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    #THIS IS THE MAIN POINT FROM WHERE THE PROGRAM WILL START
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird By Abhinav")
    GAME_SPRITES["numbers"]=(
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/0.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/1.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/2.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/3.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/4.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/5.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/6.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/7.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/8.png").convert_alpha(),
        pygame.image.load("/Users/saurabh/Downloads/GAME/SPRITES/9.png").convert_alpha()
    )

    GAME_SPRITES["message"] =pygame.image.load("/Users/saurabh/Downloads/GAME/Message.png").convert_alpha(),
    GAME_SPRITES["base"] =pygame.image.load("/Users/saurabh/Downloads/GAME/Base.png").convert_alpha(),
    GAME_SPRITES["pipe"] =(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
        pygame.image.load(PIPE).convert_alpha()
    )


    GAME_SOUND["die"]=pygame.mixer.Sound("/Users/saurabh/Downloads/GAME/SOUNDS/die.mp3")
    GAME_SOUND["hit"]=pygame.mixer.Sound("/Users/saurabh/Downloads/GAME/SOUNDS/hit.mp3")
    GAME_SOUND["point"]=pygame.mixer.Sound("/Users/saurabh/Downloads/GAME/SOUNDS/point.mp3")
    GAME_SOUND["swoosh"]=pygame.mixer.Sound("/Users/saurabh/Downloads/GAME/SOUNDS/swoosh.mp3")
    GAME_SOUND["wing"]=pygame.mixer.Sound("/Users/saurabh/Downloads/GAME/SOUNDS/wing.mp3")

    GAME_SPRITES["background"] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES["player"] = pygame.image.load(PLAYER).convert_alpha()