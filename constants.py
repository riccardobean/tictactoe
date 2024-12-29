# Copyright (c) 2024 Riccardo Bean. All Rights Reserved.
# Unauthorized use, modification, or distribution of this software is prohibited.

width = 600
HEIGHT = 800
height = 600
line_width = 15
BOARD_ROWS = 3
BOARD_COLUMNS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
BG_COLOUR = (28, 170, 156)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOUR = (23, 145, 135)
CIRCLE_COLOUR = (239, 231, 200)
CROSS_COLOUR = (66, 66, 66)
DARK_CROSS = (40, 40, 40)
DARK_CIRCLE = (219, 211, 171)

try:
    import pygame
    pygame.init()
    font = pygame.font.SysFont(None, 60)
    score_font = pygame.font.SysFont(None, 100)
    credits_font = pygame.font.SysFont(None, 30)

    LOGO_ICON = pygame.image.load('assets/logo.png')
    HOME_ICON = pygame.image.load('assets/home.png')
    RESTART_ICON = pygame.image.load('assets/undo-arrow.png')


except ModuleNotFoundError:
    import os
    file = open("log/notfounderror.txt", "w")
    file.write("Your program could not be executed.\nConsider downloading the required files again as a zip file or making sure the files are in the correct folder.")
    file.close()
    os.startfile("log\\notfounderror.txt")

except FileNotFoundError:
    import os
    file = open("log/notfounderror.txt", "w")
    file.write("Your program could not be executed.\nConsider downloading the required files again as a zip file or making sure the files are in the correct folder.")
    file.close()
    os.startfile("log\\notfounderror.txt")
