import time
from PIL import ImageGrab
from image_classifier.card_classifier import CardClassifier
from image_classifier.bet_button_classifier import BetButtonClassifier
from image_classifier.dealer_button_classifier import DealerButtonClassifier

from table import Table
import random

# def take_screen_shots():
#     i = 1
#     while 1:
#         img_path1 = "temp/button-{}.png".format(i)
#         snapshot = ImageGrab.grab(bbox=(710, 445, 830, 510))
#         snapshot.save(img_path1)
#         i += 1

#         snapshot2 = ImageGrab.grab(bbox=(835, 445, 955, 510))
#         img_path2 = "temp/button-{}.png".format(i)
#         snapshot2.save(img_path2)
#         i += 1

#         time.sleep(6)


(bet_button_model, bet_button_class_names) = BetButtonClassifier().train()
(card_model, card_class_names) = CardClassifier().train()
(dealer_button_model, dealer_button_class_names) = DealerButtonClassifier().train()

table1_left_card_pos = (559, 386, 595, 430)
table1_right_card_pos = (598, 386, 634, 430)

table1_fold_pos = (710, 445, 830, 510)
table1_call_pos = (835, 445, 955, 510)

table1_top_dealer_pos = (570, 140, 590, 170)
table1_right_dealer_pos = (835, 270, 855, 300)
table1_bottom_dealer_pos = (545, 355, 565, 385)
table1_left_dealer_pos = (350, 270, 370, 300)

table1 = Table(
    table1_left_card_pos,
    table1_right_card_pos,
    card_model,
    card_class_names,
    table1_fold_pos,
    table1_call_pos,
    table1_top_dealer_pos,
    table1_right_dealer_pos,
    table1_bottom_dealer_pos,
    table1_left_dealer_pos,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
)

while 1:
    table1.handle_action()
    time.sleep(random.uniform(1, 3))
