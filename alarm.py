import time
from datetime import datetime

from pygame import mixer

from screen import Screen
import pygame
import os

pygame.init()
screen = Screen()
pygame.font.get_fonts()
icon = pygame.image.load(os.path.join("assets", "clock.png")).convert_alpha()
alarm = pygame.image.load(os.path.join("assets", "alarm.png")).convert_alpha()
stopwatch = pygame.image.load(os.path.join("assets", "sw.png")).convert_alpha()
frame = pygame.image.load(os.path.join("assets", "frame.png")).convert_alpha()
font = pygame.font.Font('freesansbold.ttf', 45)
input_box = pygame.Rect(130, 50, 240, 60)



def Alarm():
    on = True
    dog = True
    active = False
    once = True
    text = ''
    bossmode = ":"
    while on:
        while dog:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            dog = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.fill((44, 76, 87))
            txt_surface = font.render(text, True, (1, 12, 132))
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

            pygame.display.update()

        def now(x, y):
            now = font.render(str(current_time), True, (0, 77, 0))
            screen.blit(now, (x, y))

        format = "%H:%M"
        dt_object = datetime.strptime(text, format)

        screen.fill((44, 76, 87))
        screen.blit(frame, (175, 165))
        screen.blit(alarm, (175, 165))
        screen.blit(frame, (278, 165))
        screen.blit(stopwatch, (278, 163))
        now1 = font.render(str(dt_object.minute), True, (1, 12, 132))
        screen.blit(now1, (245, 105))
        now2 = font.render(str(dt_object.hour), True, (1, 12, 132))
        screen.blit(now2, (180, 105))
        now3 = font.render(str(bossmode), True, (1, 12, 132))
        screen.blit(now3, (230, 102))
        current = datetime.now()
        current_time = current.strftime("%H:%M:%S")
        now(130, 40)

        if dt_object.minute == current.minute and dt_object.hour == current.hour:
            if once:
                mixer.init()
                mixer.music.load("alarm.wav")
                mixer.music.set_volume(1)
                mixer.music.play()
                once = False

        pygame.display.update()
        time.sleep(1)
