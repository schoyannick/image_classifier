from enum import Enum
from image_classifier.card_classifier import img_height, img_width
from PIL import ImageGrab
import tensorflow as tf
import numpy as np
import os
import time


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
    left_card: Card

    card_model: any
    card_class_names: any
    dealer_button_pos: any

    def __init__(
        self,
        left_card_pos,
        right_card_pos,
        dealer_button_pos,
        card_model,
        card_class_names,
    ):
        self.left_card_pos = left_card_pos
        self.right_card_pos = right_card_pos
        self.dealer_button_pos = dealer_button_pos
        self.card_model = card_model
        self.card_class_names = card_class_names

    def check_image(self, isLeft, i):
        img_path = "desktop/{}.png".format(i)
        card_pos = self.left_card_pos if isLeft else self.right_card_pos
        snapshot = ImageGrab.grab(card_pos)
        snapshot.save(img_path)
        img = tf.keras.utils.load_img(img_path, target_size=(img_height, img_width))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = self.card_model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        if self.card_class_names[np.argmax(score)] != "NoCard":
            img_path2 = "desktop/{}-{}.png".format(
                self.card_class_names[np.argmax(score)], i
            )
            snapshot.save(img_path2)

        os.remove(img_path)
        # print(
        #     "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
        #         class_names[np.argmax(score)], 100 * np.max(score)
        #     )
        # )

    def take_screen_shots():
        i = 1
        while True:
            game_path_left = "desktop/gameNew-{}.png".format(i)
            i += 1
            snapshot_left = ImageGrab.grab(bbox=(559, 386, 595, 430))
            snapshot_left.save(game_path_left)

            game_path_right = "desktop/gameNew-{}.png".format(i)
            i += 1
            snapshot_right = ImageGrab.grab(bbox=(598, 386, 634, 430))
            snapshot_right.save(game_path_right)
            time.sleep(6)
