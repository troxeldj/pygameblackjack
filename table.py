from constants import *
from helpers import drawText

from player import Player
from dealer import Dealer
from deck import Deck
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
# - increaseBet: Increases playefrom constants import *eal using players current money. If
#   player is out of money, game totally restarts
#######################################################################

from constants import *
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
            drawText(WIN, WINNER_FONT, 'You Win!', YELLOW,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.wait(2000)

    def Hit(self):
        self.player.drawCardFromDeck(self.deck)
        self.player.drawHand(WIN)
        if(self.player.cardTotal > 21):  # Case: Hit Bust
            self.player.money -= self.player.betAmount
            drawText(WIN, WINNER_FONT, 'You Busted!', RED,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.wait(2000)
            self._restart()
        if(self.player.cardTotal == 21):  # Case: Hit Blackjack
            self.player.money += self.player.betAmount
            drawText(WIN, WINNER_FONT, 'You Win!', YELLOW,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.wait(2000)
            self._restart()

    def Stand(self, win):
        while(self.dealer.cardTotal <= 16):
            self.dealer.drawCardFromDeck(self.deck)
            self.dealer.drawHand(win)

        if(self.dealer.cardTotal == 21):  # Case: dealer gets blackjack
            self.player.money -= self.player.betAmount
            drawText(WIN, WINNER_FONT, 'You Lose!', RED,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.wait(2000)
            self._restart()
        elif(self.dealer.cardTotal > 21):  # Case: dealer busts
            self.player.money += self.player.betAmount
            drawText(WIN, WINNER_FONT, 'You Win!', YELLOW,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.wait(2000)
            self._restart()
        elif(self.dealer.cardTotal > self.player.cardTotal):  # Case: Dealer > Player: Dealer WINS
            self.player.money -= self.player.betAmount
            drawText(WIN, WINNER_FONT, 'You Lose!', RED,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.wait(2000)
            self._restart()
        else:
            self.player.money += self.player.betAmount  # Case: Player > Dealer: Player WINS
            drawText(WIN, WINNER_FONT, 'You Win!', YELLOW,
                     WIDTH//2 - 150, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.wait(2000)
            self._restart()

    def Double(self):
        if(self.player.betAmount * 2 <= self.player.money):
            self.player.betAmount *= 2
        else:
            drawText(WIN, INNER_FONT, 'Not Enough Funds!',
                     RED, WIDTH//2 - 250, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.wait(2000)
            self.player.betAmount = 10

    def increaseBet(self, amount):
        if(self.player.betAmount + amount <= self.player.money):
            self.player.betAmount += amount
        else:
            drawText(WIN, WINNER_FONT, 'Not Enough Funds!', RED,
                     WIDTH//2 - 250, HEIGHT//2 - 100)
            pygame.display.update()
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
            drawText(WIN, GAME_OVER_FONT, "GAME OVER", RED, WIDTH//4, HEIGHT//2)
            drawText(WIN, MONEY_FONT, 'Restarting.. Wait..', WHITE,
                     WIDTH // 2 - 50, HEIGHT//2 - 10)
            pygame.display.update()
            pygame.time.wait(5000)
            self.__init__()

