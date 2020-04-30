import enum


class Card:
    """A playing card with no special attributes

    Parameters
    -----------
    name: :class:`str`
        The name of the card

    Attributes
    -----------
    name: :class:`str`
        The name of the card
    """

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


# ======================================================
# Below you will find a set of 52 standard playing cards
# ======================================================


class CardType(enum.Enum):
    ace = 1
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13


class Suit(enum.Enum):
    hearts = 0
    diamonds = 1
    spades = 2
    clubs = 3


class StandardCard(Card):

    def __init__(self, type, suit):
        name = f"{type} of {suit.value}"
        super().__init__(name)
        self.type = type
        self.suit = suit


# Comilping a list of all standard cards
# You can pass this into a deck to set up a deck
standard_cards = []

for suit in (Suit):
    for card_type in (CardType):
        standard_cards.append(StandardCard(card_type, suit))
