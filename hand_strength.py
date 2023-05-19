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

    unsuited_ranks_to_percentile = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [
            0,
            0,
            0.52337858220211153,
            0.0090497737556560764,
            0.018099547511312264,
            0.036199095022624417,
            0.02714932126696834,
            0.045248868778280493,
            0.093514328808446456,
            0.15384615384615385,
            0.23831070889894423,
            0.3227752639517345,
            0.41930618401206632,
            0.53242835595776772,
            0.68174962292609353,
            0,
        ],
        [
            0,
            0,
            0.0090497737556560764,
            0.64856711915535448,
            0.054298642533936681,
            0.075414781297134192,
            0.066365007541478116,
            0.08446455505279038,
            0.10558069381598789,
            0.18702865761689291,
            0.26244343891402711,
            0.35595776772247356,
            0.46455505279034692,
            0.56259426847662142,
            0.72398190045248867,
            0,
        ],
        [
            0,
            0,
            0.018099547511312264,
            0.054298642533936681,
            0.75263951734539969,
            0.12971342383107087,
            0.1206636500754148,
            0.14177978883861242,
            0.16289592760180993,
            0.21116138763197589,
            0.29864253393665163,
            0.3831070889894419,
            0.48567119155354455,
            0.60482654600301666,
            0.74811463046757165,
            0,
        ],
        [
            0,
            0,
            0.036199095022624417,
            0.075414781297134192,
            0.12971342383107087,
            0.86576168929110109,
            0.17797888386123684,
            0.20211161387631971,
            0.22624434389140269,
            0.27149321266968329,
            0.31372549019607843,
            0.40723981900452488,
            0.51583710407239813,
            0.63197586726998489,
            0.79185520361990946,
            0,
        ],
        [
            0,
            0,
            0.02714932126696834,
            0.066365007541478116,
            0.1206636500754148,
            0.17797888386123684,
            0.92156862745098045,
            0.25037707390648567,
            0.28657616892911009,
            0.33182503770739069,
            0.37405731523378583,
            0.43438914027149322,
            0.55354449472096534,
            0.66666666666666674,
            0.78280542986425339,
            0,
        ],
        [
            0,
            0,
            0.045248868778280493,
            0.08446455505279038,
            0.14177978883861242,
            0.20211161387631971,
            0.25037707390648567,
            0.96530920060331826,
            0.34690799396681749,
            0.39517345399698345,
            0.4434389140271493,
            0.49472096530920062,
            0.58974358974358976,
            0.69079939668174961,
            0.82503770739064852,
            0,
        ],
        [
            0,
            0,
            0.093514328808446456,
            0.10558069381598789,
            0.16289592760180993,
            0.22624434389140269,
            0.28657616892911009,
            0.34690799396681749,
            0.97285067873303166,
            0.45550527903469085,
            0.5037707390648567,
            0.57164404223227749,
            0.64102564102564097,
            0.73604826546003022,
            0.8491704374057315,
            0,
        ],
        [
            0,
            0,
            0.15384615384615385,
            0.18702865761689291,
            0.21116138763197589,
            0.27149321266968329,
            0.33182503770739069,
            0.39517345399698345,
            0.45550527903469085,
            0.9773755656108597,
            0.58069381598793357,
            0.62292609351432882,
            0.70889894419306176,
            0.80090497737556565,
            0.88386123680241324,
            0,
        ],
        [
            0,
            0,
            0.23831070889894423,
            0.26244343891402711,
            0.29864253393665163,
            0.31372549019607843,
            0.37405731523378583,
            0.4434389140271493,
            0.5037707390648567,
            0.58069381598793357,
            0.98190045248868774,
            0.69984917043740569,
            0.76168929110105577,
            0.84012066365007543,
            0.91402714932126694,
            0,
        ],
        [
            0,
            0,
            0.3227752639517345,
            0.35595776772247356,
            0.3831070889894419,
            0.40723981900452488,
            0.43438914027149322,
            0.49472096530920062,
            0.57164404223227749,
            0.62292609351432882,
            0.69984917043740569,
            0.98642533936651589,
            0.80995475113122173,
            0.87481146304675717,
            0.93363499245852188,
            0,
        ],
        [
            0,
            0,
            0.41930618401206632,
            0.46455505279034692,
            0.48567119155354455,
            0.51583710407239813,
            0.55354449472096534,
            0.58974358974358976,
            0.64102564102564097,
            0.70889894419306176,
            0.76168929110105577,
            0.80995475113122173,
            0.99095022624434392,
            0.89592760180995479,
            0.94268476621417796,
            0,
        ],
        [
            0,
            0,
            0.53242835595776772,
            0.56259426847662142,
            0.60482654600301666,
            0.63197586726998489,
            0.66666666666666674,
            0.69079939668174961,
            0.73604826546003022,
            0.80090497737556565,
            0.84012066365007543,
            0.87481146304675717,
            0.89592760180995479,
            0.99547511312217196,
            0.95475113122171951,
            0,
        ],
        [
            0,
            0,
            0.68174962292609353,
            0.72398190045248867,
            0.74811463046757165,
            0.79185520361990946,
            0.78280542986425339,
            0.82503770739064852,
            0.8491704374057315,
            0.88386123680241324,
            0.91402714932126694,
            0.93363499245852188,
            0.94268476621417796,
            0.95475113122171951,
            1.0,
            0,
        ],
    ]

    suited_ranks_to_percentile = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [
            0,
            0,
            0,
            0.05731523378582204,
            0.096530920060331815,
            0.11161387631975872,
            0.10859728506787325,
            0.13273001508295623,
            0.19306184012066363,
            0.25339366515837103,
            0.33785822021116141,
            0.42232277526395179,
            0.51885369532428349,
            0.61387631975867274,
            0.76470588235294112,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0.6,  # 43 suited
            0.16892911010558065,
            0.16591251885369529,
            0.19004524886877827,
            0.21417797888386125,
            0.28959276018099545,
            0.36199095022624439,
            0.46757164404223228,
            0.54449472096530926,
            0.65761689291101055,
            0.81297134238310709,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0.22926093514328805,
            0.21719457013574661,
            0.24132730015082959,
            0.27450980392156865,
            0.30467571644042235,
            0.39819004524886881,
            0.473604826546003,
            0.59276018099547512,
            0.67269984917043746,
            0.82805429864253388,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0.80,  # 65 suited
            0.30165912518853699,
            0.33484162895927605,
            0.36500754147812975,
            0.41025641025641024,
            0.50678733031674206,
            0.61085972850678738,
            0.71493212669683259,  # K5 suited
            0.85520361990950222,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.85,  # 67 suited
            0.38612368024132726,
            0.42533936651583715,
            0.47058823529411764,
            0.53544494720965308,
            0.64404223227752633,
            0.73906485671191557,
            0.85218702865761686,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.90,  # 78 suited
            0.47662141779788836,
            0.53846153846153844,
            0.59577677224736048,
            0.6696832579185521,
            0.77073906485671195,
            0.8868778280542986,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.9,  # 89 suited
            0.7,  # T8 suited
            0.7,  # J8 suited
            0.72699849170437414,
            0.81598793363499245,
            0.90196078431372551,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.9,  # T9 suited
            0.71191553544494723,
            0.77375565610859731,
            0.85822021116138769,
            0.9170437405731523,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.9,  # Jack Ten suited
            0.83107088989441924,
            0.89894419306184015,
            0.94570135746606332,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.86123680241327305,
            0.90497737556561086,
            0.95776772247360487,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.92458521870286581,
            0.96078431372549022,
            0,
        ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.96832579185520362, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def evaluate_percentile(self, hand):
        if hand[0].suit == hand[1].suit:
            if hand[0].rank < hand[1].rank:
                return self.suited_ranks_to_percentile[hand[0].rank][hand[1].rank]
            else:
                return self.suited_ranks_to_percentile[hand[1].rank][hand[0].rank]
        else:
            return self.unsuited_ranks_to_percentile[hand[0].rank][hand[1].rank]

    def get_hand_strength(self, left_card, right_card):
        try:
            left_score = self.get_card_value(left_card)
            left_suit = self.get_suit_value(left_card)

            right_score = self.get_card_value(right_card)
            right_suit = self.get_suit_value(right_card)

            hole = [Card(left_score, left_suit), Card(right_score, right_suit)]

            score = self.evaluate_percentile(hole)

            return score
        except:
            return 0
