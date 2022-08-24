import pygame
pygame.init()


WIDTH, HEIGHT = 900, 500
CARD_WIDTH, CARD_HEIGHT = 100, 150
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 75
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WINNER_FONT = pygame.font.SysFont('comicsans', 50)

# Colors
GREEN = (56, 150, 0)
WINNER_YELLOW = (168, 181, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (242, 245, 66)
WHITE = (255, 255, 255)
PURPLE = (89, 0, 106)
PINK = (202, 0, 233)
CYAN = (0, 255, 126)
ORANGE = (255, 150, 0)

# FPS
FPS = 15
clock = pygame.time.Clock()

# FONTS
WINNER_FONT = pygame.font.SysFont('comicsans', 60)
MONEY_FONT = pygame.font.SysFont('comicsans', 20)
GAME_OVER_FONT = pygame.font.SysFont('comicsans', 80)
