import pygame

#######################################################################
# drawText
# Input:
# - font: Font (pygame Font Object)
# - text: User Text (String)
# - color: Color of button background (Pygame color Object or RGB Tuple)
# - Screen x, y Position (int)
########################################################################


def drawText(win, font, text, color, x, y):
    winner_text = font.render(text, 1, color)
    win.blit(winner_text, (x, y))


#######################################################################
# button
# Input:
# - color: Color of button background (Pygame color Object or RGB Tuple)
# - x: Screen x position (int)
# - y: Screen y position (int)
# - width: Width of button in px (int)
# - height: Height of button in px (int)
# - font_size: size of font for button in px (int)
# - text: User Text (string)
########################################################################


class button():
    def __init__(self, color, x, y, width, height, font_size, text='',):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y -
                             2, self.width+4, self.height+4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y,
                         self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                     self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
