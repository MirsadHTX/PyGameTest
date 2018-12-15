

import pygame, sys

from pygame.locals import *

x = 400
y = 300

pygame.init()

DISPLAYSURF = pygame.display.set_mode((x, y))

#temp_surf = DISPLAYSURF.copy
temp_surf = pygame.Surface.copy
DISPLAYSURF.fill((0,0,0))  # here, you can fill the screen with whatever you want to take the place of what was there before
DISPLAYSURF.blit(temp_surf,(50,100))

pygame.display.set_caption('Hello World!')


while True: # main game loop


    DISPLAYSURF.fill((255, 255, 255))
    
    #pygame.draw.line(DISPLAYSURF, (200,200,200), (x, 0 + 200), (x+20, 60 +200), 4)
    pygame.draw.circle(DISPLAYSURF, (255,0,0), (10, 30), 5, 1)


    temp_surf = DISPLAYSURF.copy
    #DISPLAYSURF.fill((0,0,0))  # here, you can fill the screen with whatever you want to take the place of what was there before
   # DISPLAYSURF.blit(temp_surf,(50,100))
    
    pygame.display.update()


    for event in pygame.event.get():

         if event.type == QUIT:

             pygame.quit()

             sys.exit()
