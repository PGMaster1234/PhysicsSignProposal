from viable import *
import pygame
import math
import time

pygame.init()

# ---------------- Setting up the screen, assigning some global variables, and loading text fonts
screen = pygame.display.set_mode((1050, 700))
# screen = pygame.display.set_mode((1200, 650))
clock = pygame.time.Clock()
fps = 60
screen_width = screen.get_width()
screen_height = screen.get_height()
screen2 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screen3 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screen3.set_alpha(100)
screen4 = pygame.Surface((screen_width, screen_height)).convert_alpha()
timer = 0
shake = [0, 0]
shake_strength = 3
scroll_counter = 0
pygame.font.get_fonts()
font15 = pygame.font.Font("freesansbold.ttf", 15)
font20 = pygame.font.Font("freesansbold.ttf", 20)
font30 = pygame.font.Font("freesansbold.ttf", 30)
font40 = pygame.font.Font("freesansbold.ttf", 40)
better_font40 = pygame.font.SysFont("keyboard.ttf", 40)
font50 = pygame.font.Font("freesansbold.ttf", 50)
font100 = pygame.font.Font("freesansbold.ttf", 100)
line_length = 200


class Endesga:
    maroon_red = (87, 28, 39)
    lighter_maroon_red = (127, 36, 51)
    dark_green = (9, 26, 23)
    light_brown = (191, 111, 74)
    black = (19, 19, 19)
    grey_blue = (66, 76, 110)
    cream = (237, 171, 80)
    white = (255, 255, 255)
    very_light_blue = (199, 207, 221)
    my_blue = [7, 15, 21]


# Defining some more variables to use in the game loop
oscillating_random_thing = 0
ShakeCounter = 0
moveR = False
moveL = False
moveU = False

x = viable(signs["i"][0], beams["n"][0], cables["c"][0], 50)[2]

# ---------------- Main Game Loop
last_time = time.time()
running = True
while running:

    # ---------------- Reset Variables and Clear screens
    oscillating_random_thing += math.pi/fps
    click = False
    shifted_scroll = [screen_width / 2, screen_height / 2]
    mx, my = pygame.mouse.get_pos()
    screen.fill(Endesga.my_blue)
    screen2.fill(Endesga.my_blue)
    screen3.fill((0, 0, 0, 0))
    screen4.fill((0, 0, 0, 0))
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()
    timer -= 1 * dt
    shake = [0, 0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            pass

    for a in x:
        blit_a = a + math.pi
        pygame.draw.line(screen2, Endesga.white, (screen_width / 2, screen_height / 2), (screen_width / 2 + line_length * math.cos(blit_a), screen_height / 2 + line_length * math.sin(blit_a)))

    pygame.mouse.set_visible(False)
    pygame.draw.circle(screen4, Endesga.white, (mx, my), 5, 1)
    screen.blit(screen2, (shake[0], shake[1]))
    screen.blit(screen3, (0, 0))
    screen.blit(screen4, (0, 0))
    pygame.display.update()
    clock.tick(fps)
