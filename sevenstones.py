import pygame
import os


class red:
    def __init__(self, window):
        surface = pygame.image.load(os.path.join('stones', 'red.png')).convert_alpha()
        self.surface = pygame.transform.scale(surface, (40, 30))
        self.rect = surface.get_rect(center=(300 + 50, 350))
        self.window = window
        self.visible = True

    def display(self):
        if self.visible:
            self.window.blit(self.surface, self.rect)


class blue:
    def __init__(self, window):
        surface = pygame.image.load(os.path.join('stones', 'blue.png')).convert_alpha()
        self.surface = pygame.transform.scale(surface, (36, 20))
        self.rect = surface.get_rect(center=(300 + 100, 300))
        self.window = window
        self.visible = True

    def display(self):
        if self.visible:
            self.window.blit(self.surface, self.rect)


class black:
    def __init__(self, window):
        surface = pygame.image.load(os.path.join('stones', 'black.png')).convert_alpha()
        self.surface = pygame.transform.scale(surface, (32, 20))
        self.rect = surface.get_rect(center=(70 + 50, 370))
        self.window = window
        self.visible = True

    def display(self):
        if self.visible:
            self.window.blit(self.surface, self.rect)


class green:
    def __init__(self, window):
        surface = pygame.image.load(os.path.join('stones', 'green.png')).convert_alpha()
        self.surface = pygame.transform.scale(surface, (35, 20))
        self.rect = surface.get_rect(center=(50 + 50, 400))
        self.window = window
        self.visible = True

    def display(self):
        if self.visible:
            self.window.blit(self.surface, self.rect)


class yellow:
    def __init__(self, window):
        surface = pygame.image.load(os.path.join('stones', 'yellow.png')).convert_alpha()
        self.surface = pygame.transform.scale(surface, (38, 23))
        self.rect = surface.get_rect(center=(300 + 100, 320))
        self.window = window
        self.visible = True

    def display(self):
        if self.visible:
            self.window.blit(self.surface, self.rect)


class orange:

    def __init__(self, window):
        surface = pygame.image.load(os.path.join('stones', 'orangle.png')).convert_alpha()
        self.surface = pygame.transform.scale(surface, (39, 23))
        self.rect = surface.get_rect(center=(200 + 100, 400))
        self.window = window
        self.visible = True

    def display(self):
        if self.visible:
            self.window.blit(self.surface, self.rect)


class grey:

    def __init__(self, window):
        surface = pygame.image.load(os.path.join('stones', 'grey.png')).convert_alpha()
        self.surface = pygame.transform.scale(surface, (40, 20))
        self.rect = surface.get_rect(center=(80 + 50, 430))
        self.window = window
        self.visible = True

    def display(self):
        if self.visible:
            self.window.blit(self.surface, self.rect)
