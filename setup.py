import pygame
import os
from database import *

def button2(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(window, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(window, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


def message_display(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    window.blit(TextSurf, TextRect)


def text_objects(text, font):
    textSurface = font.render(text, True, (250, 250, 250))
    return textSurface, textSurface.get_rect()


WIDTH = 400
HEIGHT = 620

# game initialization
pygame.init()
pygame.display.set_caption('stones')
window = pygame.display.set_mode((WIDTH, HEIGHT))
gameIcon = pygame.image.load(os.path.join('images', 'seven.ico'))
gameIcom = pygame.transform.scale(gameIcon, (20, 20))
pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()
background = pygame.image.load(os.path.join('images', 'background.png')).convert_alpha()
background = pygame.transform.scale(background, (400, 620))
red = pygame.image.load(os.path.join('images', 'redball.png')).convert_alpha()
red = pygame.transform.scale(red, (30, 30))
white = pygame.image.load(os.path.join('images', 'ball.png')).convert_alpha()
white = pygame.transform.scale(white, (30, 30))
dic = {'red': red, 'white': white}
ball = getdefaultball()
ball_list = []

# start and music
poweredby = pygame.image.load(os.path.join('images', 'poweredby.png')).convert_alpha()
poweredby = pygame.transform.scale(poweredby, (400, 620))
start_screen = pygame.image.load(os.path.join('images', 'start.jpeg')).convert_alpha()
start_screen = pygame.transform.scale(start_screen, (400, 620))
pygame.mixer.music.load(os.path.join('sounds', "music.wav"))

# coin image
coin_image = pygame.image.load(os.path.join('images', 'coin.png')).convert_alpha()
coin_image = pygame.transform.scale(coin_image, (30, 30))
window.blit(coin_image, (4, 2))


def checkballimage():
    global dic
    ball = getdefaultball()
    return dic[ball]
