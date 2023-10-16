label esnav_day4_morning:
    scene bg int_house_of_mt_day

    menu:
        "< BACK":
            jump esnav_day4

        "Day 4 - wake up after evening with the girls":
            jump day4_std_morning

        "Day 4 - wake up after lonely evening":
            jump day4_fail_morning

        "Day 4 - wake up in the library with Ulyana":
            $ day3_us_evening = 1
            $ lp_us = 5
            jump day4_us_morning


label esnav_day4_search_in_camp:
    scene bg ext_square_day

    menu:
        "< BACK":
            jump esnav_day4

        "Day 4 - look at the map":
            jump day4_map

        "Day 4 - meet Miku at the bus stop":
            jump day4_busstop

        "Day 4 - meet Electronic in the forest":
            jump day4_forest

        "Day 4 - meet Slavya in the house":
            jump day4_house_of_mt

        "Day 4 - nearly framed by Alice":
            $ day2_dv_bet = 1
            $ day2_card_result = 3
            jump day4_boathouse


label esnav_day4_mine_alone:
    scene cg d4_catac

    menu:
        "< BACK":
            jump esnav_day4

        "Day 4 - go searching alone":
            $ day3_got_fail = 1
            $ mine_route = "fail"
            $ day4_uv_mine = 0
            jump day4_fail

        "Day 4 - inside the mine":
            $ day3_got_fail = 1
            $ mine_route = "fail"
            $ day4_uv_mine = 0
            jump mine

        "Day 4 - mine coalface":
            $ day3_got_fail = 1
            $ mine_route = "fail"
            $ point = "13"
            $ previous_point = "coalface"
            $ halt_visited = False
            $ coalface_visited = False
            $ back_to_start = False
            $ first_turn = False
            $ day4_uv_mine = 0
            jump fail_mine_coalface

        "Day 4 - mine dead end":
            $ day3_got_fail = 1
            $ mine_route = "fail"
            $ point = "3"
            $ previous_point = "halt"
            $ halt_visited = False
            $ coalface_visited = False
            $ back_to_start = False
            $ first_turn = False
            $ day4_uv_mine = 0
            jump fail_mine_halt

        "Day 4 - mine exit":
            $ day3_got_fail = 1
            $ mine_route = "fail"
            $ day4_uv_mine = 0
            jump fail_mine_exit

        "Day 4 - Miku route":
            $ prologue = 0
            $ d1_keys = True
            $ day2_cards_with_sl = 0
            $ day4_mi_accept = 1
            $ day4_uv_apple = False
            jump fail_mine_miku

        "Day 4 - UVAO route":
            $ prologue = 1
            $ d1_keys = False
            $ day3_got_fail = 1
            $ day4_uv_apple = True
            jump day4_uv
 

label esnav_day4_mine_sl:
    scene cg d4_catac_sl

    menu:
        "< BACK":
            jump esnav_day4

        "Day 4 - go searching with Slavya":
            $ day4_sl_compl = 1
            $ lp_sl = 6
            $ day4_uv_mine = 0
            jump day4_sl

        "Day 4 - mine coalface with Slavya":
            $ day4_sl_compl = 1
            $ lp_sl = 6
            $ mine_route = "sl"
            $ point = "13"
            $ previous_point = "coalface"
            $ halt_visited = False
            $ coalface_visited = False
            $ back_to_start = False
            $ first_turn = False
            $ day4_uv_mine = 0
            jump sl_mine_coalface

        "Day 4 - mine exit with Slavya":
            $ day4_sl_compl = 1
            $ lp_sl = 6
            $ mine_route = "sl"
            $ day4_uv_mine = 0
            jump sl_mine_exit


label esnav_day4_mine_dv:
    scene cg d4_catac_dv

    menu:
        "< BACK":
            jump esnav_day4

        "Day 4 - go searching with Alice":
            $ day4_dv_compl = 1
            $ lp_dv = 9
            $ day4_uv_mine = 0
            jump day4_dv

        "Day 4 - mine coalface with Alice":
            $ day4_dv_compl = 1
            $ lp_dv = 9
            $ mine_route = "dv"
            $ point = "13"
            $ previous_point = "coalface"
            $ halt_visited = False
            $ coalface_visited = False
            $ back_to_start = False
            $ first_turn = False
            $ day4_uv_mine = 0
            jump dv_mine_coalface

        "Day 4 - mine exit with Alice":
            $ day4_dv_compl = 1
            $ lp_dv = 9
            $ mine_route = "dv"
            $ day4_uv_mine = 0
            jump dv_mine_exit


label esnav_day4_mine_us:
    scene cg d4_catac_us

    menu:
        "< BACK":
            jump esnav_day4

        "Day 4 - go searching with Ulyana":
            $ day4_us_compl = 1
            $ lp_us = 6
            $ day4_uv_mine = 0
            jump day4_us

        "Day 4 - mine coalface with Ulyana":
            $ day4_us_compl = 1
            $ lp_us = 6
            $ mine_route = "us"
            $ point = "13"
            $ previous_point = "coalface"
            $ halt_visited = False
            $ coalface_visited = False
            $ back_to_start = False
            $ first_turn = False
            $ day4_uv_mine = 0
            jump us_mine_coalface

        "Day 4 - mine exit with Ulyana":
            $ day4_us_compl = 1
            $ lp_us = 6
            $ mine_route = "us"
            $ day4_uv_mine = 0
            jump us_mine_exit


label esnav_day4_mine_un:
    scene cg d4_catac_un

    menu:
        "< BACK":
            jump esnav_day4

        "Day 4 - go searching with Lena":
            $ day4_un_compl = 1
            $ lp_un = 6
            $ day4_uv_mine = 0
            jump day4_un

        "Day 4 - mine coalface with Lena":
            $ day4_un_compl = 1
            $ lp_un = 6
            $ mine_route = "un"
            $ point = "13"
            $ previous_point = "coalface"
            $ halt_visited = False
            $ coalface_visited = False
            $ back_to_start = False
            $ first_turn = False
            $ day4_uv_mine = 0
            jump un_mine_coalface

        "Day 4 - mine exit with Lena":
            $ day4_un_compl = 1
            $ lp_un = 6
            $ mine_route = "un"
            $ day4_uv_mine = 0
            jump un_mine_exit


label esnav_day4:
    scene bg ext_house_of_mt_day

    menu:
        "< BACK":
            jump es_navigator

        "Day 4 - morning":
            jump esnav_day4_morning

        "Day 4 - Shurick is missing":
            jump day4_main1

        "Day 4 - search the camp":
            jump esnav_day4_search_in_camp

        "Day 4 - dinner":
            jump day4_main2

        "Day 4 - go into the mine alone":
            jump esnav_day4_mine_alone

        "Day 4 - go into the mine with Slavya":
            jump esnav_day4_mine_sl

        "Day 4 - go into the mine with Alice":
            jump esnav_day4_mine_dv

        "Day 4 - go into the mine with Ulyana":
            jump esnav_day4_mine_us

        "Day 4 - go into the mine with Lena":
            jump esnav_day4_mine_un

        "Day 4 - Miku route":
            $ prologue = 0
            $ d1_keys = True
            $ day2_cards_with_sl = 0
            $ day4_mi_accept = 1
            $ day4_uv_apple = False
            jump fail_mine_miku

        "Day 4 - UVAO route":
            $ prologue = 1
            $ d1_keys = False
            $ day3_got_fail = 1
            $ day4_uv_apple = True
            jump day4_uv
