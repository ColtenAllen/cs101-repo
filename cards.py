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
        game.player_21()  # most of the game logic now flows through this method. I don't like how I have done this, but I will fix it at a later date
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

        if self.player_total > 21:  # adds bust logic
            print("You Bust!")
            quit()
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
        print(f"You Stand on {self.player_total}")
        print(f"Dealer shows {self.dealer_cards}")
        if self.dealer_total >= 17:
            print(f"Dealer total: {self.dealer_total}")
            if self.dealer_total < self.player_total:
                print("You Win!")
                quit()
            elif self.dealer_total == self.player_total:
                print("Draw")
                quit()
            elif self.dealer_total > self.player_total:
                print("You Lose!")
                quit()

        elif self.dealer_total < 17:
            while self.dealer_total < 17:
                self.dealer_cards.append(random.choice(list(self.cards)))  # this deals dealer another cards
                self.dealer_total = self.sum_dealer_cards()  # updates dealer total
                print(f"Dealer turns: {self.dealer_cards[-1]}. Dealer total: {self.dealer_total}")
            
            if self.player_total < self.dealer_total < 21:
                print("You Lose!")
                quit()
            elif self.player_total > self.dealer_total < 21:
                print("You Win!")
                quit()
            elif self.dealer_total > 21:
                print("Dealer Busts! You Win!")

            


        

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

    def player_has_ace(self):  # this should be called anytime the player has an ace in their hand
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

    def dealer_has_ace(self):  # this should be called anytime the dealer has an ace in their hand
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


