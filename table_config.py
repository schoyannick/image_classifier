from table import Table


class TableConfig:
    def get_table_1(
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
    ):
        table1_left_card_pos = (559, 386, 595, 430)
        table1_right_card_pos = (598, 386, 634, 430)

        table1_my_turn_pos = (550, 488, 650, 510)

        table1_top_action_pos = (582, 142, 635, 195)
        table1_right_action_pos = (797, 230, 850, 283)
        table1_left_action_pos = (356, 225, 409, 278)

        table1_fold_pos = (710, 445, 830, 510)
        table1_call_pos = (835, 445, 955, 510)

        table1_top_dealer_pos = (570, 140, 590, 170)
        table1_right_dealer_pos = (835, 270, 855, 300)
        table1_bottom_dealer_pos = (545, 355, 565, 385)
        table1_left_dealer_pos = (350, 270, 370, 300)

        return Table(
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
            table1_my_turn_pos,
            my_turn_model,
            my_turn_class_names,
            action_model,
            action_class_names,
            table1_top_action_pos,
            table1_right_action_pos,
            table1_left_action_pos,
        )

    def get_table_2(
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
    ):
        table2_left_card_pos = (1271, 386, 1307, 430)
        table2_right_card_pos = (1310, 386, 1346, 430)

        table2_my_turn_pos = (
            table2_left_card_pos[0] - 9,
            table2_left_card_pos[1] + 102,
            table2_left_card_pos[2] + 55,
            table2_left_card_pos[3] + 80,
        )

        table2_top_action_pos = (
            table2_left_card_pos[0] + 23,
            table2_left_card_pos[1] - 244,
            table2_left_card_pos[2] + 40,
            table2_left_card_pos[3] - 235,
        )
        table2_right_action_pos = (
            table2_left_card_pos[0] + 238,
            table2_left_card_pos[1] - 156,
            table2_left_card_pos[2] + 255,
            table2_left_card_pos[3] - 147,
        )
        table2_left_action_pos = (
            table2_left_card_pos[0] - 203,
            table2_left_card_pos[1] - 161,
            table2_left_card_pos[2] - 186,
            table2_left_card_pos[3] - 152,
        )

        table2_fold_pos = (1422, 445, 1542, 510)
        table2_call_pos = (1547, 445, 1667, 510)

        table2_top_dealer_pos = (1284, 140, 1304, 170)
        table2_right_dealer_pos = (
            table2_top_dealer_pos[0] + 265,
            table2_top_dealer_pos[1] + 130,
            table2_top_dealer_pos[0] + 265 + 20,
            table2_top_dealer_pos[1] + 130 + 30,
        )
        table2_bottom_dealer_pos = (
            table2_top_dealer_pos[0] - 25,
            table2_top_dealer_pos[1] + 215,
            table2_top_dealer_pos[0] - 25 + 20,
            table2_top_dealer_pos[1] + 215 + 30,
        )
        table2_left_dealer_pos = (
            table2_top_dealer_pos[0] - 220,
            table2_top_dealer_pos[1] + 130,
            table2_top_dealer_pos[0] - 220 + 20,
            table2_top_dealer_pos[1] + 130 + 30,
        )

        return Table(
            table2_left_card_pos,
            table2_right_card_pos,
            card_model,
            card_class_names,
            table2_fold_pos,
            table2_call_pos,
            table2_top_dealer_pos,
            table2_right_dealer_pos,
            table2_bottom_dealer_pos,
            table2_left_dealer_pos,
            dealer_button_model,
            dealer_button_class_names,
            bet_button_model,
            bet_button_class_names,
            table2_my_turn_pos,
            my_turn_model,
            my_turn_class_names,
            action_model,
            action_class_names,
            table2_top_action_pos,
            table2_right_action_pos,
            table2_left_action_pos,
        )

    def get_table_3(
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
    ):
        table3_left_card_pos = (559, 906, 595, 950)
        table3_right_card_pos = (
            table3_left_card_pos[0] + 39,
            table3_left_card_pos[1],
            table3_left_card_pos[2] + 39,
            table3_left_card_pos[3],
        )

        table3_my_turn_pos = (
            table3_left_card_pos[0] - 9,
            table3_left_card_pos[1] + 102,
            table3_left_card_pos[2] + 55,
            table3_left_card_pos[3] + 80,
        )

        table3_top_action_pos = (
            table3_left_card_pos[0] + 23,
            table3_left_card_pos[1] - 244,
            table3_left_card_pos[2] + 40,
            table3_left_card_pos[3] - 235,
        )
        table3_right_action_pos = (
            table3_left_card_pos[0] + 238,
            table3_left_card_pos[1] - 156,
            table3_left_card_pos[2] + 255,
            table3_left_card_pos[3] - 147,
        )
        table3_left_action_pos = (
            table3_left_card_pos[0] - 203,
            table3_left_card_pos[1] - 161,
            table3_left_card_pos[2] - 186,
            table3_left_card_pos[3] - 152,
        )

        table3_fold_pos = (
            table3_left_card_pos[0] + 151,
            table3_left_card_pos[1] + 59,
            table3_left_card_pos[2] + 235,
            table3_left_card_pos[3] + 80,
        )
        table3_call_pos = (
            table3_fold_pos[0] + 125,
            table3_fold_pos[1],
            table3_fold_pos[2] + 125,
            table3_fold_pos[3],
        )

        table3_top_dealer_pos = (
            table3_left_card_pos[0] + 11,
            table3_left_card_pos[1] - 246,
            table3_left_card_pos[2] - 5,
            table3_left_card_pos[3] - 260,
        )
        table3_right_dealer_pos = (
            table3_top_dealer_pos[0] + 265,
            table3_top_dealer_pos[1] + 130,
            table3_top_dealer_pos[0] + 265 + 20,
            table3_top_dealer_pos[1] + 130 + 30,
        )
        table3_bottom_dealer_pos = (
            table3_top_dealer_pos[0] - 25,
            table3_top_dealer_pos[1] + 215,
            table3_top_dealer_pos[0] - 25 + 20,
            table3_top_dealer_pos[1] + 215 + 30,
        )
        table3_left_dealer_pos = (
            table3_top_dealer_pos[0] - 220,
            table3_top_dealer_pos[1] + 130,
            table3_top_dealer_pos[0] - 220 + 20,
            table3_top_dealer_pos[1] + 130 + 30,
        )

        return Table(
            table3_left_card_pos,
            table3_right_card_pos,
            card_model,
            card_class_names,
            table3_fold_pos,
            table3_call_pos,
            table3_top_dealer_pos,
            table3_right_dealer_pos,
            table3_bottom_dealer_pos,
            table3_left_dealer_pos,
            dealer_button_model,
            dealer_button_class_names,
            bet_button_model,
            bet_button_class_names,
            table3_my_turn_pos,
            my_turn_model,
            my_turn_class_names,
            action_model,
            action_class_names,
            table3_top_action_pos,
            table3_right_action_pos,
            table3_left_action_pos,
        )

    def get_table_4(
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
    ):
        table4_left_card_pos = (1271, 906, 1307, 950)
        table4_right_card_pos = (
            table4_left_card_pos[0] + 39,
            table4_left_card_pos[1],
            table4_left_card_pos[2] + 39,
            table4_left_card_pos[3],
        )

        table4_my_turn_pos = (
            table4_left_card_pos[0] - 9,
            table4_left_card_pos[1] + 102,
            table4_left_card_pos[2] + 55,
            table4_left_card_pos[3] + 80,
        )

        table4_top_action_pos = (
            table4_left_card_pos[0] + 23,
            table4_left_card_pos[1] - 244,
            table4_left_card_pos[2] + 40,
            table4_left_card_pos[3] - 235,
        )
        table4_right_action_pos = (
            table4_left_card_pos[0] + 238,
            table4_left_card_pos[1] - 156,
            table4_left_card_pos[2] + 255,
            table4_left_card_pos[3] - 147,
        )
        table4_left_action_pos = (
            table4_left_card_pos[0] - 203,
            table4_left_card_pos[1] - 161,
            table4_left_card_pos[2] - 186,
            table4_left_card_pos[3] - 152,
        )

        table4_fold_pos = (
            table4_left_card_pos[0] + 151,
            table4_left_card_pos[1] + 59,
            table4_left_card_pos[2] + 235,
            table4_left_card_pos[3] + 80,
        )
        table4_call_pos = (
            table4_fold_pos[0] + 125,
            table4_fold_pos[1],
            table4_fold_pos[2] + 125,
            table4_fold_pos[3],
        )

        table4_top_dealer_pos = (
            table4_left_card_pos[0] + 11,
            table4_left_card_pos[1] - 246,
            table4_left_card_pos[2] - 5,
            table4_left_card_pos[3] - 260,
        )
        table4_right_dealer_pos = (
            table4_top_dealer_pos[0] + 265,
            table4_top_dealer_pos[1] + 130,
            table4_top_dealer_pos[0] + 265 + 20,
            table4_top_dealer_pos[1] + 130 + 30,
        )
        table4_bottom_dealer_pos = (
            table4_top_dealer_pos[0] - 25,
            table4_top_dealer_pos[1] + 215,
            table4_top_dealer_pos[0] - 25 + 20,
            table4_top_dealer_pos[1] + 215 + 30,
        )
        table3_left_dealer_pos = (
            table4_top_dealer_pos[0] - 220,
            table4_top_dealer_pos[1] + 130,
            table4_top_dealer_pos[0] - 220 + 20,
            table4_top_dealer_pos[1] + 130 + 30,
        )

        return Table(
            table4_left_card_pos,
            table4_right_card_pos,
            card_model,
            card_class_names,
            table4_fold_pos,
            table4_call_pos,
            table4_top_dealer_pos,
            table4_right_dealer_pos,
            table4_bottom_dealer_pos,
            table3_left_dealer_pos,
            dealer_button_model,
            dealer_button_class_names,
            bet_button_model,
            bet_button_class_names,
            table4_my_turn_pos,
            my_turn_model,
            my_turn_class_names,
            action_model,
            action_class_names,
            table4_top_action_pos,
            table4_right_action_pos,
            table4_left_action_pos,
        )
