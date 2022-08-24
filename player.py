#######################################################################
# PLAYER CLASS
# Represents the player of the game.
#
# Attributes:
# - Money
# - Hand: List of cards in hand
# - BetAmount: The current amount player is betting
# - cardTotal: The current total value of cards in hand
#
# Methods:
# - drawCardFromDeck
# - drawHand: Draws player's hand to the Window (pygame surface object)
# - clearHand
#######################################################################


class Player:
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.betAmount = 0
        self.cardTotal = 0

    # Draw a card from deck
    def drawCardFromDeck(self, deck):
        drawnCard = deck.drawCard()
        self.hand.append(drawnCard)
        if(self.cardTotal <= 10 and drawnCard.val == 1):
            self.cardTotal += 11
        else:
            self.cardTotal += drawnCard.val

    # Draw's player's current hand to the screen
    def drawHand(self, screen):
        initial_player_width = 0
        if not self.hand:
            print("No cards in hand")
        for i in range(len(self.hand)):
            curCardImg = self.hand[i].__makeImage__()
            if(i == 0):
                screen.blit(curCardImg, (initial_player_width, 348))
                initial_player_width += 105
            if(i == 1):
                screen.blit(curCardImg, (initial_player_width, 348))
                initial_player_width += 105
            if(i == 2):
                screen.blit(curCardImg, (initial_player_width, 348))
                initial_player_width += 105
            if(i == 3):
                screen.blit(curCardImg, (initial_player_width, 348))
                initial_player_width += 105
            if(i == 4):
                screen.blit(curCardImg, (initial_player_width, 348))
                initial_player_width += 105

    # Clears player's hand of cards
    def clearHand(self):
        self.hand = []