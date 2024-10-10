import pygame
import sys
import Schedule
import Consts


pygame.init()
def table_headers_and_rows(schedule):
    '''

    :param schedule:
    :return: rows and headers in schedule
    '''
    headers = []
    rows = []
    for i in schedule.keys():
        headers.append(i)

    for i in range(len(schedule["parent name"])):
        row_i = []
        for j in schedule.keys():
            row_i.append(schedule[j][i])
        rows.append(row_i)
    return rows, headers


screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
pygame.display.set_caption("Babysitter Requests")


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_title():
    message = "Babysitting Schedule".upper()
    draw_message(message, 50, Consts.HELLO_COLOR,
                 (300, 50))

# Font
font = pygame.font.SysFont(Consts.FONT_NAME, 20)

def draw_cell(text, x, y, width, height, color=Consts.WHITE, border_color=Consts.BLACK):
    pygame.draw.rect(screen, color, (x, y, width, height))  # Fill color
    pygame.draw.rect(screen, border_color, (x, y, width, height), 2)  # Border
    text_surface = font.render(text, True, Consts.BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def draw_table(rows, headers):
    # Draw header
    for col_index, header in enumerate(headers):
        x = Consts.TABLE_X + col_index * Consts.CELL_WIDTH
        draw_cell(header, x, Consts.TABLE_Y, Consts.CELL_WIDTH, Consts.CELL_HEIGHT, Consts.HEADER_COLOR)

    # Draw rows
    for row_index, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            x = Consts.TABLE_X + col_index * Consts.CELL_WIDTH
            y = Consts.TABLE_Y + (row_index + 1) * Consts.CELL_HEIGHT  # Below the header row
            draw_cell(cell, x, y, Consts.CELL_WIDTH, Consts.CELL_HEIGHT, Consts.ROW_COLOR)

def show_table_screen(schedule):
    screen.fill(Consts.WHITE)
    rows_headers = table_headers_and_rows(schedule)
    draw_table(rows_headers[0], rows_headers[1])
    draw_title()
    pygame.display.update()

def update_schedule(schedule, newRequest):
    Schedule.add_request_line(schedule, newRequest)
    show_table_screen(schedule)
