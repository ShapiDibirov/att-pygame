import pygame
import os
import sys
import random
import pygame_menu
from consts_ru import *

pygame.init()

size = [APP_WIDTH, APP_HEIGHT]

screen = pygame.display.set_mode(size)
pygame.display.set_caption(APP_CAPTION)
timer = pygame.time.Clock()
courier = pygame.font.SysFont('sans-serif', 36)

fullname = os.path.join('data', APP_FON_NAME)
fon = pygame.transform.scale(pygame.image.load(fullname), (APP_WIDTH, APP_HEIGHT))

screen.blit(fon, (0, 0))
pygame.display.flip()

fullname = os.path.join('data', MUSIC_FILE)
pygame.mixer.music.load(fullname)
pygame.mixer.music.play()
pmmp = True


class MusicBox(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)

        fullname = os.path.join('data', MUSIC_STATUS_ON)
        self.music_on = pygame.image.load(fullname)
        fullname = os.path.join('data', MUSIC_STATUS_OFF)
        self.music_off = pygame.image.load(fullname)

        self.image = self.music_on

        self.rect = self.music_on.get_rect()

        self.rect.x = MUSIC_LEFT + 175
        self.rect.y = MUSIC_TOP + 250

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            if self.image == self.music_on:
                self.image = self.music_off
            else:
                self.image = self.music_on


def game():
    pass


def app_menu(menu):
    menu.add_text_input(MENU_INPUT_TEXT, default='Gamer 1')
    menu.add_button(MENU_NEWGAME_TITLE, game)
    menu.add_button(MUSIC_STATUS, music_on_off)
    menu.add_button(MENU_EXIT_TITLE, pygame_menu.events.EXIT)


def music_on_off():
    global pmmp
    isout = False
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if pmmp:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
                pmmp = not pmmp
                isout = True
                break
        if isout:
            break

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE,
                         [MUSIC_LEFT - 10, MUSIC_TOP - 10,
                          APP_WIDTH - 2 * MUSIC_LEFT + 20, APP_HEIGHT - 2 * MUSIC_TOP + 20], width=1)
        pygame.draw.rect(screen, HEADER_COLOR,
                         [MUSIC_LEFT, MUSIC_TOP,
                          APP_WIDTH - 2 * MUSIC_LEFT, APP_HEIGHT - 2 * MUSIC_TOP])
        pygame.draw.rect(screen, FRAME_COLOR,
                         [MUSIC_LEFT, MUSIC_TOP,
                          APP_WIDTH - 2 * MUSIC_LEFT, HEADER_MARGIN])

        music_setup_title = courier.render("Музыка", 0, WHITE)
        screen.blit(music_setup_title, (MUSIC_LEFT + 165, MUSIC_TOP + 30))

        music_setup_status = courier.render("ВКЛ", 0, WHITE)
        screen.blit(music_setup_status, (MUSIC_LEFT + 110, MUSIC_TOP + 170))
        music_setup_status = courier.render("ВЫКЛ", 0, WHITE)
        screen.blit(music_setup_status, (MUSIC_LEFT + 250, MUSIC_TOP + 170))

        all_sprites = pygame.sprite.Group()
        music_box = MusicBox(all_sprites)
        all_sprites.draw(screen)


        all_sprites.update(pygame.event.get())
        all_sprites.draw(screen)
        pygame.display.flip()


        pygame.display.flip()


menu = pygame_menu.Menu(MENU_WIDTH, MENU_HEIGHT, MENU_WELCOME_TITLE,
                        theme=pygame_menu.themes.THEME_DARK)

app_menu(menu)

menu.mainloop(screen)
