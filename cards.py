import random 
    
deck_dict = {'ace': 1, 
'2': 2, 
'3': 3, 
'4': 4, 
'5': 5,
'6': 6,
'7': 7,
'8': 8, 
'9': 9,
'10': 10,
'jack': 10,
'queen': 10,
'king': 10,
'ace': 1, 
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'jack': 10,
'queen': 10,
'king': 10,
'ace': 1, 
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'jack': 10,
'queen': 10,
'king': 10,
'ace': 1, 
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'jack': 10,
'queen': 10,
'king': 10}

def play_game():
    game = Deck(deck_dict)
    print("SkunkRat Productions Presents: Blackjack")
    ready = input("Are you ready to play? ")
    if ready.lower() == "yes":
        game.deal()
        game.show_player_cards()
    else:
        print("Goodbye")
        quit()

    print(game.player_total)
    print(game.dealer_total) 

    '''
    game.show_dealer_card() 
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
    
    def deal(self):  # this is the initial deal for the player
        count = 0

        while count < 2:
            self.player_cards.append(random.choice(list(self.cards)))
            self.dealer_cards.append(random.choice(list(self.cards)))
            count += 1
        self.dealer_total = self.sum_dealer_cards()
        self.player_total = self.sum_player_cards()
        return self.player_cards, self.dealer_cards, self.dealer_total, self.player_total

    def player_hit_or_stand(self):  # this will prompt player to hit or stand
        hit_or_stand = input("Hit or Stand: ")
        if hit_or_stand.lower() == "hit":
            self.player_cards.append(random.choice(list(self.cards)))
            return self.player_cards, self.show_player_cards()

        

    def show_player_cards(self):   # prints players cards
        print(f"Your cards are: {self.player_cards}")

    def show_dealer_card(self):  # shows dealers first dealt card to player
        print(f"Dealer shows: {self.dealer_cards[0]}")

    def sum_player_cards(self):
        total = 0
        for card in self.player_cards:
            total += deck_dict[card]
        return total

    def sum_dealer_cards(self):
        total = 0
        for card in self.dealer_cards:
            total += deck_dict[card]
        return total









