import pygame
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 800
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
FONT_NAME = "David"

CELL_WIDTH = 150
CELL_HEIGHT = 40
TABLE_X = 50
TABLE_Y = 100  # Table start position

# Colors

BLACK = (0, 0, 0)
HEADER_COLOR = (173, 216, 230)
ROW_COLOR = (240, 248, 255)

BACKGROUND_COLOR = (255,204,255)
HELLO_COLOR = (32, 32, 32)

VOLUNTEER_IMAGE = pygame.image.load('volunteer.jpg')
VOLUNTEER_IMAGE = pygame.transform.smoothscale(VOLUNTEER_IMAGE, (70, 70))
LOGO_IMAGE = pygame.image.load('logo2.png')
LOGO_IMAGE = pygame.transform.smoothscale(LOGO_IMAGE, (100, 90))
PARENT_IMAGE = pygame.image.load('download.png')
PARENT_IMAGE = pygame.transform.smoothscale(PARENT_IMAGE, (70, 50))