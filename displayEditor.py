import math
import time
from button import *
from data import *

pygame.init()

# ---------------- Setting up the screen, assigning some global variables, and loading text fonts
screen = pygame.display.set_mode((1050, 700))
clock = pygame.time.Clock()
fps = 60
screen_width = screen.get_width()
screen_height = screen.get_height()
screen2 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screenT = pygame.Surface((screen_width, screen_height)).convert_alpha()
screenT.set_alpha(100)
screenUI = pygame.Surface((screen_width, screen_height)).convert_alpha()
timer = 0
shake = [0, 0]
shake_strength = 3
scroll_counter = 0
pygame.font.get_fonts()
font15 = pygame.font.Font("freesansbold.ttf", 15)
font20 = pygame.font.Font("freesansbold.ttf", 20)
font30 = pygame.font.Font("freesansbold.ttf", 30)
font40 = pygame.font.Font("freesansbold.ttf", 40)
better_font20 = pygame.font.SysFont("keyboard.ttf", 20)
better_font30 = pygame.font.SysFont("keyboard.ttf", 30)
better_font40 = pygame.font.SysFont("keyboard.ttf", 40)
better_font60 = pygame.font.SysFont("keyboard.ttf", 60)
better_font100 = pygame.font.SysFont("keyboard.ttf", 100)
font50 = pygame.font.Font("freesansbold.ttf", 50)
font100 = pygame.font.Font("freesansbold.ttf", 100)

# ----------------------------- Parameters
cable_strength = "a"
sign = "g"
beam = "l"
angle = 0


class Endesga:
    maroon_red = (87, 28, 39)
    lighter_maroon_red = (127, 36, 51)
    dark_green = (9, 26, 23)
    light_brown = (191, 111, 74)
    black = (19, 19, 19)
    grey_blue = (66, 76, 110)
    cream = (237, 171, 80)
    white = (255, 255, 255)
    greyL = (200, 200, 200)
    grey = (150, 150, 150)
    greyD = (100, 100, 100)
    greyVD = (50, 50, 50)
    very_light_blue = (199, 207, 221)
    my_blue = [7, 15, 21]


# Defining some more variables to use in the game loop
oscillating_random_thing = 0
ShakeCounter = 0

cableB = create_buttons(6, 1, 70, 0, 100, 50, ["a", "b", "c", "d", "e", "f"], [], [50, 600], cables)
signsB = create_buttons(5, 1, 70, 0, 100, 50, ["g", "h", "i", "j", "k"], [], [135, 500], signs)
beamsB = create_buttons(4, 1, 70, 0, 100, 50, ["l", "m", "n", "o"], [], [220, 400], beams)


def cost(ca, si, be, an):
    c = 0
    c += beams[be][1]
    c += signs[si][1]
    beamL = beams[be][2]
    cableL = beamL / math.cos(an)
    c += cableL * cables[ca][1]
    return c


# ---------------- Main Game Loop
last_time = time.time()
running = True
while running:

    # ---------------- Reset Variables and Clear screens
    oscillating_random_thing += math.pi/fps
    click = False
    mx, my = pygame.mouse.get_pos()
    screen.fill(Endesga.my_blue)
    screen2.fill(Endesga.my_blue)
    screenT.fill((0, 0, 0, 0))
    screenUI.fill((0, 0, 0, 0))
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()
    timer -= 1 * dt
    shake = [0, 0]
    if angle < math.pi / 2:
        angle += math.pi / 360
    else:
        angle = 0

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

    screen2.blit(better_font60.render("Cable Strength", True, Endesga.very_light_blue), (screen_width / 2 - pygame.font.Font.size(better_font60, "Cable Strength")[0] / 2, 560))
    cable_buttons_clicked = draw_buttons(cableB[0], cableB[1], cableB[2], [Endesga.white, Endesga.my_blue, Endesga.grey, Endesga.greyD], cableB[4], screen2, 0, 10, better_font40, click, mx, my)
    for i, b in enumerate(cable_buttons_clicked):
        if b:
            cable_strength = ["a", "b", "c", "d", "e", "f"][i]

    screen2.blit(better_font60.render("Sign", True, Endesga.very_light_blue), (screen_width / 2 - pygame.font.Font.size(better_font60, "Sign")[0] / 2, 460))
    sign_buttons_clicked = draw_buttons(signsB[0], signsB[1], signsB[2], [Endesga.white, Endesga.my_blue, Endesga.grey, Endesga.greyD], signsB[4], screen2, 0, 10, better_font40, click, mx, my)
    for i, b in enumerate(sign_buttons_clicked):
        if b:
            sign = ["g", "h", "i", "j", "k"][i]

    screen2.blit(better_font60.render("Beam", True, Endesga.very_light_blue), (screen_width / 2 - pygame.font.Font.size(better_font60, "Beam")[0] / 2, 360))
    beam_buttons_clicked = draw_buttons(beamsB[0], beamsB[1], beamsB[2], [Endesga.white, Endesga.my_blue, Endesga.grey, Endesga.greyD], beamsB[4], screen2, 0, 10, better_font40, click, mx, my)
    for i, b in enumerate(beam_buttons_clicked):
        if b:
            beam = ["l", "m", "n", "o"][i]

    screen2.blit(better_font60.render(str((cables[cable_strength])[0]), True, Endesga.very_light_blue), (200, 300))
    screen2.blit(better_font60.render(str((signs[sign])[0]), True, Endesga.very_light_blue), (200, 200))
    screen2.blit(better_font60.render(str((beams[beam])[0]), True, Endesga.very_light_blue), (200, 100))

    passing = False
    if (math.sin(angle) * cables[cable_strength][0]) > (signs[sign][0] + beams[beam][0] + 20):
        passing = True

    screen2.blit(better_font60.render(str(passing), True, Endesga.very_light_blue), (500, 100))
    screen2.blit(better_font60.render(str(angle), True, Endesga.very_light_blue), (500, 150))
    screen2.blit(better_font60.render(str(cost(cable_strength, sign, beam, angle)), True, Endesga.very_light_blue), (500, 200))
    pygame.draw.line(screen2, Endesga.white, (500, 150), (500 + 100 * math.cos(angle), 150 + -100 * math.sin(angle)))

    pygame.mouse.set_visible(False)
    pygame.draw.circle(screenUI, Endesga.very_light_blue, (mx, my), 5, 1)
    screen.blit(screen2, (shake[0], shake[1]))
    screen.blit(screenT, (0, 0))
    screen.blit(screenUI, (0, 0))
    pygame.display.update()
    clock.tick(fps)
