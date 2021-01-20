from ball import Ball
from paddle import Paddle


class Instance:
    def __init__(self, screen):
        # creates a paddle and a ball and gives the ball a reference to the paddle
        self.paddle = Paddle(screen)
        self.ball = Ball(screen, self.paddle)

    # calls both update methods
    def update(self):
        self.paddle.update()
        self.ball.update()
