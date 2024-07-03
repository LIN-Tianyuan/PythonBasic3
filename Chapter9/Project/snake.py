import pygame
import sys
import random

pygame.init()

black = (0, 0, 0)
green = (50, 155, 50)
red = (255, 0, 0)
white = (255, 255, 255)

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

    game_window.fill(black)


    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    show_score('Arial', 20, white)
    pygame.display.flip()
    fps.tick(20)






