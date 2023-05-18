from enum import Enum


class Suit(Enum):
    CLUB = "Club"
    HEART = "Heart"
    SPADE = "Spade"
    DIAMOND = "Diamond"


class Action(Enum):
    ALL_IN = "ALL_IN"
    FOLD = "FOLD"
    NOTHING = "NOTHING"


class DealerPosition(Enum):
    BUTTON = 1
    BIG_BLIND = 2
    SMALL_BLIND = 3
    UTG = 4


class Card:
    suit: Suit
    card_type: int

    def __init__(self, suit, card_type) -> None:
        self.suit = suit
        self.card_type = card_type
