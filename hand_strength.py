from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

from my_types import Suit


class HandStrength:
    def get_card_value(self, card):
        match card.card_type:
            case "Ace":
                return 14
            case "King":
                return 13
            case "Queen":
                return 12
            case "Jack":
                return 11
            case "Ten":
                return 10
            case "Nine":
                return 9
            case "Eight":
                return 8
            case "Seven":
                return 7
            case "Six":
                return 6
            case "Five":
                return 5
            case "Four":
                return 4
            case "Three":
                return 3
            case "Two":
                return 2

    def get_suit_value(self, card):
        match card.suit:
            case Suit.SPADE:
                return 1
            case Suit.HEART:
                return 2
            case Suit.DIAMOND:
                return 3
            case Suit.CLUB:
                return 4

    def get_hand_strength(self, left_card, right_card):
        left_score = self.get_card_value(left_card)
        left_suit = self.get_suit_value(left_card)

        right_score = self.get_card_value(right_card)
        right_suit = self.get_suit_value(right_card)

        hole = [Card(left_score, left_suit), Card(right_score, right_suit)]
        board = []

        score = HandEvaluator.evaluate_hand(hole, board)

        return score
