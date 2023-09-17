import pygame
from sys import exit
from pygame.locals import *

from time import time_ns, sleep
from HandReader import *
import random

clock = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.display.set_caption("Hand Dance Revolution")

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

setup = setup_camera()


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

def try_again():
    black = (0, 0, 0)
    pc_senior = pygame.font.Font("Assets\\pcsenior.ttf", 32)
    try_agian_surface = pc_senior.render("Press space to try again", False, (255, 255, 255))
    try_again_rect = try_agian_surface.get_rect(center = (500, 300))
    
    while True:
        display.fill(black)
        display.blit(try_agian_surface, try_again_rect)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    survival()
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0,0))
        pygame.display.update()
        clock.tick(60)


def survival():
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
    seconds = 5

    combo = 0
    pc_senior = pygame.font.Font("Assets\\pcsenior.ttf", 32)

    while True:
        display.fill(white)
        handsigns = detect_handsign(*setup)

        if combo <= 10000:
            if not start_left and not start_right:
                time_start_left = time_ns()
                start_left = True
                pick_1 = random.randint(0, 3)
                pick_2 = random.randint(0, 3)
            else:
                display.blit(signs_signals[pick_1], left_rect)
                display.blit(signs_signals[pick_2], right_rect)
                time_elapsed_left = time_ns() - time_start_left 
                if handsigns != None and (thing_map[pick_1], "Left") in handsigns and \
                (thing_map[pick_2], "Right") in handsigns:
                    combo += 1
                    start_left = False
                    start_right = False
                elif time_elapsed_left > (seconds * 1e+9):
                    try_again()

        combo_surface = pc_senior.render(f"Combo: {combo}", False, (0, 0, 0))
        top_text_rect = combo_surface.get_rect(midleft = (0, 50))
        display.blit(combo_surface, top_text_rect)

        if handsigns == 'break':
            break

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
