# importing modules
import pygame
from random import randint

#initializing pygame
pygame.init()

# defining variables and constants
WIDTH = 600
HEIGHT = 600
APPLE_SIZE = 20
SNAKE_SIZE = 20

head_x = WIDTH//2
head_y = HEIGHT//2
snake_dx = 0
snake_dy = 0

score = 0
speed = 10

# regulating time so the program does not run too fast
FPS = 30
clock = pygame.time.Clock()

# defining 'screen', setting root window size, setting root window title
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

# uploading the apple eating sound
eat = pygame.mixer.Sound("C:/Users/Naras/OneDrive/Desktop/New folder/Python Games/snake game/eat.mp3")

# creating and drawing snake
snakeposition = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
snake = pygame.draw.rect(screen, "lime", snakeposition)

apple_position = (500, 500, APPLE_SIZE, APPLE_SIZE)
apple = pygame.draw.rect(screen, "red", apple_position)


# continuous loop
gameloop = True
while gameloop:
    # coding for X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    # moving the snake in x or y direction depending on what key is pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            snake_dx=1*speed
            snake_dy = 0
        elif event.key == pygame.K_LEFT:
            snake_dx= -1*speed
            snake_dy = 0
        elif event.key == pygame.K_UP:
            snake_dy= -1*speed
            snake_dx = 0
        elif event.key == pygame.K_DOWN:
            snake_dy= 1*speed
            snake_dx = 0
    
    # updating the snake position based on its direction
    head_x = head_x + snake_dx
    head_y += snake_dy
    snakeposition = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    #checking if the snake collides with the apple
    if snake.colliderect(apple):
        # playing uploaded sound
        eat.play()

        # moving the apple to a new random position
        x = randint(50, WIDTH-50)
        y = randint(50, HEIGHT-50)
        apple_position = (x, y, APPLE_SIZE, APPLE_SIZE)


    # root window background color
    screen.fill("purple")
    
    # drawing snake and apple
    snake = pygame.draw.rect(screen, "lime", snakeposition)
    apple = pygame.draw.rect(screen, "red", apple_position)
    
    # updating screen
    pygame.display.flip()
    clock.tick(FPS)
    
    

# closing root window after game is over
pygame.quit()