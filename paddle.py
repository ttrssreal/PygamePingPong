import pygame


# inherits from pygame's Sprite
class Paddle(pygame.sprite.Sprite):
    def __init__(self, screen):
        # calls the default init function for the superclass (Sprite)
        super().__init__()

        # declare attributes
        self.screen = screen
        self.key_state = None

        # creates the Surface to get rendered
        self.image = pygame.Surface([25, 200])
        self.image.fill((20, 60, 150))
        self.rect = self.image.get_rect()

        # position and velocity attributes
        self.xPos = screen.get_width() - 60
        self.yPos = (screen.get_height() / 2) - (self.image.get_height() / 2)

        # velocity is 1D where magnitude is speed and direction is controlled by whether it is positive or negative
        # example: up and fast would be   (5)
        #          down and slow would be (-1)
        self.velocity = 0

    def update(self):

        # gets the 'key pressed' array
        self.key_state = pygame.key.get_pressed()

        # updates the collision mask
        self.rect = pygame.rect.Rect([self.xPos, self.yPos, 25, 200])

        # polls for keyboard input and changes velocity accordingly
        if self.key_state[pygame.K_UP]:
            self.velocity = -3
        elif self.key_state[pygame.K_DOWN]:
            self.velocity = 3
            # if no keys pressed the stop
        else:
            self.velocity = 0

        # updates velocity
        self.yPos += self.velocity

        # constricts movement between the edges of the screen
        if self.yPos <= 0:
            self.yPos = 0
        if self.yPos >= self.screen.get_height() - self.image.get_height():
            self.yPos = self.screen.get_height() - self.image.get_height()

        # renders the now updated position of the paddle to the screen
        self.draw()

        # not really sure tbh :)
        pygame.event.pump()

    def draw(self):
        # blits the paddle image surface to the screen
        self.screen.blit(self.image, (self.xPos, self.yPos))
