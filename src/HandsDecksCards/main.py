"""
The code in this module illustrates how to create and use Card, Deck, and Hand classes to represent playing cards,
decks of playing cards, and hands of cards.

Exported Classes:
    None

Exported Exceptions:
    None
 
Exported Functions:
    __main__ -- Create and use Card, Deck, and Hand objects.
"""


# Standard


# Local
from card import Card
from deck import Deck
from hand import Hand


if __name__ == '__main__':
    
    """
    Create and Use Card, Deck, and Hand objects.
    """

    # Create cards: King of Hearts and 10 of Diamonds
    c_kh = Card('H', 'K')
    c_10d = Card('D', '10')
    # Card implements __str__()
    print(f"Created cards: {c_kh}, {c_10d}")
    # You can get the suit of a card
    print(f"Suit of {c_10d}: {c_10d.suit}")
    # You can get the pips of a card
    print(f"Pips of {c_10d}: {c_10d.pips}")
    # You can get the count of a card
    print(f"Count of {c_kh}: {c_kh.count_card()}")
    # Card implements __lt__(), so a list of Card objects, can be sorted (A high)
    cards = [c_kh, c_10d]
    cards.sort()
    print(f"Sorted cards (low to high): {cards}")
    # Or Card objects an be directly compared:
    print(f"10 is less than king?: {c_10d < c_kh}")
    # Card provides a utility function that can create a list of Card objects from a string representation
    card_list = Card().make_card_list_from_str('AS KH QD JC 10H 2S')
    print(f"Created card list from string: {card_list}")

    # Create a deck of cards
    d = Deck()
    # Draw 5 cards from the deck
    drawn = d.draw(5)
    print(f"Drew 5 cards from deck: {drawn}")
    # How many cards remain in the deck? Deck implements __len__().
    print(f"Cards remaining in deck: {len(d)}")
    # What cards remain in the deck? Deck implements __str__().
    print(f"Cards remaining in deck: {d}")
 
    # Create an empty hand of cards
    h = Hand()
    # Add another ace to the card list created above
    card_list.append(Card('C','A'))
    # Add cards to the hand. Typically this would be done by drawing from a deck, but here we will just add chosen cards.
    h.add_cards(card_list)
    print(f"Hand after adding cards: {h}")
    # Count the cards in the hand
    print(f"Count of hand (ace low): {h.count_hand()}")
    # Get information about the hand
    hand_info = h.hand_info()
    print(f"Hand info: {hand_info}")
    # How many cards are in the hand?
    print(f"Number of cards in hand: {hand_info.Num_Aces + hand_info.Num_Other}")
    print(f"Number of cards in hand: {h.get_num_cards()}")
    # How many aces are in the hand?
    print(f"Number of aces in hand: {h.get_num_aces()}")
    # What aces are in the hand?
    aces = h.get_aces()
    # Can iterate a Hand object to get the cards in the hand
    for a in aces:
        print(f"Ace in hand: {a}")
    # How many non-ace cards are in the hand?
    print(f"Number of non-ace cards in hand: {h.get_num_non_aces()}")
    # Which non-ace cards are in the hand?
    non_aces = h.get_non_aces()
    # Hand defines __repr__(), so can use eval() to recreate a Hand object
    print(f"Non-ace cards in hand: {eval(repr(non_aces))}")
    # Remove the last card from the hand
    removed_card = h.remove_card()
    print(f"Removed card: {removed_card}")
    print(f"Remaining cards in hand: {h}")
    # Remove the 3rd card (index 2) from the hand
    removed_card = h.remove_card(2)
    print(f"Removed card at index 2: {removed_card}")
    print(f"Remaining cards in hand: {h}")



     
