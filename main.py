import time
from PIL import ImageGrab
import pyautogui
from hand_strength import HandStrength
from image_classifier.card_classifier import CardClassifier
from image_classifier.bet_button_classifier import BetButtonClassifier
from image_classifier.dealer_button_classifier import DealerButtonClassifier
from image_classifier.my_turn_classifier import MyTurnClassifier
from image_classifier.action_classifier import ActionClassifier
from my_types import Card, Suit

from table_config import TableConfig
import random
import keyboard

# pos = (850, 450, 955, 520)
# img_path = "temp/0.png"
# snapshot = ImageGrab.grab(bbox=pos)
# snapshot.save(img_path)

# left_card = Card(Suit.SPADE, "Queen")
# right_card = Card(Suit.SPADE, "Ten")
# hand_strength = HandStrength()
# str = hand_strength.get_hand_strength(left_card, right_card)

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

run = True


while run:
    # if keyboard.is_pressed('f5'):
    #     run = not run

    if random.random() > 0.4:
        table1.handle_action()
        time.sleep(random.uniform(0.1, 0.15))
        table2.handle_action()
        time.sleep(random.uniform(0.2, 0.2))
        table3.handle_action()
        table4.handle_action()
    else:
        table3.handle_action()
        time.sleep(random.uniform(0.1, 0.25))
        table2.handle_action()
        table4.handle_action()
        time.sleep(random.uniform(0, 0.1))
        table1.handle_action()

    if random.random() > 0.2:
        pyautogui.moveTo(
            random.randrange(0, 1000), random.randrange(0, 1000), duration=0.5
        )
