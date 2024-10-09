import pygame
import sys
import Consts

pygame.init()

screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
pygame.display.set_caption("Babysitter Matching Platform")
screen.fill(Consts.BACKGROUND_COLOR)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_hello_text():
    message = "Welcome To SitterFinder!"
    draw_message(message, 20, Consts.HELLO_COLOR,
                 (300, Consts.WINDOW_HEIGHT // 4))


def draw_welcome_screen():
    draw_hello_text()





