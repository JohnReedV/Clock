import os
import time
import pygame
from datetime import datetime
from pygame import mixer
from screen import Screen
from alarm import Alarm
from stopwatch import Stopwatch

pygame.init()

screen = Screen()
icon = pygame.image.load(os.path.join("assets", "clock.png")).convert_alpha()
alarm = pygame.image.load(os.path.join("assets", "alarm.png")).convert_alpha()
stopwatch = pygame.image.load(os.path.join("assets", "sw.png")).convert_alpha()
frame = pygame.image.load(os.path.join("assets", "frame.png")).convert_alpha()
font = pygame.font.Font('freesansbold.ttf', 69)

pygame.font.get_fonts()
pygame.display.set_caption("Clock of WONDERS")
pygame.display.set_icon(icon)

def now(x, y):
    now = font.render(str(current_time), True, (1, 12, 132))
    screen.blit(now, (x, y))


on = True
while on:
    current = datetime.now()
    current_time = current.strftime("%H:%M:%S")
    screen.fill((44, 76, 87))
    now(100, 40)

    screen.blit(frame, (175, 165))
    screen.blit(alarm, (175, 165))
    screen.blit(frame, (278, 165))
    screen.blit(stopwatch, (278, 163))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos1, pos2 = pygame.mouse.get_pos()
            if pos1 >= 174 and pos1 <= 207 and pos2 <= 200 and pos2 >= 160:
                mixer.init()
                mixer.music.load("press.wav")
                mixer.music.set_volume(.5)
                mixer.music.play()
                time.sleep(.25)
                Alarm()
                on = False
            if pos1 >= 278 and pos1 <= 308 and pos2 <= 200 and pos2 >= 160:
                mixer.init()
                mixer.music.load("press.wav")
                mixer.music.set_volume(.5)
                mixer.music.play()
                time.sleep(.25)
                Stopwatch()
                on = False


    pygame.display.update()

