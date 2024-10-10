import pygame
import sys
import entering_screen
import show_schedule
import Schedule
import Screen
import request1



current_user = ""
schedule = Schedule.schedule = Schedule.create_schedule()


def main():
    pygame.init()
    is_display_entering_screen = True

    while True:
        pygame.display.update()
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
                        show_schedule.show_table_screen_for_parent(schedule)
                        is_display_entering_screen = False
                        current_user = "Parent"

                    elif entering_screen.create_volunteer_button().collidepoint(event.pos):
                        print("Volunteer selected")
                        current_user = "Volunteer"
                        show_schedule.show_table_for_volunteer(schedule)
                        is_display_entering_screen = False

                    elif  show_schedule.create_request_button().collidepoint(event.pos):
                        print("request selected")
                        request1.get_request()
                        show_schedule.show_table_screen_for_parent(schedule)
                        is_display_entering_screen = False
                        # current_user = "Parent"


                    pygame.display.update()


if __name__ == "__main__":
    main()