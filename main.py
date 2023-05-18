import time
from PIL import ImageGrab
import pyautogui
from image_classifier.card_classifier import CardClassifier
from image_classifier.bet_button_classifier import BetButtonClassifier
from image_classifier.dealer_button_classifier import DealerButtonClassifier
from image_classifier.my_turn_classifier import MyTurnClassifier
from image_classifier.action_classifier import ActionClassifier

from table_config import TableConfig
import random


# pos = (582, 142, 635, 195)
# img_path = "temp/left.png"
# snapshot = ImageGrab.grab(bbox=pos)
# snapshot.save(img_path)


# (card_model, card_class_names) = CardClassifier().train()
card_class_names = CardClassifier().load_class_names()
card_model = CardClassifier().load_model()

# (bet_button_model, bet_button_class_names) = BetButtonClassifier().train()
bet_button_model = BetButtonClassifier().load_model()
bet_button_class_names = BetButtonClassifier().load_class_names()

# (dealer_button_model, dealer_button_class_names) = DealerButtonClassifier().train()
dealer_button_model = DealerButtonClassifier().load_model()
dealer_button_class_names = DealerButtonClassifier().load_class_names()

# (my_turn_model, my_turn_class_names) = MyTurnClassifier().train()
my_turn_model = MyTurnClassifier().load_model()
my_turn_class_names = MyTurnClassifier().load_class_names()

# (action_model, action_class_names) = ActionClassifier().train()
action_model = ActionClassifier().load_model()
action_class_names = ActionClassifier().load_class_names()

table_config = TableConfig()
table1 = table_config.get_table_1(
    card_model,
    card_class_names,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
    my_turn_model,
    my_turn_class_names,
    action_model,
    action_class_names,
)

table2 = table_config.get_table_2(
    card_model,
    card_class_names,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
    my_turn_model,
    my_turn_class_names,
    action_model,
    action_class_names,
)

table3 = table_config.get_table_3(
    card_model,
    card_class_names,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
    my_turn_model,
    my_turn_class_names,
    action_model,
    action_class_names,
)

table4 = table_config.get_table_4(
    card_model,
    card_class_names,
    dealer_button_model,
    dealer_button_class_names,
    bet_button_model,
    bet_button_class_names,
    my_turn_model,
    my_turn_class_names,
    action_model,
    action_class_names,
)

while 1:
    if random.random() > 0.4:
        table1.handle_action()
        time.sleep(random.uniform(0.1, 0.15))
        table2.handle_action()
        time.sleep(random.uniform(0.2, 0.2))
        table3.handle_action()
        time.sleep(random.uniform(0.1, 0.3))
        table4.handle_action()
    else:
        table3.handle_action()
        time.sleep(random.uniform(0.1, 0.25))
        table2.handle_action()
        time.sleep(random.uniform(0.1, 0.2))
        table4.handle_action()
        time.sleep(random.uniform(0, 0.1))
        table1.handle_action()
