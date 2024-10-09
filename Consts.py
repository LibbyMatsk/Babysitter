import pygame
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 800
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
FONT_NAME = "David"


BACKGROUND_COLOR = (255,204,255)
HELLO_COLOR = (32, 32, 32)

VOLUNTEER_IMAGE = pygame.image.load('volunteer.jpg')
VOLUNTEER_IMAGE = pygame.transform.smoothscale(VOLUNTEER_IMAGE, (70, 70))
LOGO_IMAGE = pygame.image.load('logo2.png')
LOGO_IMAGE = pygame.transform.smoothscale(LOGO_IMAGE, (100, 90))
PARENT_IMAGE = pygame.image.load('download.png')
PARENT_IMAGE = pygame.transform.smoothscale(PARENT_IMAGE, (70, 50))