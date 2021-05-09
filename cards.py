import random 
from deckDictionary import deck_dict    

def play_game():
    game = Deck(deck_dict)  # instantiates instance of Deck
    print("SkunkRat Productions Presents: Blackjack")
    # Begins game
    ready = input("Are you ready to play? ")
    if ready.lower() == "yes":
        game.deal()
        game.show_player_cards()
        game.show_dealer_card() 
    else:
        print("Goodbye")
        quit()
    # check if player dealt 21
    if game.player_total < 21 and game.dealer_total != 21:
        game.player_hit_or_stand()
    elif game.dealer_total != 21:
        print("You win!")
        quit()  # I want to add play again fucntionality at some point here and after the 'else' statement below
    else:
        print("Stand Off")
        quit()
    
        

  

    '''
    
    player_total = game.sum_player_cards()
    dealer_total = game.sum_dealer_cards()
    print(dealer_total)
    print(player_total)
    game.player_hit_or_stand()
    '''

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
        return self.player_cards, self.dealer_cards, self.dealer_total, self.player_total

    def player_hit_or_stand(self):  # this will prompt player to hit or stand
        hit_or_stand = input("Hit or Stand: ")
        if hit_or_stand.lower() == "hit":
            self.player_cards.append(random.choice(list(self.cards)))
            return self.player_cards, self.show_player_cards()

        

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









