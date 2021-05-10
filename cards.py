import random 
from deckDictionary import deck_dict    

def play_game():
    game = Deck(deck_dict)  # instantiates instance of Deck
    print("SkunkRat Productions Presents: Blackjack")

    # Begins game
    ready = input("Are you ready to play?\n")
    if ready.lower() == "yes":
        game.deal()
        game.show_player_cards()
        print()
        game.show_dealer_card()
        print()
        game.player_21() 
    else:
        print("Goodbye")
        quit()

    
class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.player_cards = []
        self.dealer_cards = []
        self.dealer_total = 0
        self.player_total = 0
    
    def deal(self):  # this is the initial deal for the player
        count = 0

        while count < 2:
            self.player_cards.append(random.choice(list(self.cards)))
            self.dealer_cards.append(random.choice(list(self.cards)))
            count += 1
        self.dealer_total = self.sum_dealer_cards()  # updates dealer and player totals automatically when deal is called
        self.player_total = self.sum_player_cards()
        print(f"This is the player total after the deal {self.player_total}")
        return self.player_cards, self.dealer_cards, self.dealer_total, self.player_total

    def player_hit(self):  # this will prompt player to hit or stand
        while self.player_total < 21:
            hit_or_stand = input("Hit or Stand:\n")
            if hit_or_stand.lower() == "hit":
                self.player_cards.append(random.choice(list(self.cards)))
                self.player_total = self.sum_player_cards()
                self.show_player_cards()
                print(f"this is the player total {self.player_total}")
        return self.player_cards, self.player_total  # self.show_player_cards()
            #else:

    def player_21(self):
        if self.player_total < 21 and self.dealer_total != 21:
            self.player_hit()
        elif self.player_total == 21 and self.dealer_total != 21:
            print("You win!")
            quit()  # I want to add play again fucntionality at some point here and after the 'else' statement below
        elif self.player_total != 21 and self.dealer_total == 21:
            print("Stand Off")
            quit()

    # def 

        

    def show_player_cards(self):   # prints players cards
        print(f"Your hand: {self.player_cards}")

    def show_dealer_card(self):  # shows dealers first dealt card to player
        print(f"Dealer shows: {self.dealer_cards[0]}")

    def sum_player_cards(self):  # sums player cards
        total = 0
        for card in self.player_cards:
            total += deck_dict[card]
        return total

    def sum_dealer_cards(self):  # sums dealer cards
        total = 0
        for card in self.dealer_cards:
            total += deck_dict[card]
        return total


'''
ace logic
 if self.player_total > 21 and 'ace' in self.player_cards:
     'ace' == 1
'''
