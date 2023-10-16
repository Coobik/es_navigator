label esnav_epilogue:
    scene bg semen_room

    menu:
        "< BACK":
            jump es_navigator

        "Wake up at home, chat with a stranger":
            jump epilogue_main

        "Wake up back in the camp with Lena, then live a life with her":
            jump epilogue_un_good

        "Wake up at home, then open up":
            jump epilogue_un_bad

        "Wake up at home, then meet Ulyana at university":
            $ persistent.replay = "us_good"
            $ epilogue_us_good = 1
            jump epilogue_us

        "Wake up at home, then do not meet Ulyana at university":
            $ persistent.replay = "us_bad"
            $ epilogue_us_bad = 1
            jump epilogue_us

        "Wake up at home, then meet Alice at the concert":
            $ persistent.replay = "dv_good"
            $ epilogue_dv_good = 1
            jump epilogue_dv

        "Wake up at home, then do not meet Alice at the concert":
            $ persistent.replay = "dv_bad"
            $ epilogue_dv_bad = 1
            jump epilogue_dv

        "Wake up at home, then meet Slavya at the bus stop":
            $ persistent.replay = "sl_good"
            $ epilogue_sl_good = 1
            jump epilogue_sl

        "Wake up at home, then do not meet Slavya at the bus stop":
            $ persistent.replay = "sl_bad"
            $ epilogue_sl_bad = 1
            jump epilogue_sl

        "Wake up on the movie set with Miku, then Pioneer Camp Horror":
            jump epilogue_mi

        "Wake up in the camp, then meet UVAO":
            jump esnav_epilogue_uv
