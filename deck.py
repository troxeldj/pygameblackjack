from constants import *
import random
import os

#######################################################################
# CARD CLASS
# Represents a single card. Later used in the deck class
# Attributes:
# suit: Suit, such as: hearts, clubs, etc.
# val: value of card (1-11)
#
# Methods:
# generateFileName: Generates a file name using the cards suit and val.
# Card images are located in Images folder.
# __makeImage__: Loads and scales down image of card and returns that
# image object.
# getCardValue: Gets value of card
#######################################################################


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        self.isHidden = False

    def __repr__(self):
        return '{} of {}'.format(self.val, self.suit)

    # Generates File name using name of card
    def generateFileName(self):
        return '{}_of_{}.png'.format(self.val, self.suit)

    # Loads and scales down card image
    def __makeImage__(self):
        cardImage = pygame.image.load(
            os.path.join('Images', self.generateFileName()))
        finalImage = pygame.transform.scale(
            cardImage, (CARD_WIDTH, CARD_HEIGHT))
        return finalImage

    def getCardValue(self):
        return self.val


#######################################################################
# DECK CLASS
# Represents a deck of cards. Has a list holding card objects.
# Methods:
# - __build__
# - drawCard
# - resetDeck
# - shuffleDeck
#######################################################################


class Deck:
    def __init__(self):
        self.cards = []
        self.__build__()
        self.shuffleDeck()

    # Populate Deck with Cards
    def __build__(self):
        # Add Cards to Deck
        for s in ['spades', 'hearts', 'clubs', 'diamonds']:
            for i in range(1, 11):
                self.cards.append(Card(s, i))

    # Draw a card from the Deck
    def drawCard(self):
        return self.cards.pop()

    # Remove all cards from the deck
    def __resetDeck(self):
        self.cards = []

    # Shuffle Cards in the Deck
    def shuffleDeck(self):
        random.shuffle(self.cards)





