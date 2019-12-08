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
        self.dx = random.choice(ball_movement)
        self.dy = random.choice(ball_movement)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move(self, window):
        self.x += self.dx
        self.y += self.dy

        # Collision with the Paddles
        # Player 1
        if (ball.x < paddle1.x + paddle1.width) and (ball.y < paddle1.y + 65 and ball.y > paddle1.y - 65):
            ball.dx *= -1

        # Player 2
        if (ball.x > paddle2.x - paddle2.width) and (ball.y < paddle2.y + 65 and ball.y > paddle2.y - 65):
            ball.dx *= -1

        # Collision witht the Walls
        # Top Wall
        if ball.y <= (top_wall.y + top_wall.height):
            ball.dy *= -1

        # Bottom Wall
        if ball.y >= (bottom_wall.y - bottom_wall.height):
            ball.dy *= -1

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
    window.fill((0, 0, 0))
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
top_wall = lines(0, 35, 600, 15)
bottom_wall = lines(0, 365, 600, 15)
half_court = lines(300, 35, 3, 330)
half_court_circle = circles(300, 205, 70, 1)
paddle1 = player(30, 170, 10, 75)
paddle2 = player(565,170,10, 75)
ball_movement = [-10, 10]
ball = ball(350, 250, 15, 15)



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

pygame.quit()
