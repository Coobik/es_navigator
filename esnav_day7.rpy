label esnav_day7:
    scene bg ext_house_of_mt_day

    menu:
        "< BACK":
            jump es_navigator

        "Day 7 - wake up alone, meet Pioneer":
            $ day3_got_fail = 1
            jump day7_main

        "Day 7 - wake up, meet Lena, then live a life with her":
            $ lp_un = 10
            jump day7_un

        "Day 7 - wake up again with Lena, then live a life with her":
            jump day7_un_good

        "Day 7 - wake up, meet Lena, then open up":
            $ lp_un = 8
            jump day7_un

        "Day 7 - wake up again with Lena, then open up":
            jump day7_un_bad        

        "Day 7 - wake up with Ulyana at the cyber club":
            $ lp_us = 8
            jump day7_us

        "Day 7 - board the bus with Ulyana":
            $ epilogue_us_good = 1
            jump day7_us_good

        "Day 7 - board the bus without Ulyana":
            $ epilogue_us_bad = 1
            jump day7_us_bad

        "Day 7 - hangover with Alice, then get along with her":
            $ lp_dv = 10
            jump day7_dv

        "Day 7 - get along with Alice":
            $ epilogue_dv_good = 1
            jump day7_dv_good

        "Day 7 - hangover with Alice, then break up with her":
            $ lp_dv = 8
            jump day7_dv

        "Day 7 - break up with Alice":
            $ epilogue_dv_bad = 1
            jump day7_dv_bad

        "Day 7 - wake up with Slavya, then get along with her":
            $ lp_sl = 10
            jump day7_sl

        "Day 7 - get along with Slavya":
            $ epilogue_sl_good = 1
            jump day7_sl_good

        "Day 7 - wake up with Slavya, then break up with her":
            $ lp_sl = 8
            jump day7_sl

        "Day 7 - break up with Slavya":
            $ epilogue_sl_bad = 1
            jump day7_sl_bad
