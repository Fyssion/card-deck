import random

from .card import Card


class Deck:
    """A card deck

    Parameters
    -----------
    cards ([card_deck.Card]):
        A list of cards to start the deck with. These are automatically shuffled
    """

    def __init__(self, cards):
        self._deck = cards
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self._deck)

    def draw(self, count: int = 1, from_bottom: bool = False):
        """Draw a card from the deck

        Parameters
        -----------
        count (int) [optional]:
            How many cards to draw from the deck
        from_bottom (bool) [optional]:
            Whether or not to draw from the bottom

        Returns
        --------
        card(s) (Card or [Card,..]):
            The card draw or a list of cards draw in order
        """
        cards = []
        for i in range(count):
            cards += self._deck.pop(i)

        if count == 1:
            return cards[0]
        else:
            return cards

    def insert(self, card: Card, position: int = 0):
        """Insert a card at the given position, zero being the top

        Parameters
        -----------
        card (card_deck.Card):
            The card to insert into the deck
        position (int) [optional]:
            The position at which to insert the card, zero being the top
        """
        self._deck.insert(position, card)

    def insert_many(self, cards: list, position: int = 0):
        """Insert a list of cards at the given position, zero being the top

        Parameters
        -----------
        cards ([card_deck.Card,...]):
            The list of cards to insert into the deck
        position (int) [optional]:
            The position at which to insert the cards, zero being the top
        """
        for i, card in enumerate(cards):
            self._deck.insert(position + i, card)
