from table import Table


class TableConfig:
    def get_config(
        self,
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
        left_card_pos,
    ):
        right_card_pos = (
            left_card_pos[0] + 39,
            left_card_pos[1],
            left_card_pos[2] + 39,
            left_card_pos[3],
        )

        my_turn_pos = (
            left_card_pos[0] - 9,
            left_card_pos[1] + 102,
            left_card_pos[2] + 55,
            left_card_pos[3] + 80,
        )

        top_action_pos = (
            left_card_pos[0] + 23,
            left_card_pos[1] - 244,
            left_card_pos[2] + 40,
            left_card_pos[3] - 235,
        )
        right_action_pos = (
            left_card_pos[0] + 238,
            left_card_pos[1] - 156,
            left_card_pos[2] + 255,
            left_card_pos[3] - 147,
        )
        left_action_pos = (
            left_card_pos[0] - 203,
            left_card_pos[1] - 161,
            left_card_pos[2] - 186,
            left_card_pos[3] - 152,
        )

        fold_pos = (
            left_card_pos[0] + 151,
            left_card_pos[1] + 59,
            left_card_pos[2] + 235,
            left_card_pos[3] + 80,
        )
        call_pos = (
            fold_pos[0] + 125,
            fold_pos[1],
            fold_pos[2] + 125,
            fold_pos[3],
        )

        top_dealer_pos = (
            left_card_pos[0] + 11,
            left_card_pos[1] - 246,
            left_card_pos[2] - 5,
            left_card_pos[3] - 260,
        )
        right_dealer_pos = (
            top_dealer_pos[0] + 265,
            top_dealer_pos[1] + 130,
            top_dealer_pos[0] + 265 + 20,
            top_dealer_pos[1] + 130 + 30,
        )
        bottom_dealer_pos = (
            top_dealer_pos[0] - 25,
            top_dealer_pos[1] + 215,
            top_dealer_pos[0] - 25 + 20,
            top_dealer_pos[1] + 215 + 30,
        )
        left_dealer_pos = (
            top_dealer_pos[0] - 220,
            top_dealer_pos[1] + 130,
            top_dealer_pos[0] - 220 + 20,
            top_dealer_pos[1] + 130 + 30,
        )

        im_back_button_pos = (
            left_card_pos[0] - 114,
            left_card_pos[1] - 66,
            left_card_pos[2] - 30,
            left_card_pos[3] - 45,
        )
        return Table(
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
            im_back_button_pos,
        )
