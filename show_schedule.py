
import pygame
import sys
import Schedule
import Consts

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

# Data for babysitter requests

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_title():
    message = "Babysitting Schedule".upper()
    draw_message(message, 50, Consts.HELLO_COLOR,
                 (300, 50))

pygame.init()
# Font
font = pygame.font.SysFont('Arial', 20)

def draw_cell(text, x, y, width, height, color=Consts.WHITE, border_color=Consts.BLACK):
    pygame.draw.rect(screen, color, (x, y, width, height))  # Fill color
    pygame.draw.rect(screen, border_color, (x, y, width, height), 2)  # Border
    text_surface = font.render(str(text), True, Consts.BLACK)  # Convert text to string
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


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_request_button_text(x, y):
    message = "Add Request"
    draw_message(message, 30, Consts.HELLO_COLOR,
                 (x,y))
def create_request_button():
    return pygame.Rect(210, 300, 370, 80)

def show_table_for_volunteer(schedule):
    screen.fill(Consts.WHITE)
    rows_headers = table_headers_and_rows(schedule)
    draw_table(rows_headers[0], rows_headers[1])
    draw_title()
    pygame.display.update()

def show_table_screen_for_parent(schedule):
    screen.fill(Consts.WHITE)
    rows_headers = table_headers_and_rows(schedule)
    draw_table(rows_headers[0], rows_headers[1])
    request_button = create_request_button()
    pygame.draw.rect(screen, (255, 255, 255), request_button)
    draw_request_button_text(300, 22)
    draw_title()
    pygame.display.update()

def update_schedule(schedule, newRequest):
    Schedule.add_request_line(schedule, newRequest)
    show_table_screen_for_parent(schedule)




# def main():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
#                 sys.exit()
#
#         # Fill screen with white background
#         screen.fill(WHITE)
#
#         # Draw the table
#         draw_table()
#
#         pygame.display.update()
#
# if __name__ == "__main__":
#     main()
