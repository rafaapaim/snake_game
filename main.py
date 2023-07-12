import pygame
import random

from config import *


pygame.init()
pygame.display.set_caption('Snake')
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

square_size = 20
game_speed = 15

def create_food():
    food_x = round(random.randrange(0, width - square_size) / float(square_size)) * float(square_size)
    food_y = round(random.randrange(0, height - square_size) / float(square_size)) * float(square_size)
    return food_x, food_y

def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, GREEN, [food_x, food_y, size, size])

def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, WHITE, [pixel[0], pixel[1], size, size])

def draw_score(score):
    font = pygame.font.SysFont('Helvetica', 50)
    text = font.render(f'Score: {score}', True, RED)
    screen.blit(text, [1, 1])

def speed_select(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = square_size
    elif key == pygame.K_UP:
        speed_x = 0
        speed_y = - square_size
    elif key == pygame.K_RIGHT:
        speed_x = square_size
        speed_y = 0
    elif key == pygame.K_LEFT:
        speed_x = - square_size
        speed_y = 0

    return speed_x, speed_y

def run_game():
    end_game = False

    x = width / 2
    y = height / 2
    speed_x = 0
    speed_y = 0
    snake_size = 1
    pixels = []
    
    food_x, food_y = create_food()

    while not end_game:
        screen.fill(BLACK)

        for player_event in pygame.event.get():
            if player_event.type == pygame.QUIT:
                end_game = True
            elif player_event.type == pygame.KEYDOWN:
                speed_x, speed_y = speed_select(player_event.key)

        draw_food(square_size, food_x, food_y)
        
        if x < 0 or x >= width or y < 0 or y >= height:
            end_game = True
        
        x += speed_x
        y += speed_y
        
        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels[0]

        for pixel in pixels[: -1]:
            if pixel == [x, y]:
                end_game = True
        
        draw_snake(square_size, pixels)
        draw_score(snake_size - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = create_food()

        clock.tick(game_speed)

run_game()
