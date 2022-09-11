
from playsound import playsound
from pygame import mixer
import pygame
import time
import sys
import os

pygame.init()

X = pygame.display.Info().current_w - 150
Y = pygame.display.Info().current_h

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

font = pygame.font.SysFont('segoeuisym', 32)

mixer.music.load("outro.mp3")
mixer.music.play()

messages = ["Bbg you had a good day today", "However I must shutdown now", " It was fun...", "Cya"]

def text(txt):
    text = font.render(txt, True, (0, 255, 0))
    textRect = text.get_rect() 
    textRect.center = (X // 2, Y // 2)

    return text, textRect


msg = 0
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    try:
        txt, pos = text(messages[msg])                  
    except:
        pygame.quit()
        sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(txt, pos)
    pygame.display.update()

    if msg == 3:
        time.sleep(2)
        os.system("shutdown /s /t 1")

    msg += 1
    time.sleep(4.7)
