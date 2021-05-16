import pygame
import os
import random


class Runner:
    run_list_left = []
    run_list_right = []
    run_list = {}

    for i in range(1, 4):
        image = pygame.image.load(os.path.join('images', 'run' + str(i) + '.png')).convert_alpha()
        image = pygame.transform.scale(image, (60, 60))
        right = pygame.transform.flip(image, True, False)
        run_list_left.append(image)
        run_list_right.append(right)

    run_list['right'] = run_list_right
    run_list['left'] = run_list_left

    run_index = 0

    def __init__(self, direction, window):
        self.image = self.run_list[direction][self.run_index]
        self.direction = direction
        self.x, self.y = self.getrandom(direction)
        self.rectangle = self.image.get_rect(center=(self.x, self.y))
        self.window = window
        self.stone = False
        self.colors = ""

    def image_selection(self, index):
        self.run_index = index
        self.image = self.run_list[self.direction][self.run_index]
        self.rectangle = self.image.get_rect(center=(self.rectangle.centerx, self.y))

    def getrandom(self, direction):
        left = [(0, 300), (0, 350), (0, 400), (0, 450), (0, 450), (0, 400)]
        right = [(400, 300), (400, 350), (400, 400), (400, 450), (400, 400), (400, 450)]

        if direction.lower() == 'right':
            return random.choice(right)
        return random.choice(left)

    def display(self):
        self.window.blit(self.image, self.rectangle)

    def move(self):
        direction = self.direction

        if direction == 'right':
            self.rectangle.centerx -= 3
        else:
            self.rectangle.centerx += 3
        self.display()

    def collision(self, rect):
        return self.rectangle.colliderect(rect)


def createRunner(direction, window):
    run = Runner(direction, window)
    return run
