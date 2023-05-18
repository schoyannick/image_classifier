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
