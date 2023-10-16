label esnav_day3:
    scene bg ext_washstand2_day

    menu:
        "< BACK":
            jump es_navigator

        "Day 3 - wake up":
            jump day3_main1

        "Day 3 - breakfast":
            jump esnav_day3_breakfast

        "Day 3 - after breakfast":
            jump day3_main2

        "Day 3 - first aid post - help":
            jump esnav_day3_help

        "Day 3 - hear guitar sounds":
            jump day3_main3

        "Day 3 - roam the camp":
            jump esnav_day3_camp

        "Day 3 - dinner":
            jump day3_main4

        "Day 3 - after dinner":
            jump esnav_day3_eve

        "Day 3 - supper":
            jump day3_main5

        "Day 3 - evening with the girls":
            jump esnav_day3_girls_eve

        "Day 3 - lonely evening":
            $ day3_got_fail = 1
            jump day3_fail


label esnav_day3_breakfast:
    scene bg int_dining_hall_day

    menu:
        "< BACK":
            jump esnav_day3

        "Day 3 - breakfast with Lena":
            $ day3_breakfast_with_un = 1
            $ lp_un = 4
            jump day3_breakfast_un

        "Day 3 - breakfast with Zhenya":
            jump day3_breakfast_mz


label esnav_day3_help:
    scene bg ext_aidpost_day

    menu:
        "< BACK":
            jump esnav_day3

        "Day 3 - agree to help Lena at the first aid post":
            $ day3_un_help_accept = 1
            $ lp_un = 5
            jump day3_helpaccept

        "Day 3 - do not agree to help Lena":
            jump day3_helpreject


label esnav_day3_camp:
    scene bg ext_square_day

    menu:
        "< BACK":
            jump esnav_day3

        "Day 3 - talk to Olga in her house":
            $ day3_house_of_mt = 1
            jump day3_house_of_mt

        "Day 3 - clean up the square with Slavya":
            $ day3_sl_cleaned = 1
            $ lp_sl = 4
            jump day3_square

        "Day 3 - visit cyber club":
            jump day3_clubs

        "Day 3 - play football with Ulyana":
            $ day3_us_football = 1
            $ lp_us = 4
            jump day3_playground_us

        "Day 3 - watch Alice play guitar":
            $ lp_dv = 6
            jump day3_stage_dv


label esnav_day3_eve:
    scene bg ext_dining_hall_near_day

    menu:
        "< BACK":
            jump esnav_day3

        "Day 3 - help Slavya at the library":
            $ day3_sl_library = 1
            $ lp_sl = 5
            jump day3_library_sl

        "Day 3 - help Ulyana clean up the canteen":
            $ day3_us_cleaned = 1
            $ lp_us = 5
            jump day3_cleaning_us


label esnav_day3_girls_eve:
    scene bg ext_square_night_party

    menu:
        "< BACK":
            jump esnav_day3

        "Day 3 - evening with Slavya":
            $ day3_sl_library = 1
            $ day3_sl_cleaned = 1
            $ lp_sl = 5
            jump day3_evening_sl

        "Day 3 - evening with Lena":
            $ day3_un_dumped = False
            $ day3_un_help_accept = 1
            $ lp_un = 5
            $ day2_un = 1
            jump day3_evening_un

        "Day 3 - evening with Ulyana":
            $ day3_us_cleaned = 1
            $ day3_us_football = 1
            $ lp_us = 5
            jump day3_evening_us

        "Day 3 - evening with Alice":
            $ day3_dv_dumped = False
            $ day3_dv_accept = 1
            $ lp_dv = 7
            jump day3_evening_dv
