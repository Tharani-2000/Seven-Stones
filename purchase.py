import pygame
import os
from button import *
from database import *


def purchase(window, score, background):
    pbool = True
    window.blit(background, (0, 0))
    mouse = pygame.mouse.get_pos()

    white_ball = pygame.image.load(os.path.join('images', 'ball.png')).convert_alpha()
    white_ball = pygame.transform.scale(white_ball, (100, 100))
    white_ball_rect = white_ball.get_rect(center=(125, 400))

    red_ball = pygame.image.load(os.path.join('images', 'redball.png')).convert_alpha()
    red_ball = pygame.transform.scale(red_ball, (120, 120))
    red_ball_rect = red_ball.get_rect(center=(280, 410))

    window.blit(white_ball, white_ball_rect)
    window.blit(red_ball, red_ball_rect)
    score_font = pygame.font.Font('04B_19.ttf', 40)
    score_surface = score_font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(75, 20))
    window.blit(score_surface, score_rect)
    coin_image = pygame.image.load(os.path.join('images', 'coin.png')).convert_alpha()
    coin_image = pygame.transform.scale(coin_image, (40, 40))
    window.blit(coin_image, (3, 2))
    Text = pygame.font.Font('freesansbold.ttf', 12)

    purchased = getpurchased()

    text = 'BUY 200 COINS'
    if 'red' == purchased.lower().strip():
        text = 'Purchased'

    if (230 < mouse[0] < 320) and (380 < mouse[1] < 400):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if purchased.lower().strip() != 'red' and score > 200:
                purchased = 'red'
                score -= 200
                text = 'Purchased'
                updatepurchase('red')
            updatedefaultball('red')

    if (30 < mouse[0] < 170) and (380 < mouse[1] < 400):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            updatedefaultball('white')

    default_ball = getdefaultball()

    default = (125, 460)
    if default_ball.strip().lower() == 'red':
        default = (285, 490)

    red_ball_text = Text.render(text, True, (0, 0, 0))
    red_ball_text_rect = red_ball_text.get_rect(center=(285, 460))
    window.blit(red_ball_text, red_ball_text_rect)

    white_ball_text = Text.render('Default Ball', True, (0, 0, 0))
    white_ball_text_rect = white_ball_text.get_rect(center=default)
    window.blit(white_ball_text, white_ball_text_rect)

    if button("Start Game", mouse[0], mouse[1], 250, 0, 150, 30, (43, 3, 132), (60, 0, 190), 10, window):
        pbool = False
        updatepurchase(purchased)

    return pbool, score


