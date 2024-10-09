import pygame
import sys
import entering_screen

current_user = ""

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

                        current_user = "Parent"
                    elif entering_screen.create_volunteer_button().collidepoint(event.pos):
                        print("volunteer selected")
                        current_user = "volunteer"





if __name__ == "__main__":
    main()