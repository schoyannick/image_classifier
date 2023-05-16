from enum import Enum
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
from PIL import ImageGrab
import tensorflow as tf
import numpy as np
import os
import time


class DealerPosition(Enum):
    BUTTON = 1
    BIG_BLIND = 2
    SMALL_BLIND = 3
    UTG = 4


class Suit(Enum):
    CLUB = "CLUB"
    HEART = "HEART"
    SPADE = "SPADE"
    DIAMOND = "DIAMOND"


class Card:
    suit: Suit
    type: int
    full_name = ""

    def __init__(self, suit, type, image) -> None:
        self.suit = suit
        self.type = type
        self.image = image


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

    def handle_action(self):
        # get my position
        my_table_position = self.get_dealer_position()
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

            print(self.card_class_names[np.argmax(left_score)])

            right_score = self.get_image_score(
                "temp/right_card.png",
                self.right_card_pos,
                card_img_height,
                card_img_width,
                self.card_model,
            )

            print(self.card_class_names[np.argmax(right_score)])

            self.check_image(True, self.i)
            self.i += 1
            self.check_image(False, self.i)
            self.i += 1

    def check_image(self, isLeft, i):
        img_path = "temp/{}.png".format(i)
        card_pos = self.left_card_pos if isLeft else self.right_card_pos
        snapshot = ImageGrab.grab(card_pos)
        snapshot.save(img_path)
        img = tf.keras.utils.load_img(
            img_path, target_size=(card_img_height, card_img_width)
        )
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = self.card_model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        if self.card_class_names[np.argmax(score)] != "NoCard":
            img_path2 = "temp/{}-{}.png".format(
                self.card_class_names[np.argmax(score)], i
            )
            snapshot.save(img_path2)

        os.remove(img_path)
        # print(
        #     "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
        #         class_names[np.argmax(score)], 100 * np.max(score)
        #     )
        # )

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
