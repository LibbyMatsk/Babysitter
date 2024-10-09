# button.py
import pygame
import Consts
class Button:
    def __init__(self, text, font_size, color, hover_color, position, size):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.hover_color = hover_color
        self.position = position
        self.size = size
        self.font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

    def draw(self, surface):
        # Check if the mouse is over the button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        # Render the text and place it in the center of the button
        text_surface = self.font.render(self.text, True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        return self.rect.collidepoint(mouse_pos) and mouse_click[0]  # Left mouse button
