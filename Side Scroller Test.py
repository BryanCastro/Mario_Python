#imports
import pygame
import time
import random

#other pygame
pygame.init()

#Window Info
display_width=800
display_height=600
gameDisplay =pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Side-Scroller')

clock=pygame.time.Clock()

#Colors
white=(255,255,255)
test=(30,155,178)

#load textures
mario=pygame.image.load('8_Bit_Mario.png')
floor_brick=pygame.image.load('brick.png')

#other variables
origin=0

#definitions
def character(x,y):
    gameDisplay.blit(mario, (x,y))

def brick():

    floor_X=origin
    floor_Y=display_height-50
    
    for x in range(1,17):
        gameDisplay.blit(floor_brick, (floor_X,floor_Y))
        floor_X+=50

def game_loop():

    #variables
    mario_startX = (display_width * 0.45)
    mario_floor_level = display_height-100
    mario_startY = mario_floor_level
    x_change=0
    y_change=0
    
    #game run bool
    gameExit=False

    #game loop
    while not gameExit:

        #input checking
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    x_change= 5
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_a:
                    if mario_startY>display_height:
                        y_change=5
                    elif mario_startY<mario_floor_level-100:
                    y_change= 0
                    
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                if event.key==pygame.K_a:
                    if mario_startY<mario_floor_level:
                        y_change=-5

        if mario_startY<mario_floor_level-100:
            y_change=0
        if mario_startY>mario_floor_level+1:
            y_change=0
            mario_startY=mario_floor_level
        print('mario_startX: ' + str(mario_startX))
        print('mario_startY: ' + str(mario_startY))
        print('Y_change: ' + str(y_change))

        mario_startX+=x_change
        mario_startY-=y_change
        
        #mario_startY=floor_level
            
        #fill, draw and display
        gameDisplay.fill(test)
        brick()
        character(mario_startX,mario_startY)
        pygame.display.update()
        clock.tick(60)
                
game_loop()
pygame.quit()
quit()
