import random 
from deckDictionary import deck_dict    

def play_game():
    game = Deck(deck_dict)  # instantiates instance of Deck
    print("SkunkRat Productions Presents: Blackjack\n")

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
        self.hit_or_stand = 'hit'
    
    def deal(self):  # this is the initial deal for the player
        count = 0

        while count < 2:
            self.player_cards.append(random.choice(list(self.cards)))  # adds dealt cards to player cards list
            self.dealer_cards.append(random.choice(list(self.cards)))  # adds dealt dealer cards to dealer cards list
            count += 1
        self.dealer_total = self.sum_dealer_cards()  # updates dealer total automatically when deal() is called
        self.player_total = self.sum_player_cards()  # updates player total automatically when deal() is called 
        return self.player_cards, self.dealer_cards, self.dealer_total, self.player_total

    def player_hit(self):  # this will prompt player to hit or stand
        
        while self.hit_or_stand == 'hit' and self.player_total < 21:
            self.hit_or_stand = input("Hit or Stand:\n")
            if self.hit_or_stand.lower() == "hit":
                self.player_cards.append(random.choice(list(self.cards)))  # adds card to player card list
                self.player_total = self.sum_player_cards()  # updates sum of player cards
                self.show_player_cards()  # shows the player their cards
            elif self.hit_or_stand.lower() == "stand":
                self.player_stand()
        return self.player_cards, self.player_total  # self.show_player_cards()                

    def player_21(self):
        if self.player_total < 21 and self.dealer_total != 21:
            self.player_hit()
        elif self.player_total == 21 and self.dealer_total != 21:
            print("You Win!")
            quit()  # I want to add play again fucntionality at some point here and after the 'else' statement below
        elif self.player_total != 21 and self.dealer_total == 21:
            print("You Lose!")
            quit()
        else:
            print("Stand Off")
            quit()

    def player_stand(self):
        print("You want no card sir")

        

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

    def player_has_ace(self):
        if "ace of hearts" in self.player_cards:
            if self.player_total > 21:
                deck_dict["ace of hearts"] = 1 

        if "ace of spades" in self.player_cards:
            if self.player_total > 21:
                deck_dict["ace of spades"] = 1
    
        if "ace of clubs" in self.player_cards:
            if self.player_total > 21:
                deck_dict["ace of clubs"] = 1

        if "ace of diamonds" in self.player_cards:
            if self.player_total > 21:
                deck_dict["ace of diamonds"] = 1

    def dealer_has_ace(self):
        if "ace of hearts" in self.dealer_cards:
            if self.dealer_total > 21:
                deck_dict["ace of hearts"] = 1 

        if "ace of spades" in self.dealer_cards:
            if self.dealer_total > 21:
                deck_dict["ace of spades"] = 1
    
        if "ace of clubs" in self.dealer_cards:
            if self.dealer_total > 21:
                deck_dict["ace of clubs"] = 1

        if "ace of diamonds" in self.dealer_cards:
            if self.dealer_total > 21:
                deck_dict["ace of diamonds"] = 1

'''
ace logic
 if self.player_total > 21 and 'ace' in self.player_cards:
     'ace' == 1
'''
