# Pong 0.1
# A Pong clone built using Pygame

import pygame

pygame.init()

# Game window settings
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pong - version 0.1")
window.fill((0, 0, 0))
clock = pygame.time.Clock()

# Game Classes

# Walls and Lines
class lines(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))


# Half Court Circle and Ball
class circles(object):
    def __init__(self, x, y, radius, width):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius, self.width)


# Game Functions
def redraw_game_window():
    window.fill((0, 0, 0))
    top_wall.draw(window)
    bottom_wall.draw(window)
    half_court.draw(window)
    half_court_circle.draw(window)
    paddle1.draw(window)
    paddle2.draw(window)
    pygame.display.update()



# Variables
run = True
top_wall = lines(0, 35, 600, 15)
bottom_wall = lines(0, 365, 600, 15)
half_court = lines(300, 35, 3, 330)
half_court_circle = circles(300, 205, 70, 1)
paddle1 = lines(30, 170, 10, 75)
paddle2 = lines(565,170,10, 75)


# Main Game

while run:
    # Main game Variables
    pygame.time.delay(100)
    redraw_game_window()

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
