import time
from PIL import ImageGrab
import pyautogui
from image_classifier.card_classifier import CardClassifier
from image_classifier.bet_button_classifier import BetButtonClassifier
from image_classifier.dealer_button_classifier import DealerButtonClassifier

from table_config import TableConfig
import random


# table3_left_card_pos = (1271, 906, 1307, 950)
# img_path1 = "temp/left.png"
# snapshot = ImageGrab.grab(bbox=table3_left_card_pos)
# snapshot.save(img_path1)


# (card_model, card_class_names) = CardClassifier().train()
card_class_names = CardClassifier().load_class_names()
card_model = CardClassifier().load_model()

# (bet_button_model, bet_button_class_names) = BetButtonClassifier().train()
bet_button_model = BetButtonClassifier().load_model()
bet_button_class_names = BetButtonClassifier().load_class_names()

# (dealer_button_model, dealer_button_class_names) = DealerButtonClassifier().train()
dealer_button_model = DealerButtonClassifier().load_model()
dealer_button_class_names = DealerButtonClassifier().load_class_names()


table_config = TableConfig()
table1 = table_config.get_table_1(
    card_model,
    card_class_names,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
)

table2 = table_config.get_table_2(
    card_model,
    card_class_names,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
)

table3 = table_config.get_table_3(
    card_model,
    card_class_names,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
)

table4 = table_config.get_table_4(
    card_model,
    card_class_names,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
)

while 1:
    if random.random() > 0.4:
        table1.handle_action()
        time.sleep(random.uniform(0.1, 0.4))
        table2.handle_action()
        time.sleep(random.uniform(0.2, 0.3))
        table3.handle_action()
        time.sleep(random.uniform(0.1, 0.3))
        table4.handle_action()
    else:
        table3.handle_action()
        time.sleep(random.uniform(0.2, 0.3))
        table2.handle_action()
        time.sleep(random.uniform(0.1, 0.2))
        table4.handle_action()
        time.sleep(random.uniform(0, 0.3))
        table1.handle_action()

# pyautogui.mouseInfo()
