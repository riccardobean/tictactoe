# Copyright (c) 2024 Riccardo Bean. All Rights Reserved.
# Unauthorized use, modification, or distribution of this software is prohibited.

try:
    import random
    import pygame
    import sys
    import numpy as np
    import os
    from pygame.locals import *
    from constants import *

    pygame.init()
    screen = pygame.display.set_mode((width, HEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    pygame.display.set_icon(LOGO_ICON)

    board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))
    file = open("log/error.txt", "w")
    file.close()


    def draw_lines():
        pygame.draw.line(screen, LINE_COLOUR, (0, 200), (600, 200), line_width)
        pygame.draw.line(screen, LINE_COLOUR, (0, 400), (600, 400), line_width)
        pygame.draw.line(screen, LINE_COLOUR, (200, 0), (200, 600), line_width)
        pygame.draw.line(screen, LINE_COLOUR, (400, 0), (400, 600), line_width)
        pygame.draw.line(screen, RED, (0, 600), (600, 600), 10)


    def draw_figures():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLUMNS):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, CIRCLE_COLOUR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                       CIRCLE_WIDTH)
                elif board[row][col] == 2:
                    pygame.draw.line(screen, CROSS_COLOUR, (col * 200 + SPACE, row * 200 + 200 - SPACE),
                                     (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOUR, (col * 200 + SPACE, row * 200 + SPACE),
                                     (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


    def mark_square(row, col, player):
        board[row][col] = player


    def available_square(row, col):
        if board[row][col] == 0:
            return True
        else:
            return False


    def get_empty_squares():
        empty_squares = []
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLUMNS):
                if available_square(row, col):
                    empty_squares.append((row, col))
        return empty_squares


    def rand():
        empty_squares = get_empty_squares()
        index = random.randrange(0, len(empty_squares))
        return empty_squares[index]


    def check_win(player):
        for col in range(BOARD_COLUMNS):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                draw_vertical_winning_line(col, player)
                return True
        for row in range(BOARD_ROWS):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                draw_horizontal_winning_line(row, player)
                return True

        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_asc_diagonal(player)
            return True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desc_diagonal(player)
            return True

        return False


    def draw_vertical_winning_line(col, player):
        posX = col * 200 + 100

        if player == 1:
            colour = CIRCLE_COLOUR
        else:
            colour = CROSS_COLOUR

        pygame.draw.line(screen, colour, (posX, 15), (posX, height - 15), 15)


    def draw_horizontal_winning_line(row, player):
        posY = row * 200 + 100

        if player == 1:
            colour = CIRCLE_COLOUR
        else:
            colour = CROSS_COLOUR

        pygame.draw.line(screen, colour, (15, posY), (width - 15, posY), 15)


    def draw_asc_diagonal(player):
        if player == 1:
            colour = CIRCLE_COLOUR
        else:
            colour = CROSS_COLOUR
        pygame.draw.line(screen, colour, (15, height - 15), (width - 15, 15), 15)


    def draw_desc_diagonal(player):
        if player == 1:
            colour = CIRCLE_COLOUR
        else:
            colour = CROSS_COLOUR
        pygame.draw.line(screen, colour, (15, 15), (width - 15, height - 15), 15)


    def restart():
        screen.fill(BG_COLOUR)
        draw_lines()
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLUMNS):
                board[row][col] = 0


    def is_board_full():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLUMNS):
                if board[row][col] == 0:
                    return False
        return True


    def draw_text(text, font, colour, surface, x, y):
        textobj = font.render(text, 1, colour)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    def score(player, win1, win2):
        reset(win1, win2)
        if player == 1:
            pygame.draw.rect(screen, RED, pygame.Rect(40, 610, 170, 80))
        if player == 2:
            pygame.draw.rect(screen, RED, pygame.Rect(390, 610, 170, 80))
        pygame.draw.circle(screen, CIRCLE_COLOUR, (80, 650), 30, 8)
        pygame.draw.line(screen, CROSS_COLOUR, (495, 680), (545, 620), 10)
        pygame.draw.line(screen, CROSS_COLOUR, (545, 680), (495, 620), 10)
        win1TXT = str(win1)
        win2TXT = str(win2)
        screen.blit(score_font.render(win1TXT, True, CIRCLE_COLOUR), (130, 620))
        screen.blit(score_font.render(win2TXT, True, CROSS_COLOUR), (420, 620))


    def idiot_ai_score(player, win1, win2):
        idiot_ai_reset(win1, win2)
        if player == 1:
            pygame.draw.rect(screen, RED, pygame.Rect(40, 610, 170, 80))
        pygame.draw.circle(screen, CIRCLE_COLOUR, (80, 650), 30, 8)
        pygame.draw.line(screen, CROSS_COLOUR, (495, 680), (545, 620), 10)
        pygame.draw.line(screen, CROSS_COLOUR, (545, 680), (495, 620), 10)
        win1TXT = str(win1)
        win2TXT = str(win2)
        screen.blit(score_font.render(win1TXT, True, CIRCLE_COLOUR), (130, 620))
        screen.blit(score_font.render(win2TXT, True, CROSS_COLOUR), (420, 620))


    def idiot_ai_reset(win1, win2):
        pygame.draw.rect(screen, RED, pygame.Rect(40, 610, 170, 80))
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(390, 610, 170, 80))
        pygame.draw.circle(screen, CIRCLE_COLOUR, (80, 650), 30, 8)
        pygame.draw.line(screen, CROSS_COLOUR, (495, 680), (545, 620), 10)
        pygame.draw.line(screen, CROSS_COLOUR, (545, 680), (495, 620), 10)
        win1TXT = str(win1)
        win2TXT = str(win2)
        screen.blit(score_font.render(win1TXT, True, CIRCLE_COLOUR), (130, 620))
        screen.blit(score_font.render(win2TXT, True, CROSS_COLOUR), (420, 620))


    def reset(win1, win2):
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(40, 610, 170, 80))
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(390, 610, 170, 80))
        pygame.draw.circle(screen, CIRCLE_COLOUR, (80, 650), 30, 8)
        pygame.draw.line(screen, CROSS_COLOUR, (495, 680), (545, 620), 10)
        pygame.draw.line(screen, CROSS_COLOUR, (545, 680), (495, 620), 10)
        win1TXT = str(win1)
        win2TXT = str(win2)
        screen.blit(score_font.render(win1TXT, True, CIRCLE_COLOUR), (130, 620))
        screen.blit(score_font.render(win2TXT, True, CROSS_COLOUR), (420, 620))



    def home():
        click = False
        while True:
            screen.fill(BG_COLOUR)
            draw_text("Welcome!", score_font, CIRCLE_COLOUR, screen, 140, 250)
            pygame.draw.circle(screen, CIRCLE_COLOUR, (200, 120), 90, CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOUR, (330, 30), (470, 210), CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOUR, (470, 30), (330, 210), CROSS_WIDTH)
            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(65, 380, 220, 140)
            button2 = pygame.Rect(325, 400, 200, 100)
            button3 = pygame.Rect(75, 600, 200, 100)
            button4 = pygame.Rect(325, 600, 200, 100)
            pygame.draw.rect(screen, DARK_RED, button1)
            screen.blit(font.render("Play", True, CIRCLE_COLOUR), (130, 430))
            pygame.draw.rect(screen, DARK_CROSS, button2)
            screen.blit(font.render("Rules", True, CIRCLE_COLOUR), (370, 430))
            pygame.draw.rect(screen, DARK_CROSS, button3)
            screen.blit(font.render("Credits", True, CIRCLE_COLOUR), (100, 630))
            pygame.draw.rect(screen, DARK_CROSS, button4)
            screen.blit(font.render("Quit", True, CIRCLE_COLOUR), (380, 630))
            if button1.collidepoint((mx, my)):
                pygame.draw.rect(screen, RED, button1)
                screen.blit(font.render("Play", True, CIRCLE_COLOUR), (130, 430))
                if click:
                    restart()
                    game_page()
            if button2.collidepoint((mx, my)):
                pygame.draw.rect(screen, CROSS_COLOUR, button2)
                screen.blit(font.render("Rules", True, CIRCLE_COLOUR), (370, 430))
                if click:
                    rules()
            if button3.collidepoint((mx, my)):
                pygame.draw.rect(screen, CROSS_COLOUR, button3)
                screen.blit(font.render("Credits", True, CIRCLE_COLOUR), (100, 630))
                if click:
                    credits()
            if button4.collidepoint((mx, my)):
                pygame.draw.rect(screen, CROSS_COLOUR, button4)
                screen.blit(font.render("Quit", True, CIRCLE_COLOUR), (380, 630))
                if click:
                    os.remove("log/error.txt")
                    pygame.quit()
                    sys.exit()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        os.remove("log/error.txt")
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()


    def rules():
        click3 = False
        while True:
            screen.fill(BG_COLOUR)
            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(50, 50, 64, 64)
            screen.blit(HOME_ICON, (50, 50))
            screen.blit(score_font.render("How to play?", True, CROSS_COLOUR), (150, 55))

            screen.blit(credits_font.render("There are three game modes:", True, CIRCLE_COLOUR), (45, 155))
            screen.blit(credits_font.render("     1) Multiplayer", True, CIRCLE_COLOUR), (45, 190))
            screen.blit(credits_font.render("     2) Easy AI", True, CIRCLE_COLOUR), (45, 210))
            screen.blit(credits_font.render("     3) Impossible AI", True, CIRCLE_COLOUR), (45, 230))

            screen.blit(credits_font.render("Your goal is to place three equal symbols on the", True, CIRCLE_COLOUR), (45, 300))
            screen.blit(credits_font.render("same line. The line can be vertical, horizontal, or", True, CIRCLE_COLOUR),(45, 330))
            screen.blit(credits_font.render("oblique. The first player to complete one line wins.", True, CIRCLE_COLOUR),(45, 360))

            screen.blit(credits_font.render("If you press the ESC key in any subpage you will be", True, CIRCLE_COLOUR),(45, 430))
            screen.blit(credits_font.render("brought to the homepage. The home symbol will also", True, CIRCLE_COLOUR),(45, 460))
            screen.blit(credits_font.render("take you to the homepage. If you press the ESC key", True, CIRCLE_COLOUR),(45, 490))
            screen.blit(credits_font.render("in the homepage you will exit the game. Remember,", True,CIRCLE_COLOUR), (45, 520))
            screen.blit(credits_font.render("your score is not saved. Thus, if you exit the game", True, CIRCLE_COLOUR),(45, 550))
            screen.blit(credits_font.render("your score will go back to zero.", True, CIRCLE_COLOUR),(45, 580))

            screen.blit(credits_font.render("If you want to learn more about the graphics, check", True, CIRCLE_COLOUR),(45, 650))
            screen.blit(credits_font.render('out the "Credits" subpage.', True, CIRCLE_COLOUR),(45, 680))

            screen.blit(credits_font.render('NOW, HAPPY GAME!', True, CROSS_COLOUR), (208, 730))

            if button1.collidepoint((mx, my)):
                if click3:
                    home()
            click3 = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os.remove("log/error.txt")
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        home()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click3 = True
            pygame.display.update()


    def credits():
        click4 = False
        while True:
            screen.fill(BG_COLOUR)
            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(50, 50, 64, 64)
            screen.blit(HOME_ICON, (50, 50))
            screen.blit(score_font.render("Credits", True, CROSS_COLOUR), (180, 60))
            screen.blit(credits_font.render("(c) Copyright 2024. All rights reserved.", True, CIRCLE_COLOUR), (45, 340))
            screen.blit(credits_font.render("Created by Riccardo Bean.", True, CIRCLE_COLOUR), (45, 400))
            screen.blit(credits_font.render("All icons were copyright-free during development.", True, CIRCLE_COLOUR), (45, 460))
            if button1.collidepoint((mx, my)):
                if click4:
                    home()
            click4 = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os.remove("log/error.txt")
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        home()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click4 = True
            pygame.display.update()


    def idiot_ai():
        win1 = 0
        win2 = 0
        draw_lines()
        player = 1
        click5 = False
        game_over = False
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(40, 610, 170, 80))
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(390, 610, 170, 80))
        while True:
            if not game_over:
                idiot_ai_score(player, win1, win2)
            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(50, 720, 64, 64)
            button2 = pygame.Rect(495, 720, 64, 64)
            screen.blit(HOME_ICON, (50, 720))
            screen.blit(RESTART_ICON, (495, 720))
            if button1.collidepoint((mx, my)):
                if click5:
                    home()
            if button2.collidepoint((mx, my)):
                if click5:
                    restart()
                    game_over = False
            click5 = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os.remove("log/error.txt")
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        home()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click5 = True
                if player == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                        mouseX = event.pos[0]
                        mouseY = event.pos[1]
                        if mouseY <= 600:
                            clicked_row = int(mouseY // 200)
                            clicked_col = int(mouseX // 200)
                            if available_square(clicked_row, clicked_col):
                                mark_square(clicked_row, clicked_col, 1)
                                if check_win(player):
                                    win1 = win1 + 1
                                    screen.blit(font.render("Human wins!", True, CIRCLE_COLOUR), (170, 730))
                                    game_over = True
                                    reset(win1, win2)
                                if is_board_full() and not game_over:
                                    screen.blit(font.render("Draw", True, RED), (255, 730))
                                    game_over = True
                                    reset(win1, win2)
                                player = 2
                                if not game_over:
                                    idiot_ai_score(2, win1, win2)
                elif player == 2:
                    if not is_board_full() and not game_over:
                        row, col = rand()
                        mark_square(row, col, 2)
                    if check_win(player):
                        win2 = win2 + 1
                        screen.blit(font.render("Robot wins!", True, CROSS_COLOUR), (180, 730))
                        game_over = True
                        reset(win1, win2)
                    if is_board_full() and not game_over:
                        screen.blit(font.render("Draw", True, RED), (255, 730))
                        game_over = True
                        reset(win1, win2)
                    player = 1
                    if not game_over:
                        idiot_ai_score(1, win1, win2)
                    draw_figures()
            pygame.display.update()


    def win_vertically(played, player):
        if not played and player == 2:
            if (board[0][0] == 2) and (board[1][0] == 2):
                row = 2
                col = 0
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][0] == 2) and (board[2][0] == 2) and not played:
                row = 1
                col = 0
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[1][0] == 2) and (board[2][0] == 2) and not played:
                row = 0
                col = 0
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][1] == 2) and (board[1][1] == 2) and not played:
                row = 2
                col = 1
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][1] == 2) and (board[2][1] == 2) and not played:
                row = 1
                col = 1
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[1][1] == 2) and (board[2][1] == 2) and not played:
                row = 0
                col = 1
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][2] == 2) and (board[1][2] == 2) and not played:
                row = 2
                col = 2
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[1][2] == 2) and (board[2][2] == 2) and not played:
                row = 0
                col = 2
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][2] == 2) and (board[2][2] == 2) and not played:
                row = 1
                col = 2
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if not played:
                row = 3
                col = 3
        return played, row, col


    def win_horizontally(played, player):
        if not played and player == 2:
            if (board[0][0] == 2) and (board[0][1] == 2):
                row = 0
                col = 2
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][0] == 2) and (board[0][2] == 2) and not played:
                row = 0
                col = 1
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][1] == 2) and (board[0][2] == 2) and not played:
                row = 0
                col = 0
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[1][0] == 2) and (board[1][1] == 2) and not played:
                row = 1
                col = 2
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[1][0] == 2) and (board[1][2] == 2) and not played:
                row = 1
                col = 1
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[1][1] == 2) and (board[1][2] == 2) and not played:
                row = 1
                col = 0
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[2][0] == 2) and (board[2][1] == 2) and not played:
                row = 2
                col = 2
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[2][1] == 2) and (board[2][2] == 2) and not played:
                row = 2
                col = 0
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[2][0] == 2) and (board[2][2] == 2) and not played:
                row = 2
                col = 1
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if not played:
                row = 3
                col = 3
        return played, row, col


    def win_obliquely(played, player):
        if not played and player == 2:
            if (board[0][0] == 2) and (board[1][1] == 2):
                row = 2
                col = 2
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][0] == 2) and (board[2][2] == 2) and not played:
                row = 1
                col = 1
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[1][1] == 2) and (board[2][2] == 2) and not played:
                row = 0
                col = 0
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[2][0] == 2) and (board[1][1] == 2) and not played:
                row = 0
                col = 2
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][2] == 2) and (board[1][1] == 2) and not played:
                row = 2
                col = 0
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if (board[0][2] == 2) and (board[2][0] == 2) and not played:
                row = 1
                col = 1
                if board[row][col] != 1:
                    played = True
                else:
                    played = False
            if not played:
                row = 3
                col = 3
        return played, row, col


    def block_vertically(played, player):
        if not played and player == 2:
            if (board[0][0] == 1) and (board[1][0] == 1) and not played:
                row = 2
                col = 0
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][0] == 1) and (board[2][0] == 1) and not played:
                row = 1
                col = 0
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[1][0] == 1) and (board[2][0] == 1) and not played:
                row = 0
                col = 0
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][1] == 1) and (board[1][1] == 1) and not played:
                row = 2
                col = 1
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][1] == 1) and (board[2][1] == 1) and not played:
                row = 1
                col = 1
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[1][1] == 1) and (board[2][1] == 1) and not played:
                row = 0
                col = 1
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][2] == 1) and (board[1][2] == 1) and not played:
                row = 2
                col = 2
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[1][2] == 1) and (board[2][2] == 1) and not played:
                row = 0
                col = 2
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][2] == 1) and (board[2][2] == 1) and not played:
                row = 1
                col = 2
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if not played:
                row = 3
                col = 3
        return played, row, col


    def block_horizontally(played, player):
        if not played and player == 2:
            if (board[0][0] == 1) and (board[0][1] == 1):
                row = 0
                col = 2
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][0] == 1) and (board[0][2] == 1) and not played:
                row = 0
                col = 1
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][1] == 1) and (board[0][2] == 1) and not played:
                row = 0
                col = 0
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[1][0] == 1) and (board[1][1] == 1) and not played:
                row = 1
                col = 2
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[1][0] == 1) and (board[1][2] == 1) and not played:
                row = 1
                col = 1
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[1][1] == 1) and (board[1][2] == 1) and not played:
                row = 1
                col = 0
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[2][0] == 1) and (board[2][1] == 1) and not played:
                row = 2
                col = 2
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[2][1] == 1) and (board[2][2] == 1) and not played:
                row = 2
                col = 0
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[2][0] == 1) and (board[2][2] == 1) and not played:
                row = 2
                col = 1
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if not played:
                row = 3
                col = 3
        return played, row, col


    def block_obliquely(played, player):
        if not played and player == 2:
            if (board[0][0] == 1) and (board[1][1] == 1):
                row = 2
                col = 2
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][0] == 1) and (board[2][2] == 1) and not played:
                row = 1
                col = 1
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[1][1] == 1) and (board[2][2] == 1) and not played:
                row = 0
                col = 0
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[2][0] == 1) and (board[1][1] == 1) and not played:
                row = 0
                col = 2
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][2] == 1) and (board[1][1] == 1) and not played:
                row = 2
                col = 0
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if (board[0][2] == 1) and (board[2][0] == 1) and not played:
                row = 1
                col = 1
                if board[row][col] != 2:
                    played = True
                else:
                    played = False
            if not played:
                row = 3
                col = 3
        return played, row, col


    def pick_center(played, player):
        if not played and player == 2:
            if board[1][1] != 1 and board[1][1] != 2:
                row = 1
                col = 1
                played = True
            if not played:
                row = 3
                col = 3
        return played, row, col


    def create_fork(played, player):
        if not played and player == 2:
            if ((board[0][0] == 1 and board[2][2] == 1) or (board[0][2] == 1 and board[2][0] == 1)):
                possible = [(1, 2), (0, 1), (1, 0), (2, 1)]
                index = random.randint(0, 3)
                if board[possible[index][0]][possible[index][1]] != 1 and board[possible[index][0]][
                    possible[index][1]] != 2:
                    row = possible[index][0]
                    col = possible[index][1]
                    played = True
            if not played:
                row = 3
                col = 3
        return played, row, col


    def pick_corner(played, player):
        if not played and player == 2:
            possible = [(0, 0), (0, 2), (2, 2), (2, 0)]
            index = random.randint(0, 3)
            empty_squares = get_empty_squares()
            i = index
            while i < index + 4 and not played:
                if possible[i % 4] in empty_squares:
                    row = possible[i % 4][0]
                    col = possible[i % 4][1]
                    played = True
                i += 1
            if not played:
                row = 3
                col = 3
        return played, row, col


    def rand_move(played, player):
        if not played and player == 2:
            move = rand()
            row = move[0]
            col = move[1]
        return row, col


    def smart_ai_score(player, win1, win2):
        idiot_ai_reset(win1, win2)
        if player == 1:
            pygame.draw.rect(screen, RED, pygame.Rect(40, 610, 170, 80))
        pygame.draw.circle(screen, CIRCLE_COLOUR, (80, 650), 30, 8)
        pygame.draw.line(screen, CROSS_COLOUR, (495, 680), (545, 620), 10)
        pygame.draw.line(screen, CROSS_COLOUR, (545, 680), (495, 620), 10)
        win1TXT = str(win1)
        win2TXT = str(win2)
        screen.blit(score_font.render(win1TXT, True, CIRCLE_COLOUR), (130, 620))
        screen.blit(score_font.render(win2TXT, True, CROSS_COLOUR), (420, 620))


    def smart_ai():
        win1 = 0
        win2 = 0
        draw_lines()
        player = 1
        click5 = False
        game_over = False
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(40, 610, 170, 80))
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(390, 610, 170, 80))
        while True:
            if not game_over:
                smart_ai_score(player, win1, win2)
            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(50, 720, 64, 64)
            button2 = pygame.Rect(495, 720, 64, 64)
            screen.blit(HOME_ICON, (50, 720))
            screen.blit(RESTART_ICON, (495, 720))
            if button1.collidepoint((mx, my)):
                if click5:
                    home()
            if button2.collidepoint((mx, my)):
                if click5:
                    restart()
                    game_over = False
            click5 = False
            played = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os.remove("log/error.txt")
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        home()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click5 = True
                if player == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                        mouseX = event.pos[0]
                        mouseY = event.pos[1]
                        if mouseY <= 600:
                            clicked_row = int(mouseY // 200)
                            clicked_col = int(mouseX // 200)
                            if available_square(clicked_row, clicked_col):
                                mark_square(clicked_row, clicked_col, 1)
                                if check_win(player):
                                    win1 = win1 + 1
                                    screen.blit(font.render("Human wins!", True, CIRCLE_COLOUR), (170, 730))
                                    file = open("log/error.txt", "w")
                                    file.write("Wow, that should not have happened. AI should always win. Please report it using the following link: https://bit.ly/3O72Rpa")
                                    file.close()
                                    os.startfile("log\\error.txt")
                                    game_over = True
                                    reset(win1, win2)
                                if is_board_full() and not game_over:
                                    screen.blit(font.render("Draw", True, RED), (255, 730))
                                    game_over = True
                                    reset(win1, win2)
                                player = 2
                                if not game_over:
                                    smart_ai_score(2, win1, win2)
                elif player == 2:
                    played = False
                    if not is_board_full() and not game_over and not played:
                        # Win vertically
                        win, row, col = win_vertically(played, player)
                        if not win:
                            win, row, col = win_horizontally(played, player)
                            if not win:
                                win, row, col = win_obliquely(played, player)
                                if not win:
                                    win, row, col = block_vertically(played, player)
                                    if not win:
                                        win, row, col = block_horizontally(played, player)
                                        if not win:
                                            win, row, col = block_obliquely(played, player)
                                            if not win:
                                                win, row, col = pick_center(played, player)
                                                if not win:
                                                    win, row, col = create_fork(played, player)
                                                    if not win:
                                                        win, row, col = pick_corner(played, player)
                                                        if not win:
                                                            row, col = rand_move(played, player)

                        mark_square(row, col, 2)


                    if check_win(player):
                        win2 = win2 + 1
                        screen.blit(font.render("Robot wins!", True, CROSS_COLOUR), (180, 730))
                        game_over = True
                        reset(win1, win2)
                    if is_board_full() and not game_over:
                        screen.blit(font.render("Draw", True, RED), (255, 730))
                        game_over = True
                        reset(win1, win2)
                    player = 1
                    if not game_over:
                        idiot_ai_score(1, win1, win2)
                    draw_figures()
            pygame.display.update()


    def game_page():
        screen.fill(BG_COLOUR)
        click6 = False
        while True:
            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(50, 720, 64, 64)
            screen.blit(HOME_ICON, (50, 720))
            screen.blit(font.render("Choose your game!", True, CIRCLE_COLOUR), (105, 70))
            button2 = pygame.Rect(150, 170, 300, 120)
            button3 = pygame.Rect(150, 360, 300, 120)
            button4 = pygame.Rect(150, 560, 300, 120)
            pygame.draw.rect(screen, DARK_RED, button2)
            pygame.draw.rect(screen, DARK_RED, button3)
            pygame.draw.rect(screen, DARK_RED, button4)
            screen.blit(font.render("Multiplayer", True, CIRCLE_COLOUR), (185, 210))
            screen.blit(font.render("Easy", True, CIRCLE_COLOUR), (250, 400))
            screen.blit(font.render("Impossible", True, CIRCLE_COLOUR), (195, 600))
            if button1.collidepoint((mx, my)):
                if click6:
                    home()
            if button2.collidepoint((mx, my)):
                pygame.draw.rect(screen, RED, button2)
                screen.blit(font.render("Multiplayer", True, CIRCLE_COLOUR), (185, 210))
                if click6:
                    screen.fill(BG_COLOUR)
                    game()
            if button3.collidepoint((mx, my)):
                pygame.draw.rect(screen, RED, button3)
                screen.blit(font.render("Easy", True, CIRCLE_COLOUR), (250, 400))
                if click6:
                    screen.fill(BG_COLOUR)
                    idiot_ai()
            if button4.collidepoint((mx, my)):
                pygame.draw.rect(screen, RED, button4)
                screen.blit(font.render("Impossible", True, CIRCLE_COLOUR), (195, 600))
                if click6:
                    screen.fill(BG_COLOUR)
                    smart_ai()
            click6 = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os.remove("log/error.txt")
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click6 = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        home()
            pygame.display.update()

    def game():
        win1 = 0
        win2 = 0
        click2 = False
        draw_lines()
        player = 1
        game_over = False
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(40, 610, 170, 80))
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(390, 610, 170, 80))
        while True:
            if not game_over:
                score(player, win1, win2)
            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(50, 720, 64, 64)
            button2 = pygame.Rect(495, 720, 64, 64)
            screen.blit(HOME_ICON, (50, 720))
            screen.blit(RESTART_ICON, (495, 720))
            if button1.collidepoint((mx, my)):
                if click2:
                    home()
            if button2.collidepoint((mx, my)):
                if click2:
                    restart()
                    game_over = False
            click2 = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os.remove("log/error.txt")
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    if mouseY <= 600:
                        clicked_row = int(mouseY // 200)
                        clicked_col = int(mouseX // 200)

                        if available_square(clicked_row, clicked_col):
                            if player == 1:
                                mark_square(clicked_row, clicked_col, 1)
                                if check_win(player):
                                    win1 = win1 + 1
                                    screen.blit(font.render("Player 1 wins!", True, CIRCLE_COLOUR), (160, 730))
                                    game_over = True
                                    reset(win1, win2)
                                if is_board_full() and not check_win(player):
                                    screen.blit(font.render("Draw", True, RED), (255, 730))
                                    game_over = True
                                    reset(win1, win2)
                                player = 2
                                if not game_over:
                                    score(2, win1, win2)
                            elif player == 2:
                                mark_square(clicked_row, clicked_col, 2)
                                if check_win(player):
                                    win2 = win2 + 1
                                    screen.blit(font.render("Player 2 wins!", True, CROSS_COLOUR), (160, 730))
                                    game_over = True
                                    reset(win1, win2)
                                if is_board_full() and not check_win(player):
                                    screen.blit(font.render("Draw", True, RED), (255, 730))
                                    game_over = True
                                    reset(win1, win2)
                                player = 1
                                if not game_over:
                                    score(1, win1, win2)

                        draw_figures()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click2 = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        os.remove("log/error.txt")
                        pygame.quit()
                        sys.exit()
            pygame.display.update()


    home()


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