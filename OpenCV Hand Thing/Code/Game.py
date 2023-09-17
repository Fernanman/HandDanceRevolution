import pygame
from sys import exit
from pygame.locals import *

from time import time_ns, sleep
from HandReader import *
import random

clock = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.display.set_caption("Plant Gang")

size = pygame.display.get_desktop_sizes()
WINDOW_SIZE = (1000, 600)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((1000, 600))

icon = pygame.image.load("Assets\\Fern.png").convert_alpha()
pygame.display.set_icon(icon)

# Hand signs
index = pygame.image.load("Assets\\Index.png").convert_alpha()
index_middle = pygame.image.load("Assets\\Index-Middle.png").convert_alpha()
pinky_thumb = pygame.image.load("Assets\\Pinky-Thumb.png").convert_alpha()
pinky_thumb_index = pygame.image.load("Assets\\Pinky-Thumb-Index.png").convert_alpha()


def song_select():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0,0))
        pygame.display.update()
        clock.tick(60)

def test():
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    font = pygame.font.Font('Game\\Assets\\pcsenior.ttf', 32)
    text = font.render('a', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

    while True:
        display.blit(text, textRect)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0,0))
        pygame.display.update()
        clock.tick(60)

def survival():
    setup = setup_camera()
    white = (255, 255, 255)
    thing_map = {0 : "Index",
                 1 : "Index-Middle",
                 2 : "Pinky-Thumb",
                 3 : "Pinky-Thumb-Index"}
    
    border = pygame.image.load("Assets\\border.png").convert()
    left_rect = border.get_rect(center = (250, 300))
    right_rect = border.get_rect(center = (750, 300))

    signs_signals = [index, index_middle, pinky_thumb, pinky_thumb_index]
    start_left = False
    start_right = False
    
    combo = 0
    pc_senior = pygame.font.Font("Assets\\pcsenior.ttf", 32)

    while True:
        display.fill(white)
        handsigns = detect_handsign(*setup)

        if combo <= 10000:
            if not start_left:
                time_start_left = time_ns()
                start_left = True
                pick_1 = random.randint(0,3)
            else:
                display.blit(signs_signals[pick_1], left_rect)
                time_elapsed_left = time_start_left - time_ns()
                if handsigns != None and (thing_map[pick_1], "Left") in handsigns:
                    combo += 1
                    start_left = False
                elif time_elapsed_left > 2e+9:
                    pygame.quit()
                    exit()

        # elif combo <=20:
        #     pick_2 = random.randint(0,4)
        # else:
        #     pass

        combo_surface = pc_senior.render(f"Combo: {combo}", False, (0, 0, 0))
        top_text_rect = combo_surface.get_rect(midleft = (0, 50))
        display.blit(combo_surface, top_text_rect)

        print(clock.get_time())

        if handsigns == 'break':
            break
        elif handsigns != None:
            for sign in handsigns:
                print(sign[0], '-', sign[1])

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0,0))
        pygame.display.update()
        clock.tick(60)
        

def song():
    pass



if __name__ == "__main__":
    survival()