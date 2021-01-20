import pygame


# inherits from pygame's Sprite
class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, paddle):
        # calls the default init function for the superclass (Sprite)
        super().__init__()

        # declare attributes
        self.screen = screen
        self.paddle = paddle

        # creates the Surface to get rendered
        self.image = pygame.Surface([10, 10])
        self.image.fill((150, 0, 150))
        self.rect = self.image.get_rect()

        # position and velocity attributes
        self.xPos = screen.get_width() / 2
        self.yPos = screen.get_height() / 2
        self.velocity = [3, 3]

    def update(self):

        # updates the collision mask
        self.rect = pygame.rect.Rect([self.xPos, self.yPos, 10, 10])

        # changes position based on velocity
        self.xPos += self.velocity[0]
        self.yPos += self.velocity[1]

        # handles collision with paddle
        if pygame.sprite.collide_mask(self, self.paddle):
            if self.xPos <= self.paddle.xPos:
                self.velocity[0] *= -1
                self.xPos -= 7
            elif self.yPos <= self.paddle.yPos + self.paddle.rect[3]:
                self.velocity[1] *= -1
                self.yPos += 7
            elif self.yPos + self.rect[3] >= self.paddle.yPos:
                self.velocity[1] *= -1
                self.yPos -= 7

        # handles collision with the 4 screen boundaries
        if self.xPos >= self.screen.get_width() - self.image.get_width():
            self.velocity[0] *= -1
            # imitates clicking clicking close
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        if self.yPos >= self.screen.get_height() - self.image.get_height():
            self.velocity[1] *= -1
        if self.yPos <= 0:
            self.velocity[1] *= -1
        if self.xPos <= 100:
            self.velocity[0] *= -1

        # renders the now updated position of the ball to the screen
        self.draw()

    def draw(self):
        # blits the ball image surface to the screen
        self.screen.blit(self.image, (self.xPos, self.yPos))
