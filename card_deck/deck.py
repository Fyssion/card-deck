import random

from card_cards import Card


class Deck:
    """A card deck

    Parameters
    -----------
    cards: List[:class:`.Card`]
        A list of cards to start the deck with. These are automatically shuffled
    """

    def __init__(self, cards):
        self._cards = cards
        self.shuffle()

    def __getitem__(self, item):
        return self._cards[item]

    def __len__(self):
        return len(self._cards)

    def __iter__(self):
        return iter(self._cards)

    def __str__(self):
        return str(self._cards)

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self._cards)

    def draw(self, count: int = 1, from_bottom: bool = False):
        """Draw a card from the deck

        Parameters
        -----------
        count: Optional[:class:`int`]
            How many cards to draw from the deck
        from_bottom: Optional[:class:`bool`]
            Whether or not to draw from the bottom

        Returns
        --------
        card(s): Union[:class:`.Card`, List[:class:`.Card`]]
            The card drawn or a list of cards drawn in order
        """
        cards = []
        for i in range(count):
            if from_bottom:
                cards += self._cards.pop(len(self._cards) - 1 - i)
            cards += self._cards.pop(i)

        if count == 1:
            return cards[0]
        else:
            return cards

    def insert(self, card: Card, position: int = 0):
        """Insert a card at the given position, zero being the top

        Parameters
        -----------
        card: :class:`.Card`
            The card to insert into the deck
        position: Optional[:class:`int`]
            The position at which to insert the card, zero being the top
        """
        self._cards.insert(position, card)

    def insert_many(self, cards: list, position: int = 0):
        """Insert a list of cards at the given position, zero being the top

        Parameters
        -----------
        cards: List[:class:`.Card`]
            The list of cards to insert into the deck
        position: Optional[:class:`int`]
            The position at which to insert the cards, zero being the top
        """
        for i, card in enumerate(cards):
            self._cards.insert(position + i, card)

    def peek(self, count: int = 1, from_bottom: bool = False):
        """Peek at the top card(s)

        Parameters
        -----------
        count: :class:`int`
            The number of cards to peek
        from_bottom: Optional[:class:`bool`]
            Whether or not to peek from the bottom of the deck
        """
        if from_bottom:
            cards = [self._cards[len(self._cards) - 1 - i] for i in range(count)]
        else:
            cards = [self._cards[i] for i in range(count)]
        return cards
