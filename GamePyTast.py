import pygame


lydObject = pygame.mixer.Sound('lyd.wav')
#pygame.mixer.music.play()
pygame.init()

minVindue = pygame.display.set_mode((200, 500))
minVindue.fill((0, 255, 0))

while True:


    for event in pygame.event.get():

        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT):
            pygame.draw.circle(minVindue, (255, 0, 0), (50, 150), 1, 0)



    pygame.display.update()