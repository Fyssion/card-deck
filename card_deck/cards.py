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

    def __repr__(self):
        return self.name


# ======================================================
# Below you will find a set of 52 standard playing cards
# ======================================================


class StandardCardType(enum.Enum):
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
        name = f"{type.name} of {suit.name}"
        super().__init__(name)
        self.type = type
        self.suit = suit


# Comilping a list of all standard cards
# You can pass this into a deck to set up a deck
standard_cards = []

for suit in (Suit):
    for card_type in (StandardCardType):
        standard_cards.append(StandardCard(card_type, suit))

# ======================================
# Below you will find a set of Uno cards
# ======================================


class Color(enum.Enum):
    red = 0
    yellow = 1
    blue = 2
    green = 3


class UnoCardType(enum.Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    skip = 10
    reverse = 11
    add_2 = 12
    wild = 13
    wild_add_4 = 14


class UnoCard(Card):

    def __init__(self, color: Color, type: UnoCardType):
        name = f"{color.name} {type.name}"
        super().__init__(name)
        self.color = color
        self.type = type

# Comilping a list of all uno cards in a standard uno game
# You can pass this into a deck to set up an uno deck
uno_cards = []

# Adding first set of cards
for color in (Color):
    for i in range(14):
        uno_cards.append(UnoCard(color, UnoCardType(i)))
# Adding second set of cards
for color in (Color):
    for i in range(12):
        uno_cards.append(UnoCard(color, UnoCardType(i+1)))
        # Append missing wild_add_4 card
    uno_cards.append(UnoCard(color, UnoCardType.wild_add_4))
