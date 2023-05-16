import time

from image_classifier.card_classifier import CardClassifier

from table import Table

(card_model, card_class_names) = CardClassifier().train()


table1 = Table(
    (559, 386, 595, 430), (598, 386, 634, 430), None, card_model, card_class_names
)

i = 1
while 1:
    table1.check_image(True, i)
    i += 1
    table1.check_image(False, i)
    i += 1
    time.sleep(6)
