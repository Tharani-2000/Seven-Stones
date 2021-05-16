class Ball:
    def __init__(self, screen, posx, ball_image):
        self.image = ball_image
        self.rectangle = self.image.get_rect(center=(posx, 580))
        self.screen = screen

    def move(self):
        self.rectangle.centery -= 5
        self.display()

    def display(self):
        self.screen.blit(self.image, self.rectangle)

    def collide(self, rect):
        return self.rectangle.colliderect(rect)
