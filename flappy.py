import pygame
import random
import math

pygame.init()

# game window
width, height = 400, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird Clone")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Bird stuff
bird_x = 50
bird_y = height // 2
bird_radius = 20
bird_color = blue
bird_velocity = 0
bird_jump = -10

# Gravity
gravity = 0.5

# Pipe stuff
pipe_width = 50
pipe_gap = 200
pipe_color = white
pipe_list = []
pipe_spawn_time = 1500 
last_pipe_spawn = pygame.time.get_ticks()


# Game loop
running = True
game_over = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_over: 
                bird_velocity = bird_jump
            if game_over:
                # Restart when the player presses space after game over
                bird_y = height // 2
                bird_velocity = 0
                pipe_list = []
                game_over = False

    # Birb movement
    bird_velocity += gravity
    bird_y += bird_velocity

    # game over check
    if bird_y > height or bird_y < 0:
        game_over = True

    # Pipe
    if pygame.time.get_ticks() - last_pipe_spawn > pipe_spawn_time:
        pipe_height = random.randint(100, height - pipe_gap - 100)
        pipe_list.append([width, 0, pipe_width, pipe_height])
        pipe_list.append([width, pipe_height + pipe_gap, pipe_width, height - pipe_height - pipe_gap])
        last_pipe_spawn = pygame.time.get_ticks()

    # Pipe movement
    for pipe in pipe_list:
        pipe[0] -= 5

    # Bird collision with pipes
    for pipe in pipe_list:
        pipe_x, pipe_y, pipe_width, pipe_height = pipe

    # Check collision with the pipe's left border
        if bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width:
            if bird_y - bird_radius < pipe_y + pipe_height and bird_y + bird_radius > pipe_y:
                game_over = True

    # Check collision with the pipe's right border
        if bird_x - bird_radius < pipe_x + pipe_width and bird_x + bird_radius > pipe_x:
            if bird_y - bird_radius < pipe_y + pipe_height:
                game_over = True
         # Check collision with the top of the pipe
        if bird_y - bird_radius < pipe_y and bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width:
            game_over = True

        # Check collision with the bottom of the pipe
        if bird_y + bird_radius > pipe_y + pipe_height and bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width:
            game_over = True


    # Clear screen
    window.fill((0, 0, 0))

    # Draw pipes
    for pipe in pipe_list:
        pygame.draw.rect(window, pipe_color, pipe)

    # Draw bird
    pygame.draw.circle(window, bird_color, (bird_x, int(bird_y)), bird_radius)

    # game over
    if game_over:
        font = pygame.font.Font(None, 36)
        game_over_text = font.render("Game Over", True, white)
        restart_text = font.render("Press SPACE to Restart", True, white)
        window.blit(game_over_text, (width // 2 - 80, height // 2 - 20))
        window.blit(restart_text, (width // 2 - 130, height // 2 + 20))


    pygame.display.update()
    clock.tick(30)

pygame.quit()

