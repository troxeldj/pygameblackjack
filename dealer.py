from constants import *


#######################################################################
# DEALER CLASS
# Represents the dealer that the player plays against.
#
# Attributes:
# - Hand: List of cards in hand
# - cardTotal: The current total value of cards in hand
#
# Methods:
# - drawCardFromDeck
# - drawHand: Draws player's hand to the Window (pygame surface object)
#######################################################################


class Dealer():

    def __init__(self):
        self.hand = []
        self.cardTotal = 0

    def drawCardFromDeck(self, deck):
        drawnCard = deck.drawCard()
        self.hand.append(drawnCard)
        self.cardTotal += drawnCard.getCardValue()

    def drawHand(self, screen):
        initial_dealer_width = WIDTH - CARD_WIDTH
        if not self.hand:
            print("No cards in hand")
        for i in range(len(self.hand)):
            curCardImg = self.hand[i].__makeImage__()
            if(i == 0):
                screen.blit(curCardImg, (initial_dealer_width, 0))
                initial_dealer_width -= 105
            if(i == 1):
                screen.blit(curCardImg, (initial_dealer_width, 0))
                initial_dealer_width -= 105
            if(i == 2):
                screen.blit(curCardImg, (initial_dealer_width, 0))
                initial_dealer_width -= 105
            if(i == 3):
                screen.blit(curCardImg, (initial_dealer_width, 0))
                initial_dealer_width -= 105
            if(i == 4):
                screen.blit(curCardImg, (initial_dealer_width, 0))
                initial_dealer_width -= 105