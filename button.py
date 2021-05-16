import pygame


def button(text, xmouse, ymouse, x, y, w, h, i, a, fs, window):
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(window, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(window, i, [x, y, w, h])
    message_display1(text, (x + w + x) / 2, (y + h + y) / 2, fs, window)


def message_display1(text, x, y, fs, window):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    window.blit(TextSurf, TextRect)


def text_objects1(text, font):
    textSurface = font.render(text, True, (250, 250, 250))
    return textSurface, textSurface.get_rect()