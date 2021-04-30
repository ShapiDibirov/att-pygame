import pygame
import os
import sys

pygame.init()
sc = pygame.display.set_mode((400, 300))

fullname = os.path.join('data', 'sound01.ogg')

pygame.mixer.music.load(fullname)
pygame.mixer.music.play()


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_1:
                pygame.mixer.music.pause()
                # pygame.mixer.music.stop()
            elif i.key == pygame.K_2:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)
            elif i.key == pygame.K_3:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)



    pygame.time.delay(20)
