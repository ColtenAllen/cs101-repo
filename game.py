from cards import Deck, deck_dict

new_deck = Deck(deck_dict)

new_deck.deal_player()
new_deck.show_player_cards()
new_deck.deal_dealer()
new_deck.show_dealer_card()
new_deck.player_hit_or_stand()