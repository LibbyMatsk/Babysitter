import pygame
import sys
import entering_screen


def main():
    pygame.init()
    while True:
        pygame.display.update()
        entering_screen.draw_welcome_screen()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()