import random 

'''
class Cards:
    def __init__(self):
        self.cards =
 '''        
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


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.player_cards = []
        self.dealer_cards = []
    
    def deal_player(self):  # this is the initial deal for the player
        count_player = 0
        
        while count_player < 2:
            self.player_cards.append(random.choice(list(self.cards)))
            count_player += 1
        return self.player_cards

    def player_hit_or_stand(self):  # this will prompt player to hit or stand
        hit_or_stand = input("Hit or Stand: ")
        if hit_or_stand.lower() == "hit":
            self.player_cards.append(random.choice(list(self.cards)))
            return self.player_cards, self.show_player_cards()

        

    def show_player_cards(self):   # prints players cards
        print(f"Your cards are: {self.player_cards}")

    def deal_dealer(self):  # deals dealer cards
        count_dealer = 0
        
        while count_dealer < 2:
            self.dealer_cards.append(random.choice(list(self.cards)))
            count_dealer += 1
        return self.dealer_cards

    def show_dealer_card(self):  # shows dealers first dealt card to player
        print(f"Dealer shows: {self.dealer_cards[0]}")










