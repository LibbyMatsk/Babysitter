import pygame
import sys
import entering_screen
import show_schedule
import Schedule


current_user = ""
schedule = Schedule.create_schedule()


def main():
    pygame.init()
    while True:
        pygame.display.update()
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
                    elif entering_screen.create_volunteer_button().collidepoint(event.pos):
                        print("volunteer selected")
                        current_user = "volunteer"
                        show_schedule.show_table_screen(schedule)


        pygame.display.update()







if __name__ == "__main__":
    main()