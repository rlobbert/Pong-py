# A Pong clone built using Pygame
import pygame
import random

pygame.init()

################ Game window settings ###############
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pong")
window.fill((0, 0, 0))
clock = pygame.time.Clock()

############### Game Classes ###############

# Players Pads
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 20

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move_paddle(self, window):
        #Player 1 Move and Collision
        if keys[pygame.K_w] and paddle1.y > (top_wall.y + top_wall.height):
            paddle1.y -= paddle1.velocity
        if keys[pygame.K_s] and (paddle1.y + paddle1.height) < (bottom_wall.y - bottom_wall.height):
            paddle1.y += paddle1.velocity

        #Player 2 Move and Collision
        if keys[pygame.K_i] and paddle2.y > (top_wall.y + top_wall.height):
            paddle2.y -= paddle2.velocity
        if keys[pygame.K_k] and (paddle2.y + paddle2.height) < (bottom_wall.y - bottom_wall.height):
            paddle2.y += paddle2.velocity

# Ball
class ball(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = -10#random.choice(ball_movement)
        self.dy = -10#random.choice(ball_movement)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move(self, window):
        self.x += self.dx
        self.y += self.dy

# Walls and Lines
class lines(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

# Half Court Circle
class circles(object):
    def __init__(self, x, y, radius, width):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius, self.width)


############### Game Functions ###############
def redraw_game_window():
    player1_score = font.render('P1: ' + str(p1_score), 1, (255, 255, 255))
    player2_score = font.render('P2: ' + str(p2_score), 1, (255, 255, 255))

    window.fill((0, 0, 0))
    window.blit(player1_score, (10, 10))
    window.blit(player2_score, (490, 10))
    top_wall.draw(window)
    bottom_wall.draw(window)
    half_court.draw(window)
    half_court_circle.draw(window)
    paddle1.draw(window)
    paddle2.draw(window)
    paddle1.move_paddle(window)
    ball.draw(window)
    ball.move(window)
    pygame.display.update()

############### Variables ###############
run = True
font = pygame.font.SysFont('comicsans', 30)
top_wall = lines(0, 35, 600, 15)
bottom_wall = lines(0, 365, 600, 15)
half_court = lines(300, 35, 3, 330)
half_court_circle = circles(300, 205, 70, 1)
paddle1 = player(30, 170, 10, 75)
paddle2 = player(565,170,10, 75)
ball_movement = [-10, 10]
ball = ball(350, 250, 15, 15)
p1_score = 0
p2_score = 0


############### Main Game ###############

while run:
    # Main game Variables
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()
    redraw_game_window()

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Scoring System
    # Player 1
    if ball.x > 590:
        ball.x = 350
        ball.y = 250
        ball.dx *= -1
        p1_score += 1

    # Player 2
    if ball.x < 0:
        ball.x = 350
        ball.y = 250
        ball.dx *= -1
        p2_score += 1

    # Collision with the Paddles
    # Player 1
    if ball.x < 40 and (ball.y > paddle1.y - 30 and ball.y < paddle1.y + 75):
        ball.dx *= -1

    # Player 2
    if (ball.x < 565 and ball.x > 550) and (ball.y > paddle2.y - 30 and ball.y < paddle2.y + 75):
        ball.dx *= -1

    # Collision with the Walls
    # Top Wall
    if ball.y <= (top_wall.y + top_wall.height):
        ball.dy *= -1

    # Bottom Wall
    if ball.y >= (bottom_wall.y - bottom_wall.height):
        ball.dy *= -1

pygame.quit()
