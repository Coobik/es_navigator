label esnav_day2:
    scene bg ext_house_of_mt_day

    menu:
        "< BACK":
            jump es_navigator

        "Day 2 - wake up":
            jump day2_main1

        "Day 2 - checklist":
            jump esnav_day2_checklist

        "Day 2 - checklist complete!":
            jump day2_main2

        "Day 2 - before card game":
            jump esnav_day2_before_cards

        "Day 2 - card game":
            jump esnav_day2_card_game

        "Day 2 - after card game":
            jump day2_main3

        "Day 2 - evening":
            jump esnav_day2_eve

        "Day 2 - evening with the girls":
            jump esnav_day2_girls_eve

        "Day 2 - night":
            jump day2_main4


label esnav_day2_checklist:
    scene bg ext_square_day

    menu:
        "< BACK":
            jump esnav_day2

        "Day 2 - music club":
            jump day2_musclub

        "Day 2 - cyber club":
            jump day2_clubs

        "Day 2 - library":
            jump day2_library

        "Day 2 - first aid post":
            jump day2_aidpost

        "Day 2 - dinner":
            jump day2_dinner


label esnav_day2_before_cards:
    scene bg ext_dining_hall_near_day

    menu:
        "< BACK":
            jump esnav_day2

        "Day 2 - fetch cards with Slavya":
            jump day2_cards_with_sl

        "Day 2 - fetch cards without Slavya":
            jump day2_cards_without_sl

        "Day 2 - bet with Alice":
            jump day2_pre_cards

        "Day 2 - before card game":
            jump day2_cards


label esnav_day2_card_game:
    scene bg int_dining_hall_sunset

    menu:
        "< BACK":
            jump esnav_day2

        "Day 2 - card game":
            jump day2_cardgame

        "Day 2 - demo play":
            jump demo_play

        "Day 2 - card game continue":
            jump day_2_cards_continue

        "Day 2 - play cards with Lena":
            jump un_play

        "Day 2 - play cards with Ulyana":
            jump us_play

        "Day 2 - play cards with Ulyana again":
            jump us2_play

        "Day 2 - play cards with Alice":
            jump dv_play


label esnav_day2_eve:
    scene bg ext_square_night

    menu:
        "< BACK":
            jump esnav_day2

        "Day2 - first aid post - evening":
            jump day2_aidpost_eve

        "Day2 - square - evening":
            jump day2_square_eve

        "Day2 - beach - evening":
            jump day2_beach_eve

        "Day2 - dock - evening":
            jump day2_dock_eve

        "Day2 - bus stop - evening":
            jump day2_busstop_eve

        "Day2 - stage - evening":
            jump day2_stage_eve

        "Day2 - football - evening":
            jump day2_football_eve


label esnav_day2_girls_eve:
    scene bg ext_beach_night:

    menu:
        "< BACK":
            jump esnav_day2

        "Day 2 - evening with Alice":
            $ day2_card_result == 3
            $ day2_dv_bet == 1
            $ lp_dv = 5
            jump day2_dv

        "Day 2 - evening with Slavya":
            $ day2_cards_with_sl == 1
            $ lp_sl = 3
            jump day2_sl

        "Day 2 - evening with Lena":
            $ day2_dv_bet == 0
            $ day2_card_result == 0
            $ lp_un = 3
            jump day2_un

        "Day 2 - evening with Ulyana":
            $ day2_card_result == 1
            $ lp_us = 3
            jump day2_us
