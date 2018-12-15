

import pygame, sys, time
import pygame.locals

#from pygame.locals import *

xVindueBrede = 1200
yVindueHoejde = 600

pygame.init()

minVindue = pygame.display.set_mode((xVindueBrede, yVindueHoejde))




x = 0



minVindue.fill((0, 255, 0))





while True: # main game loop

    
    y = -0.001 * x * x + 500 #funktion f(x)

    
    
    y = int(yVindueHoejde - y) #Lav om på y koordinat

    pygame.draw.circle(minVindue, (255,0,0), (x, y), 1, 0)
    x = x + 1
    pygame.display.update()
    time.sleep(0.02)





    

############# Kun til at afslute PyGame ##################
    for event in pygame.event.get():

         if event.type == pygame.locals.QUIT:

             pygame.quit()

             sys.exit()
###########################################################
