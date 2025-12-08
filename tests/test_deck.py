"""
This module provides unit tests for Deck, ShoeDeck, and StackedDeck classes.
"""


# Standard
import unittest

# Local
from deck import Deck, ShoeDeck, StackedDeck
from card import Card

class Test_Deck(unittest.TestCase):
    
    def test_add_card(self):
        d1 = Deck()
        exp_val = Card('C','Q')
        d2 = d1.add_card(exp_val)
        act_val = d2[len(d2)-1]
        self.assertEqual(exp_val.suit, act_val.suit)
        self.assertEqual(exp_val.pips, act_val.pips)
    
    def test_cards_remaining(self):
        exp_val = 52
        d = Deck()
        act_val = d.cards_remaining()
        self.assertEqual(exp_val, act_val)

    def test_len(self):
        exp_val = 52
        d = Deck()
        act_val = len(d)
        self.assertEqual(exp_val, act_val)
        
    def test_draw_one_not_infinite(self):
        from random import seed
        seed(1234567890)
        d = Deck()
        dc = d.draw()
        # Has the number of cards decreased by 1?
        self.assertEqual(51, d.cards_remaining())
        # Has the expected card been drawn?
        c = Card('H', 'Q')
        exp_val = (c.suit, c.pips)
        act_val = (dc.suit, dc.pips)
        self.assertTupleEqual(exp_val, act_val)
        # Is the drawn card gone from the deck?
        self.assertTrue(dc not in d._deck)
        
    def test_draw_all_not_infinite(self):
        from random import seed
        seed(1234567890)
        d = Deck()
        dc = d.draw(52)
        # Are there no cards remaining in the deck?
        self.assertEqual(0, d.cards_remaining())
        # Is there 52 cards in the draw?
        self.assertEqual(52, len(dc))
        
    def test_draw_one_infinite(self):
        from random import seed
        seed(1234567890)
        # Create an "infinte" deck
        d = Deck(True)
        dc = d.draw()
        # Has the number of cards remained 52?
        self.assertEqual(52, d.cards_remaining())
        # Has the expected card been drawn?
        c = Card('H', 'Q')
        exp_val = (c.suit, c.pips)
        act_val = (dc.suit, dc.pips)
        self.assertTupleEqual(exp_val, act_val)
        # Is the drawn card still in the deck?
        self.assertTrue(dc in d._deck)
        
    def test_draw_too_many_cards(self):
        from random import seed
        seed(1234567890)
        d = Deck()
        # Draw one more card than is available in the deck, to force the deck to be rebuilt to provide the last card of the draw
        dc = d.draw(53)
        # Deck should have 51 cards
        self.assertEqual(51, d.cards_remaining())
        # Has the expected card been drawn last?
        c = Card('S', '2')
        exp_val = (c.suit, c.pips)
        act_val = (dc[len(dc)-1].suit, dc[len(dc)-1].pips)
        self.assertTupleEqual(exp_val, act_val)


class Test_ShoeDeck(unittest.TestCase):
    
    def test_init(self):
        d1 = ShoeDeck()
        exp_val = 5*52
        act_val = d1.cards_remaining()
        self.assertEqual(exp_val, act_val)

    def test_draw(self):
        from random import seed
        seed(1234567890)
        d1 = ShoeDeck()
        # Draw 5*52+1 cards to force a rebuild of the shoe
        card_list = d1.draw(5*52+1)
        # The last card drawn should be the 3 of Hearts
        self.assertTupleEqual(('H','3'), (card_list[len(card_list)-1].suit, card_list[len(card_list)-1].pips))
        # And the shoe should now have 5*52-1 cards remaining
        self.assertEqual(5*52-1, len(d1))


class Test_StackedDeck(unittest.TestCase):
    
    def test_init(self):
        d1 = StackedDeck()
        exp_val = 0
        act_val = d1.cards_remaining()
        self.assertEqual(exp_val, act_val)

    def test_draw(self):
        d1 = StackedDeck()
        # Add 5 cards to the stacked deck
        card_list = Card().make_card_list_from_str('AS 3C 9D 4H JC')
        d1.add_cards(card_list)
        # Draw 2 cards. Last card drawn should be the 3 of Clubs
        card_list = d1.draw(2)
        self.assertTupleEqual(('C','3'), (card_list[1].suit, card_list[1].pips))
        # And the show should now have 3 cards remaining
        self.assertEqual(3, len(d1))
        # Draw 3 cards, then one more. Since only 3 remain, should assert when the one more is requested.
        d1.draw(3)
        self.assertRaises(AssertionError, d1.draw)
        

if __name__ == '__main__':
    unittest.main()
