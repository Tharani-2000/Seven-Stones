import sys
import os
from button import *
from database import *


COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)
font = pygame.font.Font(None, 22)
image = pygame.image.load(os.path.join('images', 'icon' + '.png')).convert_alpha()
image = pygame.transform.scale(image, (80, 80))


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.password = ''

    def handle_event(self, event, key=False):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.password = self.password[:-1]
                else:
                    self.text += event.unicode
                    if key:
                        self.password += "*"
                # Re-render the text.
                self.txt_surface = FONT.render(self.password if key else self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



def signingup(name , password):
    insert_signupvalues_database(name, password)
    return False

def logingin(name, password):
    return checkforlogin(name, password)


def intro(window, poweredby, clock):

    login = False
    sign = False

    global event
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 2500:
        window.blit(poweredby, (0, 0))
        pygame.display.update()

    input_box1 = InputBox(100, 300, 140, 32)
    input_box2 = InputBox(100, 400, 140, 32)

    introduction = True
    passwordincorrect = False

    while introduction:
        clock.tick(60)

        window.fill((250, 250, 250))
        mouse = pygame.mouse.get_pos()

        name_surface = FONT.render('Name:', True, (0,0,0))
        window.blit(name_surface, (100, 275))
        input_box1.draw(window)
        pass_surface = FONT.render('Password:', True, (0, 0, 0))
        window.blit(pass_surface, (100, 375))
        input_box2.draw(window)




        for event in pygame.event.get():
            input_box1.handle_event(event)
            input_box2.handle_event(event, True)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        if button("LOGIN", mouse[0], mouse[1], 150, 200, 50, 30, (43, 3, 132), (60, 0, 190), 10, window) or login:
            login = True
            if button("LOGIN", mouse[0], mouse[1], 180, 470, 50, 30, (43, 3, 132), (60, 0, 190), 10, window):
                login = False
                passed = logingin(input_box1.text, input_box2.text)
                if passed:
                    introduction = False
                else:
                    passwordincorrect = True
                    name_surface = FONT.render('Name or Password is incorrect', True, (0, 0, 0))
                    window.blit(name_surface, (10, 250))



        if button("SIGN UP", mouse[0], mouse[1], 210, 200, 50, 30, (43, 3, 132), (60, 0, 190), 10, window) or sign:
            sign = True
            if button("SIGN UP", mouse[0], mouse[1], 180, 470, 50, 30, (43, 3, 132), (60, 0, 190), 10, window):
                sign = False
                introduction = signingup(input_box1.text, input_box2.text)

        if passwordincorrect:
            name_surface = font.render('Name or Password is incorrect', True, (250, 0, 0))
            window.blit(name_surface, (70, 250))


        input_box1.update()
        input_box2.update()
        window.blit(image, (170, 100))
        pygame.display.update()



