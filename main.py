import pygame
import random
import os
from helpers import drawText, button
from constants import *

from dealer import Dealer
from player import Player
from table import BlackJackTable

pygame.init()


#######################################################################
# Button Objects for Game
# hitButton: Button to hit / get another card
# standButton: Button to stand
# doubleButton: Button to double down
# bet5Button: Button to increase bet by 5
# bet10Button: Button to increase bet by 10
# bet25Button: Button to increase bet by 25
# bet100Button: Button to increase bet by 100
#######################################################################


hitButton = button(RED, WIDTH-BUTTON_WIDTH, HEIGHT -
                   BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, 30, 'HIT')
standButton = button(YELLOW, WIDTH-BUTTON_WIDTH, HEIGHT -
                     BUTTON_HEIGHT * 2, BUTTON_WIDTH, BUTTON_HEIGHT, 30, 'STAND')
doubleButton = button(PURPLE, WIDTH-BUTTON_WIDTH, HEIGHT -
                      BUTTON_HEIGHT * 3, BUTTON_WIDTH, BUTTON_HEIGHT, 30, 'DOUBLE')
bet5Button = button(CYAN, WIDTH-BUTTON_WIDTH * 2,
                    HEIGHT - (BUTTON_HEIGHT + BUTTON_HEIGHT // 3), BUTTON_WIDTH, BUTTON_HEIGHT//3, 15, 'BET + 5')
bet10Button = button(BLUE, WIDTH-BUTTON_WIDTH * 2,
                     HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT//3, 15, 'BET + 10')
bet25Button = button(PINK, WIDTH-BUTTON_WIDTH * 2, HEIGHT -
                     (BUTTON_HEIGHT//3 * 2), BUTTON_WIDTH, BUTTON_HEIGHT//3, 15, 'BET + 25')
bet100Button = button(ORANGE, WIDTH-BUTTON_WIDTH * 2,
                      HEIGHT - BUTTON_HEIGHT//3, BUTTON_WIDTH, BUTTON_HEIGHT//3, 15, 'BET + 100')

#######################################################################
# draw_window
# Input:
# - table: BlackJackTable object
# Draws and updates screen w/ new info. Called in while loop of main
# game loop
#######################################################################


def draw_window(table):
    WIN.fill(GREEN)

    # Draw Buttons
    hitButton.draw(WIN)
    standButton.draw(WIN)
    doubleButton.draw(WIN)
    bet5Button.draw(WIN)
    bet10Button.draw(WIN)
    bet25Button.draw(WIN)
    bet100Button.draw(WIN)

    # Draw Player / Dealer Hands
    table.player.drawHand(WIN)
    table.dealer.drawHand(WIN)

    # Update Screen
    pygame.display.update()

    # Write Money / Bet to Screen
    drawText(WIN, MONEY_FONT, 'Money: ' + str(table.player.money), WHITE,
             WIDTH-BUTTON_WIDTH * 2, HEIGHT-(BUTTON_HEIGHT + 90))
    drawText(WIN, MONEY_FONT, 'Bet: ' + str(table.player.betAmount), WHITE,
             WIDTH-BUTTON_WIDTH * 2, HEIGHT-(BUTTON_HEIGHT + 60))

    # Write Dealer/Player Deck Values to Screen

    drawText(WIN, MONEY_FONT, 'Your Deck: ' + str(table.player.cardTotal), WHITE,
             CARD_WIDTH * 3, HEIGHT - CARD_HEIGHT * 1.25)
    drawText(WIN, MONEY_FONT, 'Dealer Deck: ' + str(table.dealer.cardTotal), WHITE,
             WIDTH-BUTTON_WIDTH * 2, HEIGHT-BUTTON_HEIGHT * 4)

    pygame.display.update()
    # NOTICE: I did not have to call pygame.display.update() because the drawText function already does.


def main():
    tableOne = BlackJackTable()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # Get Position of mouse
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If mouse is over button and mousebuttondown -> CLICK BUTTON and run function.
                if hitButton.isOver(mouse_pos):
                    tableOne.Hit()
                elif standButton.isOver(mouse_pos):
                    tableOne.Stand(WIN)
                elif doubleButton.isOver(mouse_pos):
                    tableOne.Double()
                elif bet5Button.isOver(mouse_pos):
                    tableOne.increaseBet(5)
                elif bet10Button.isOver(mouse_pos):
                    tableOne.increaseBet(10)
                elif bet25Button.isOver(mouse_pos):
                    tableOne.increaseBet(25)
                elif bet100Button.isOver(mouse_pos):
                    tableOne.increaseBet(100)
                pass
        # Draw Information to window.
        draw_window(tableOne)


if __name__ == '__main__':
    main()
