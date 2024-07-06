import pygame
import sys
import random
import time

pygame.init()

black = (0, 0, 0)
green = (50, 155, 50)
red = (255, 0, 0)
white = (255, 255, 255)
pink = (255, 192, 203)

window_x = 720
window_y = 480


snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]
fruit_position = [random.randint(1, window_x // 10) * 10, random.randint(1, window_y // 10) * 10]

direction = 'RIGHT'
change_direction = direction

# Score initial
score = 0


def show_score(font, size, color):
    score_font = pygame.font.SysFont(font, size)
    score_text = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_text.get_rect()
    game_window.blit(score_text, score_rect)


def game_over(font, size, color):
    over_font = pygame.font.SysFont(font, size)
    over_text = over_font.render('Your score is : ' + str(score), True, color)
    over_rect = over_text.get_rect()
    over_rect.center = (window_x / 2, window_y / 2)
    game_window.blit(over_text, over_rect)
    pygame.display.flip()
    # Après 2 secondes, nous quitterons le programme
    time.sleep(2)
    pygame.quit()
    sys.exit()



# Initialisation de la fenêtre de jeu
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
pygame.display.set_caption("Snake")

while True:
    for event in pygame.event.get():
        # Gestion des événements clés
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_direction = 'UP'
            if event.key == pygame.K_DOWN:
                change_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_direction = 'RIGHT'

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if direction != 'RIGHT' and change_direction == 'LEFT':
        direction = 'LEFT'
    if direction != 'LEFT' and change_direction == 'RIGHT':
        direction = 'RIGHT'
    if direction != 'UP' and change_direction == 'DOWN':
        direction = 'DOWN'
    if direction != 'DOWN' and change_direction == 'UP':
        direction = 'UP'

    # Serpent en mouvement
    if direction == 'RIGHT':
        snake_position[0] = snake_position[0] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10

    snake_body.insert(0, list(snake_position))

    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score = score + 10
        fruit_position = [random.randint(1, window_x // 10) * 10, random.randint(1, window_y // 10) * 10]
    else:
        snake_body.pop()

    game_window.fill(pink)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Toucher le corps du serpent
    for block in snake_body[1: ]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over('Arial', 50, red)


    show_score('Arial', 20, white)
    pygame.display.flip()
    fps.tick(20)






