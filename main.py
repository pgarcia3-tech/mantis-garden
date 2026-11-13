#BASIC PYGAME WINDOW, GRID
import pygame
import sys
import random
import math

import TTTbackend

#initialize pygame
pygame.init()
clock = pygame.time.Clock()

#window dimensions
WIDTH = 900
HEIGHT = 900

#display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# cell size in grid
CELL_SIZE = 200
BOARD_SIZE= CELL_SIZE * 3
board_x = (WIDTH - BOARD_SIZE)//2
board_y = 150

#fonts
title_font = pygame.font.SysFont("jokerman", 48, bold=True)
font = pygame.font.SysFont(None, 100)
med_font = pygame.font.SysFont("consolas", 18, bold=True)
small_font = pygame.font.SysFont("consolas", 26)

#import ladybug and beetle drawings
ladybug_img = pygame.image.load("ladybug.png").convert_alpha()
beetle_img = pygame.image.load("beetle.png").convert_alpha()
mantis_img = pygame.image.load("mantis.png").convert_alpha()
cloud_img = pygame.image.load("cloud.png").convert_alpha()
caterpillar_img = pygame.image.load("caterpillar.png").convert_alpha()
wasp_img = pygame.image.load("wasp.png").convert_alpha()
house_img = pygame.image.load("mantis_house.png").convert_alpha()

#resize
ladybug_img = pygame.transform.scale(ladybug_img, (100, 100))
beetle_img = pygame.transform.smoothscale(beetle_img, (100 ,100 ))
mantis_img = pygame.transform.smoothscale(mantis_img, (500,500))
cloud_img = pygame.transform.scale(cloud_img, (70, 70))
caterpillar_img = pygame.transform.smoothscale(caterpillar_img, (110, 45))
wasp_img = pygame.transform.smoothscale(wasp_img, (85, 65))
house_img = pygame.transform.scale(house_img, (210, 210))
clouds = [
    {"x": 20, "y": 5, "speed": 0.15, "phase": 0},
    {"x": 180, "y": 35, "speed": 0.20, "phase": 1.5},
    {"x": 350, "y": 10, "speed": 0.25, "phase": 3},
    {"x": 520, "y": 40, "speed": 0.18, "phase": 4.5},
    {"x": 690, "y": 5, "speed": 0.30, "phase": 2},
]
#cloud_speed = 0.3

#ladybug celebration
celebration_ladybugs = []
for i in range(40):
    celebration_ladybugs.append([
        random.randint(0, WIDTH - 50),
        random.randint(-300, 0),
        random.randint(6, 12)
    ])

#thunderstorm
storm_active = False
storm_end_time = 0

#scarab swarm 
scarab_swarm_x = -400


def draw_grid():
    # background 
    # screen.fill((117, 170, 255))
    # Draw nine grassy garden plots
    for row in range(3):
        for col in range(3):
            x = board_x + col * CELL_SIZE
            y = board_y + row * CELL_SIZE
            if (row + col) % 2 == 0:
                grass_color = (125, 175, 95)
            else:
                grass_color = (140, 190, 105)
            
            pygame.draw.rect(
                screen,
                grass_color,
                (x, y, CELL_SIZE, CELL_SIZE)
                )


    # # vertical lines
    # for i in range(1, 3):
    #     pygame.draw.line(
    #         screen,
    #         (30,90,30), # black color
    #         (board_x + i * CELL_SIZE, board_y), # start 
    #         (board_x + i * CELL_SIZE, board_y + BOARD_SIZE), # end 
    #         5 # thickness
    #     )

    # # horizontal lines
    # for i in range(1, 3):
    #     pygame.draw.line(
    #         screen,
    #         (30,90,30),
    #         (board_x, board_y + i * CELL_SIZE),
    #         (board_x + BOARD_SIZE, board_y + i * CELL_SIZE),
    #         5
    #     )

def draw_flower(x, y, color):
    pixel = 5

    # Stem
    pygame.draw.rect(
        screen, (45, 110, 45),
        (x, y + pixel, pixel, pixel * 3)
    )

    # Four petals
    pygame.draw.rect(screen, color, (x, y - pixel, pixel, pixel))
    pygame.draw.rect(screen, color, (x - pixel, y, pixel, pixel))
    pygame.draw.rect(screen, color, (x + pixel, y, pixel, pixel))
    pygame.draw.rect(screen, color, (x, y + pixel, pixel, pixel))

    # Yellow center
    pygame.draw.rect(screen, (255, 220, 90), (x, y, pixel, pixel))

def draw_marks(board):
        #draw X and O on the grid 

        for row in range(3):
            for col in range(3):
                mark = board[row][col]
                if mark != "": #if mark isnt empty

                    # text = font.render(mark, True, color)
                    x = board_x + col * CELL_SIZE + CELL_SIZE // 2 - 50
                    y = board_y + row * CELL_SIZE + CELL_SIZE // 2 - 50

                    if mark == "X":
                        screen.blit(ladybug_img, (x, y))
                    else:
                        screen.blit(beetle_img, (x, y))

def draw_restart_button():
    # button_color = (170, 145, 200)

    button_width = 200
    button_height = 40

    button_x = (WIDTH - button_width) // 2
    button_y = 825
    
    # Shadow directly behind the button
    # Shadow cast directly downward
    pygame.draw.rect(
        screen,
        (110, 90, 135),
        (button_x, button_y + 3, button_width, button_height)
        )
    # Lavender button
    pygame.draw.rect(
        screen,
        (170, 145, 200),
        (button_x, button_y, button_width, button_height)
        )

    # Thick, dark outline
    pygame.draw.rect(
        screen,
        (45, 35, 60),
        (button_x, button_y, button_width, button_height),
        3
        )

    # Light highlight along the top
    pygame.draw.line(
        screen,
        (225, 205, 245),
        (button_x + 4, button_y + 4),
        (button_x + button_width - 5, button_y + 4),
        3
        )

    # pygame.draw.rect(
    #     screen,
    #     button_color,
    #     (button_x, button_y, button_width, button_height),
    #     border_radius=5
    # )

    # pygame.draw.rect(
    #     screen,
    #     (75, 55, 100),
    #     (button_x, button_y, button_width, button_height),
    #     2,
    #     border_radius=5
    # )

    text = small_font.render("THUNDER", False, (255, 225, 90))

    screen.blit(
        text,
        (
            button_x + (button_width - text.get_width()) // 2,
            button_y + (button_height - text.get_height()) // 2
        )
    )

def draw_title():
    title = title_font.render("Tic Tac Toe", False, (255, 225, 90))

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 25))
    #mantis image - he wants YOU to protect his garden
    
 
#status at the bottom!
def draw_status():
    if TTTbackend.winner == "X":
        message = "Ladybugs win :D "
    elif TTTbackend.winner == "O":
        message = "Scarabs feast tonight >:D "
    elif TTTbackend.winner == "Tie":
        message = "The garden rests..."
    else:
        message = "Defend Old Mr. Mantis' Garden"
    status_text = med_font.render(message, True, (190, 75, 110))
    screen.blit(status_text, (WIDTH // 2 - status_text.get_width() // 2, 95))

    # Scoreboard background
    pygame.draw.rect(
        screen,
        (255, 240, 200),
        (155, 765, 590, 45)
        )

    # Pixel-style border
    pygame.draw.rect(
        screen,
        (65, 90, 55),
        (155, 765, 590, 45),
        3
        )

    # Scoreboard text
    score_text = small_font.render(
        f"Ladybugs: {TTTbackend.player_score}   Scarabs: {TTTbackend.computer_score}   Ties: {TTTbackend.ties}",
        False,
        (65, 90, 55)
        )

    screen.blit(
        score_text,
        score_text.get_rect(center=(WIDTH // 2, 787))
        )

#cloud for decoration

def draw_cloud():
    time = pygame.time.get_ticks() / 1000
    for cloud in clouds:
        bobbing = 5 * math.sin(
            (2 * math.pi / 4) * time + cloud["phase"]
            )
        
        screen.blit(
            cloud_img, (cloud["x"], cloud["y"] + bobbing)
            )
        cloud["x"] -= cloud["speed"]
        
        if cloud["x"] < -cloud_img.get_width():
            cloud["x"] = WIDTH + random.randint(100, 400)

    
# ladybugs rain every time they win
def draw_ladybug_celebration():
    if TTTbackend.winner == "X":
        for bug in celebration_ladybugs:
            x, y, speed = bug

            screen.blit(
                pygame.transform.scale(ladybug_img, (45, 45)),
                (x, y)
            )

            bug[1] += speed

            if bug[1] > HEIGHT:
                bug[0] = random.randint(0, WIDTH - 45)
                bug[1] = random.randint(-200, -45)
                bug[2] = random.randint(6, 12)

# flashing red every time the scarabs win
def draw_scarab_swarm():
    global scarab_swarm_x
    if TTTbackend.winner == "O":
        for i in range(30):
            x = scarab_swarm_x + random.randint(0, 900)
            y = random.randint(90, 500)

            screen.blit(
                pygame.transform.scale(beetle_img, (60, 60)),
                (x, y)
            )

        scarab_swarm_x += 10
        if scarab_swarm_x > WIDTH:
            scarab_swarm_x = -500
    else:
        scarab_swarm_x = -500

#thunderstorm hard reset
def draw_thunderstorm():
    if storm_active:
        current_time = pygame.time.get_ticks()
        # flashing effect
        if (current_time // 80) % 2 == 0:
            screen.fill((255, 255, 120)) #yellow flash
        else:
            screen.fill((240, 240, 240))  # white flash

flower_colors = [
    (255, 190, 200),  # Pink
    (255, 245, 180),  # Pale yellow
    (220, 190, 255),  # Lavender
    (255, 255, 240)   # Cream
]

#drawing flowers
flowers = []

for row in range(3):
    for col in range(3):

        for i in range(4):

            x = board_x + col * CELL_SIZE + random.randint(20, CELL_SIZE - 30)
            y = board_y + row * CELL_SIZE + random.randint(20, CELL_SIZE - 40)

            color = random.choice(flower_colors)

            flowers.append({
                "x": x,
                "y": y,
                "color": color,
                "eaten": False
                })

def draw_flowers():
    for flower in flowers:
        if not flower["eaten"]:
            draw_flower(
                flower["x"],
                flower["y"],
                flower["color"]
            )
       
        
       
def draw_wasp(x, y):
    # Wings
    pygame.draw.rect(screen, (230, 240, 255), (x + 10, y - 8, 12, 8))
    pygame.draw.rect(screen, (230, 240, 255), (x + 22, y - 8, 12, 8))

    # Body
    pygame.draw.rect(screen, (245, 200, 40), (x, y, 40, 16))

    # Black stripes
    pygame.draw.rect(screen, (35, 30, 25), (x + 10, y, 6, 16))
    pygame.draw.rect(screen, (35, 30, 25), (x + 24, y, 6, 16))

    # Eye
    pygame.draw.rect(screen, (20, 20, 20), (x + 34, y + 4, 4, 4))

    # Stinger
    pygame.draw.polygon(
        screen,
        (35, 30, 25),
        [(x, y + 5), (x - 8, y + 8), (x, y + 11)]
    )

def draw_caterpillar(x, y):
    # Body segments
    for i in range(5):
        pygame.draw.rect(
            screen,
            (95, 165, 65),
            (x + i * 12, y, 14, 18)
        )

    # Head
    pygame.draw.rect(
        screen,
        (135, 195, 75),
        (x + 60, y - 4, 18, 22)
    )

    # Eye
    pygame.draw.rect(
        screen,
        (25, 45, 20),
        (x + 72, y + 2, 4, 4)
    )

    # Tiny legs
    for i in range(5):
        pygame.draw.rect(
            screen,
            (55, 110, 45),
            (x + i * 12 + 4, y + 16, 5, 7)
        )

    # Antennae
    pygame.draw.line(
        screen,
        (55, 110, 45),
        (x + 65, y - 4),
        (x + 62, y - 12),
        3
    )
#wasp and caterpillar
wasp_x = -50
wasp_y = 350
wasp_speed = 3

wasp_active = False
next_wasp_time = pygame.time.get_ticks() + random.randint(15000, 40000)

caterpillar_x = -90
caterpillar_y = 500
caterpillar_speed = 0.8
caterpillar_active = False
next_caterpillar_time = pygame.time.get_ticks() + random.randint(20000, 50000)
caterpillar_nibbling_until = 0


def caterpillar_eat_flower():
    global caterpillar_nibbling_until
    for flower in flowers:
        if flower["eaten"]:
            continue

        # Approximate position of the caterpillar's head
        head_x = caterpillar_x + 100
        head_y = caterpillar_y + 25 + math.sin(pygame.time.get_ticks() / 180) * 3

        distance_x = abs(head_x - flower["x"])
        distance_y = abs(head_y - flower["y"])

        # Check whether a flower is nearby
        if distance_x < 15 and distance_y < 15:
            if random.random() < 0.02:
                flower["eaten"] = True
                caterpillar_nibbling_until = pygame.time.get_ticks() + 1200
                break
# game loop, runs continuously
while True:
    TTTbackend.update_computer()
    TTTbackend.update_reset()
    screen.fill((117, 170, 255))
    screen.blit(mantis_img, (-120,-50))
    draw_grid()
    draw_flowers()
    draw_marks(TTTbackend.board)
    current_time = pygame.time.get_ticks()
    # Start a random encounter
    if not wasp_active and current_time >= next_wasp_time:
        wasp_active = True
        wasp_x = -50
        wasp_y = random.randint(board_y + 30, board_y + BOARD_SIZE - 50)
        # Move the wasp while it's visiting
    if wasp_active:
        wasp_x += wasp_speed
        wobble = math.sin(current_time / 150) * 12
        screen.blit( wasp_img, (int(wasp_x), int(wasp_y + wobble))
                    )

        # End encounter when the wasp leaves the screen
        if wasp_x > WIDTH:
            wasp_active = False
            next_wasp_time = current_time + random.randint(15000, 40000)
    # Caterpillar random encounter
    current_time = pygame.time.get_ticks()

    if not caterpillar_active and current_time >= next_caterpillar_time:
        caterpillar_active = True
        caterpillar_x = -90
        caterpillar_y = random.randint(
            board_y + 30,
            board_y + BOARD_SIZE - 50
            )

    if caterpillar_active:
        if current_time >= caterpillar_nibbling_until:
            caterpillar_x += caterpillar_speed
            caterpillar_eat_flower()

        crawl = math.sin(current_time / 180) * 3
        screen.blit(
            caterpillar_img,
            (int(caterpillar_x), int(caterpillar_y + crawl))
            )

        if caterpillar_x > WIDTH:
           caterpillar_active = False
           next_caterpillar_time = current_time + random.randint(20000, 50000)

    screen.blit(house_img, (770, 750))    
    draw_cloud()
    draw_title()
    draw_status()
    draw_restart_button()
    draw_ladybug_celebration()
    draw_scarab_swarm()
    draw_thunderstorm()
    
# check for event, closing window, etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 350 <= x <= 550 and 825 <= y <= 865:
                storm_active = True
                storm_end_time = pygame.time.get_ticks() + 800
                TTTbackend.reset_all()
            else:
                TTTbackend.handle_click(event.pos)
    current_time = pygame.time.get_ticks()
    if storm_active and current_time >= storm_end_time:
        storm_active = False


# update display
    pygame.display.update()
    clock.tick(60)