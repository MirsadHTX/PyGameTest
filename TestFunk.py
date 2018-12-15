import pygame

def startSkerm(breddePaaVinduet,hoejdePaaVinduet,roedBaggrund,groenBaggrund,blaaBaggrund):
    pygame.init()
    minVindue = pygame.display.set_mode((breddePaaVinduet, hoejdePaaVinduet))
    minVindue.fill((roedBaggrund, groenBaggrund, blaaBaggrund))

def opdatererSkerm():

    pygame.display.update()

def makeButton():

    pygame.draw.rect(minVindue,(255,0,0),(20,50,50,100),0)
