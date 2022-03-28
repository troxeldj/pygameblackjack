import pygame
import random
import os
pygame.init()

# Constants
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
FPS = 20
clock = pygame.time.Clock()

# FONTS
WINNER_FONT = pygame.font.SysFont('comicsans', 60)
MONEY_FONT = pygame.font.SysFont('comicsans', 20)
GAME_OVER_FONT = pygame.font.SysFont('comicsans', 80)

#######################################################################
# drawText
# Input:
# - font: Font (pygame Font Object)
# - text: User Text (String)
# - color: Color of button background (Pygame color Object or RGB Tuple)
# - Screen x, y Position (int)
########################################################################


def drawText(font, text, color, x, y):
    winner_text = font.render(text, 1, color)
    WIN.blit(winner_text, (x, y))
    pygame.display.update()


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


#######################################################################
# BLACKJACK TABLE CLASS
# Represents the blackjack table. Handles game logic.
#
# Attributes:
# - player: player playing at blackjack table
# - dealer: dealer dealing at blackjack table.
# - deck: Deck of cards at the blackjack table.
#
# Methods:
# - initDeal: Inital deal (Player gets two cards / Dealer one).
# - Hit: Handles player hitting / getting card.
# - Stand: Handles player standing and dealer drawing.
# - Double: Handles player doubling down (FOR NOW IT'S JUST BETX2)
# - increaseBet: Increases players current bet by set amount
# - _restart: Goes back to initdeal using players current money. If
#   player is out of money, game totally restarts
#######################################################################


class BlackJackTable():
    def __init__(self):
        self.player = Player(500)
        self.player.betAmount = 10
        self.dealer = Dealer()
        self.deck = Deck()
        self.initDeal()

    def initDeal(self):
        # Player Draws Two Cards
        self.player.drawCardFromDeck(self.deck)
        self.player.drawCardFromDeck(self.deck)

        # Dealer Draws One Card
        self.dealer.drawCardFromDeck(self.deck)

        # Draw Player and Dealer Hands
        self.player.drawHand(WIN)
        self.dealer.drawHand(WIN)

        if(self.player.cardTotal == 21):  # Case: Immediate Jackpot
            drawText(WINNER_FONT, 'You Win!', YELLOW,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.time.wait(2000)

    def Hit(self):
        self.player.drawCardFromDeck(self.deck)
        self.player.drawHand(WIN)
        if(self.player.cardTotal > 21):  # Case: Hit Bust
            self.player.money -= self.player.betAmount
            drawText(WINNER_FONT, 'You Busted!', RED,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.time.wait(2000)
            self._restart()
        if(self.player.cardTotal == 21):  # Case: Hit Blackjack
            self.player.money += self.player.betAmount
            drawText(WINNER_FONT, 'You Win!', YELLOW,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.time.wait(2000)
            self._restart()

    def Stand(self, win):
        while(self.dealer.cardTotal <= 16):
            self.dealer.drawCardFromDeck(self.deck)
            self.dealer.drawHand(win)

        if(self.dealer.cardTotal == 21):  # Case: dealer gets blackjack
            self.player.money -= self.player.betAmount
            drawText(WINNER_FONT, 'You Lose!', RED,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.time.wait(2000)
            self._restart()
        elif(self.dealer.cardTotal > 21):  # Case: dealer busts
            self.player.money += self.player.betAmount
            drawText(WINNER_FONT, 'You Win!', YELLOW,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.time.wait(2000)
            self._restart()
        elif(self.dealer.cardTotal > self.player.cardTotal):  # Case: Dealer > Player: Dealer WINS
            self.player.money -= self.player.betAmount
            drawText(WINNER_FONT, 'You Lose!', RED,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.time.wait(2000)
            self._restart()
        else:
            self.player.money += self.player.betAmount  # Case: Player > Dealer: Player WINS
            drawText(WINNER_FONT, 'You Win!', YELLOW,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.time.wait(2000)
            self._restart()

    def Double(self):
        if(self.player.betAmount * 2 <= self.player.money):
            self.player.betAmount *= 2
        else:
            drawText(WINNER_FONT, 'Not Enough Funds!',
                     RED, WIDTH//2 - 250, HEIGHT//2 - 100)
            pygame.time.wait(2000)
            self.player.betAmount = 10

    def increaseBet(self, amount):
        if(self.player.betAmount + amount <= self.player.money):
            self.player.betAmount += amount
        else:
            drawText(WINNER_FONT, 'Not Enough Funds!', RED,
                     WIDTH//2 - 250, HEIGHT//2 - 100)
            pygame.time.wait(2000)
            self.player.betAmount = 10

    def _restart(self):
        if(self.player.money > 0):
            self.player = Player(self.player.money)
            self.player.betAmount = 10
            self.dealer = Dealer()
            self.deck = Deck()
            self.initDeal()
        else:
            drawText(GAME_OVER_FONT, "GAME OVER", RED, WIDTH//4, HEIGHT//2)
            drawText(MONEY_FONT, 'Restarting.. Wait..', WHITE,
                     WIDTH // 2 - 50, HEIGHT//2 - 10)
            pygame.time.wait(5000)
            self.__init__()


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
    drawText(MONEY_FONT, 'Money: ' + str(table.player.money), WHITE,
             WIDTH-BUTTON_WIDTH * 2, HEIGHT-(BUTTON_HEIGHT + 90))
    drawText(MONEY_FONT, 'Bet: ' + str(table.player.betAmount), WHITE,
             WIDTH-BUTTON_WIDTH * 2, HEIGHT-(BUTTON_HEIGHT + 60))

    # Write Dealer/Player Deck Values to Screen

    drawText(MONEY_FONT, 'Your Deck: ' + str(table.player.cardTotal), WHITE,
             CARD_WIDTH * 3, HEIGHT - CARD_HEIGHT * 1.25)
    drawText(MONEY_FONT, 'Dealer Deck: ' + str(table.dealer.cardTotal), WHITE,
             WIDTH-BUTTON_WIDTH * 2, HEIGHT-BUTTON_HEIGHT * 4)

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
