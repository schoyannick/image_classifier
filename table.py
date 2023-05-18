from enum import Enum
import math
from image_classifier.card_classifier import (
    img_height as card_img_height,
    img_width as card_img_width,
)
from image_classifier.bet_button_classifier import (
    img_height as bet_button_img_height,
    img_width as bet_button_img_width,
)
from image_classifier.dealer_button_classifier import (
    img_height as dealer_button_img_height,
    img_width as dealer_button_img_width,
)
from image_classifier.my_turn_classifier import (
    img_height as my_turn_img_height,
    img_width as my_turn_img_width,
)
from image_classifier.action_classifier import (
    img_height as action_img_height,
    img_width as action_img_width,
)
from PIL import ImageGrab
import tensorflow as tf
import numpy as np
import os
import re
from my_types import Suit, Action
from hand_strength import HandStrength
import random
import pyautogui


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


class Table:
    left_card_pos: any
    right_card_pos: any
    fold_pos: any
    call_pos: any

    left_card: Card
    right_card: Card

    card_model: any
    card_class_names: any

    bet_button_model: any
    bet_button_class_names: any

    top_dealer_pos: any
    right_dealer_pos: any
    bottom_dealer_pos: any
    left_dealer_pos: any

    dealer_button_class_names: any
    dealer_button_model: any

    my_table_position: DealerPosition

    hand_strength: HandStrength

    my_turn_pos: any

    mouse_x = 0
    mouse_y = 0

    i = 0

    def __init__(
        self,
        left_card_pos,
        right_card_pos,
        card_model,
        card_class_names,
        fold_pos,
        call_pos,
        top_dealer_pos,
        right_dealer_pos,
        bottom_dealer_pos,
        left_dealer_pos,
        dealer_button_model,
        dealer_button_class_names,
        bet_button_model,
        bet_button_class_names,
        my_turn_pos,
        my_turn_model,
        my_turn_class_names,
        action_model,
        action_class_names,
        top_action_pos,
        right_action_pos,
        left_action_pos,
    ):
        self.left_card_pos = left_card_pos
        self.right_card_pos = right_card_pos
        self.card_model = card_model
        self.card_class_names = card_class_names
        self.fold_pos = fold_pos
        self.call_pos = call_pos
        self.bet_button_model = bet_button_model
        self.bet_button_class_names = bet_button_class_names

        self.dealer_button_model = dealer_button_model
        self.dealer_button_class_names = dealer_button_class_names

        self.top_dealer_pos = top_dealer_pos
        self.right_dealer_pos = right_dealer_pos
        self.bottom_dealer_pos = bottom_dealer_pos
        self.left_dealer_pos = left_dealer_pos

        self.my_turn_pos = my_turn_pos
        self.my_turn_model = my_turn_model
        self.my_turn_class_names = my_turn_class_names

        self.action_model = action_model
        self.action_class_names = action_class_names

        self.top_action_pos = top_action_pos
        self.right_action_pos = right_action_pos
        self.left_action_pos = left_action_pos

        self.hand_strength = HandStrength()

    def get_image_score(self, img_path, pos, height, width, model):
        snapshot = ImageGrab.grab(pos)
        snapshot.save(img_path)
        img = tf.keras.utils.load_img(img_path, target_size=(height, width))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        return score

    def get_dealer_position(self) -> DealerPosition:
        scoreTop = self.get_image_score(
            "temp/dealer_top.png",
            self.top_dealer_pos,
            dealer_button_img_height,
            dealer_button_img_width,
            self.dealer_button_model,
        )
        if self.dealer_button_class_names[np.argmax(scoreTop)] == "Dealer":
            return DealerPosition.BIG_BLIND

        scoreRight = self.get_image_score(
            "temp/dealer_right.png",
            self.right_dealer_pos,
            dealer_button_img_height,
            dealer_button_img_width,
            self.dealer_button_model,
        )
        if self.dealer_button_class_names[np.argmax(scoreRight)] == "Dealer":
            return DealerPosition.SMALL_BLIND

        scoreBottom = self.get_image_score(
            "temp/dealer_bottom.png",
            self.bottom_dealer_pos,
            dealer_button_img_height,
            dealer_button_img_width,
            self.dealer_button_model,
        )
        if self.dealer_button_class_names[np.argmax(scoreBottom)] == "Dealer":
            return DealerPosition.BUTTON

        return DealerPosition.UTG

    def get_card_enum(self, card_suit):
        if card_suit == "Heart":
            return Suit.HEART
        if card_suit == "Club":
            return Suit.CLUB
        if card_suit == "Spade":
            return Suit.SPADE
        return Suit.DIAMOND

    def get_hand_strength(self):
        if not self.left_card or not self.right_card:
            return 0
        return self.hand_strength.get_hand_strength(self.left_card, self.right_card)

    def is_my_turn(self):
        score = self.get_image_score(
            "temp/my_turn.png",
            self.my_turn_pos,
            my_turn_img_height,
            my_turn_img_width,
            self.my_turn_model,
        )

        action = self.my_turn_class_names[np.argmax(score)]

        return action == "MyTurn"

    def get_all_in_players(self):
        count = 0
        score_action_top = self.get_image_score(
            "temp/action_top.png",
            self.top_action_pos,
            action_img_height,
            action_img_width,
            self.action_model,
        )

        action_top = self.action_class_names[np.argmax(score_action_top)]
        if action_top == "AllIn":
            count += 1

        score_action_right = self.get_image_score(
            "temp/action_right.png",
            self.right_action_pos,
            action_img_height,
            action_img_width,
            self.action_model,
        )

        action_right = self.action_class_names[np.argmax(score_action_right)]
        if action_right == "AllIn":
            count += 1

        score_action_left = self.get_image_score(
            "temp/action_left.png",
            self.left_action_pos,
            action_img_height,
            action_img_width,
            self.action_model,
        )

        action_left = self.action_class_names[np.argmax(score_action_left)]
        if action_left == "AllIn":
            count += 1

        return count

    def decide_action(self) -> Action:
        strength = self.get_hand_strength()
        if strength >= 0.8 and random.random() > 0.4:
            return Action.ALL_IN

        if strength < 0.3 and random.random() > 0.4:
            return Action.FOLD
        
        my_turn = self.is_my_turn()
        if not my_turn:
            return Action.NOTHING

        if self.my_table_position == DealerPosition.UTG:
            if strength >= random.uniform(0.72, 0.74):
                return Action.ALL_IN
            else:
                return Action.FOLD

        all_in_count = self.get_all_in_players()
        if self.my_table_position == DealerPosition.BUTTON:
            match all_in_count:
                case 0:
                    if strength >= random.uniform(0.67, 0.69):
                        return Action.ALL_IN
                    else:
                        return Action.FOLD
                case 1:
                    if strength >= random.uniform(0.77, 0.8):
                        return Action.ALL_IN
                    else:
                        return Action.FOLD

        if self.my_table_position == DealerPosition.SMALL_BLIND:
            match all_in_count:
                case 0:
                    if strength >= random.uniform(0.55, 0.57):
                        return Action.ALL_IN
                    else:
                        return Action.FOLD
                case 1:
                    if strength >= random.uniform(0.75, 0.8):
                        return Action.ALL_IN
                    else:
                        return Action.FOLD
                case 2:
                    if strength >= 0.8:
                        return Action.ALL_IN
                    else:
                        return Action.FOLD

        match all_in_count:
            case 0:
                return Action.FOLD
            case 1:
                if strength >= random.uniform(0.62, 0.64):
                    return Action.ALL_IN
                else:
                    return Action.FOLD
            case 2 | 3:
                if strength >= 0.8:
                    return Action.ALL_IN
                else:
                    return Action.FOLD
        return Action.FOLD

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()

    def click_call(self):
        left, top, right, bottom = self.call_pos
        use_hot_key = random.random() < 0.4
        if use_hot_key:
            x = math.floor(
                (left + right) / 2 + random.uniform(-10, 10)
            ) - random.randint(50, 150)
            y = math.floor((top + bottom) / 2 + random.uniform(-3, 3)) - random.randint(
                150, 350
            )
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.press("f2")
        else:
            x = math.floor((left + right) / 2 + random.uniform(-10, 10))
            y = math.floor((top + bottom) / 2 + random.uniform(-3, 3))
            self.move_mouse(x, y)

    def click_fold(self):
        left, top, right, bottom = self.fold_pos
        use_hot_key = random.random() < 0.6
        if use_hot_key:
            x = math.floor(
                (left + right) / 2 + random.uniform(-10, 10)
            ) - random.randint(50, 150)
            y = math.floor((top + bottom) / 2 + random.uniform(-3, 3)) - random.randint(
                150, 350
            )
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.press("f1")
        else:
            x = math.floor((left + right) / 2 + random.uniform(-10, 10))
            y = math.floor((top + bottom) / 2 + random.uniform(-3, 3))
            self.move_mouse(x, y)

    def handle_action(self):
        self.my_table_position = self.get_dealer_position()
        call_button = self.get_action_button(True)
        fold_button = self.get_action_button(False)

        if call_button == "AllIn" and fold_button == "Fold":
            left_score = self.get_image_score(
                "temp/left_card.png",
                self.left_card_pos,
                card_img_height,
                card_img_width,
                self.card_model,
            )

            left_card_name = self.card_class_names[np.argmax(left_score)]
            split_left_card = re.findall("[A-Z][^A-Z]*", left_card_name)
            self.left_card = Card(
                self.get_card_enum(split_left_card[0]), split_left_card[1]
            )

            right_score = self.get_image_score(
                "temp/right_card.png",
                self.right_card_pos,
                card_img_height,
                card_img_width,
                self.card_model,
            )

            right_card_name = self.card_class_names[np.argmax(right_score)]
            split_right_card = re.findall("[A-Z][^A-Z]*", right_card_name)
            self.right_card = Card(
                self.get_card_enum(split_right_card[0]), split_right_card[1]
            )

            if (
                self.left_card.card_type == "Card"
                or self.right_card.card_type == "Card"
            ):
                self.left_card = None
                self.right_card = None
                return

            # self.check_image(True, self.i)
            # self.i += 1
            # self.check_image(False, self.i)
            # self.i += 1

            my_action = self.decide_action()

            if my_action == Action.NOTHING:
                return

            # img_path = "temp/bet-{}.png".format(self.i)
            # snapshot = ImageGrab.grab(bbox=self.left_action_pos)
            # snapshot.save(img_path)
            # self.i += 1

            # img_path = "temp/bet-{}.png".format(self.i)
            # snapshot = ImageGrab.grab(bbox=self.right_action_pos)
            # snapshot.save(img_path)
            # self.i += 1

            # img_path = "temp/bet-{}.png".format(self.i)
            # snapshot = ImageGrab.grab(bbox=self.top_action_pos)
            # snapshot.save(img_path)
            # self.i += 1

            if my_action == Action.ALL_IN:
                self.click_call()
            else:
                self.click_fold()

            if random.random() > 0.4:
                pyautogui.moveTo(random.randrange(300, 800), random.randrange(100, 700))

    # def check_image(self, isLeft, i):
    #     img_path = "temp/{}.png".format(i)
    #     card_pos = self.left_card_pos if isLeft else self.right_card_pos
    #     snapshot = ImageGrab.grab(card_pos)
    #     snapshot.save(img_path)
    #     img = tf.keras.utils.load_img(
    #         img_path, target_size=(card_img_height, card_img_width)
    #     )
    #     img_array = tf.keras.utils.img_to_array(img)
    #     img_array = tf.expand_dims(img_array, 0)

    #     predictions = self.card_model.predict(img_array)
    #     score = tf.nn.softmax(predictions[0])

    #     # if self.card_class_names[np.argmax(score)] != "NoCard":
    #     #     img_path2 = "temp/{}-{}.png".format(
    #     #         self.card_class_names[np.argmax(score)], i
    #     #     )
    #     #     snapshot.save(img_path2)

    #     os.remove(img_path)

    def get_action_button(self, is_call_button):
        img_path = "temp/{}.png".format("call" if is_call_button else "fold")
        pos = self.call_pos if is_call_button else self.fold_pos
        score = self.get_image_score(
            img_path,
            pos,
            bet_button_img_height,
            bet_button_img_width,
            self.bet_button_model,
        )

        return self.bet_button_class_names[np.argmax(score)]
