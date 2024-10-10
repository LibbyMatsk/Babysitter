import pygame
import sys
import entering_screen
import show_schedule
import Schedule
import Screen


current_user = ""

schedule = Schedule.create_schedule()


def main():
    is_active = False
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = entering_screen.create_input_rect()

    pygame.init()
    is_display_entering_screen = True
    while True:
        if is_display_entering_screen:
            entering_screen.draw_welcome_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if entering_screen.create_parent_button().collidepoint(event.pos):
                        print("Parent selected")
                        show_schedule.show_table_screen(schedule)

                        current_user = "Parent"
                    if entering_screen.create_volunteer_button().collidepoint(event.pos):
                        print("volunteer selected")
                        current_user = "volunteer"
                        show_schedule.show_table_screen(schedule)
                    is_display_entering_screen = False

                    if input_rect.collidepoint(event.pos):
                        is_active = True
                    else:
                        is_active = False

            if event.type == pygame.KEYDOWN:
                if event.key() == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

                else:
                    user_text += event.unicode

        if is_active:
            color = entering_screen.color_active
        else:
            color = entering_screen.color_passive
        pygame.draw.rect(entering_screen.screen, color, input_rect)
        text_surface = base_font.render( entering_screen.user_text, True, (255, 255, 255))
        entering_screen.screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.update()













if __name__ == "__main__":
    main()