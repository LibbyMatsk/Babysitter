import pygame
import sys
import Consts
import Button
import Screen


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
    draw_message(message, 50, Consts.HELLO_COLOR,
                 (130, Consts.WINDOW_HEIGHT // 4))

def draw_question_text():
    message = "Are you a parent or a volunteer?"
    draw_message(message, 30, Consts.HELLO_COLOR,
                 (210, Consts.WINDOW_HEIGHT // 4  + 45))

def draw_button_volunteer_text(x, y):
    message = "I'm a volunteer"
    draw_message(message, 30, Consts.HELLO_COLOR,
                 (x,y))

def draw_button_parent_text(x, y):
    message = "I'm a parent"
    draw_message(message, 30, Consts.HELLO_COLOR,
                 (x,y))


def create_parent_button():
    return pygame.Rect(210, 300, 370, 80)
def create_volunteer_button():
    return pygame.Rect(210, 400, 370, 80)


def draw_welcome_screen():
    screen.fill(Consts.BACKGROUND_COLOR)
    parent_button = create_parent_button()
    volunteer_button = create_volunteer_button()

    pygame.draw.rect(screen, (255,255,255), parent_button)
    pygame.draw.rect(screen, (255,255,255), volunteer_button)

    draw_button_volunteer_text(280, 425)
    draw_button_parent_text(280, 325)

    screen.blit(Consts.VOLUNTEER_IMAGE, (210, 405))
    screen.blit(Consts.PARENT_IMAGE, (210, 315))
    screen.blit(Consts.LOGO_IMAGE, (340, 60))

    draw_hello_text()
    draw_question_text()


    pygame.display.update()





