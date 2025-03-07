# importing module
import pygame

#initializing pygame
pygame.init()

# defining 'screen', setting root window size, setting root window title
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake Game")

# creating and drawing snake
snakeposition = (300, 300, 20, 20)
snake = pygame.draw.rect(screen, "lime", snakeposition)

# continuous loop
gameloop = True
while gameloop:
    # root window background color
    screen.fill("purple")
    
    # drawing snake
    snake = pygame.draw.rect(screen, "lime", snakeposition)
    # updating screen
    pygame.display.flip()
    
    # coding for X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

# closing root window after game is over
pygame.quit()