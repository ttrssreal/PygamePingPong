import pygame
from instance import Instance

pygame.init()

screen = pygame.display.set_mode((1100, 800))
clock = pygame.time.Clock()

# create wall
wall = pygame.Rect((50, 0), (20, screen.get_height()))

# create game instance and pass in the screen
instance = Instance(screen)

# start the main game loop
running = True
while running:
    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # color screen black, for new frame
    screen.fill((0, 0, 0))

    # render the wall, in white
    pygame.draw.rect(screen, (255, 255, 255), (80, 0, 20, screen.get_height()))

    # update the game
    instance.update()

    # update the screen & 60 fps maximum
    pygame.display.update()
    clock.tick(60)

# quit upon exit
pygame.quit()
quit()