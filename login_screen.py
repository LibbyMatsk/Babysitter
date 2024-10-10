import pygame
import sys
import Consts
import Button
import Screen


pygame.init()


screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
pygame.display.set_caption("Babysitter Matching Platform")

def create_upper_rect():
    return pygame.Rect(0, 0, 370, 80)



def draw_login_screen():
    screen.fill(Consts.WHITE)


