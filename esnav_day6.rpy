label esnav_day6:
    scene bg ext_houses_day

    menu:
        "< BACK":
            jump es_navigator

        "Day 6 - wake up alone, then meet Pioneer":
            jump day6_main

        "Day 6 - wake up, Lena is missing (Lena route)":
            $ lp_un = 8
            jump day6_un

        "Day 6 - meet Electronic at the cyber club (Lena route)":
            $ lp_un = 8
            jump day6_after_map

        "Day 6 - wake up (Ulyana route)":
            $ lp_us = 7
            jump day6_us

        "Day 6 - wake up, Slavya is in the first aid post (Slavya route)":
            $ lp_sl = 8
            jump day6_sl

        "Day 6 - wake up (Alice route)":
            $ lp_dv = 10
            jump day6_dv
