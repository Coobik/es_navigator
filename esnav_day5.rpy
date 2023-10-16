label esnav_day5:
    scene bg ext_houses_day

    menu:
        "< BACK":
            jump es_navigator

        "Day 5 - wake up after the nightmare, then witness Alice and Ulyana bathing":
            jump day5_main1

        "Day 5 - meet Miku at the canteen":
            jump day5_dining_hall

        "Day 5 - visit first aid post":
            jump day5_aidpost

        "Day 5 - meet Ulyana at the cyber club":
            jump day5_clubs

        "Day 5 - lunch, then go strawberry picking":
            jump day5_main2

        "Day 5 - yeast, flour, and sugar":
            jump esnav_day5_yeast_flour_sugar

        "Day 5 - UVAO asks for some sugar, later go hiking into the forest":
            jump day5_main3

        "Day 5 - choose your route":
            jump esnav_day5_choose_route


label esnav_day5_yeast_flour_sugar:
    scene bg ext_square_day

    menu:
        "< BACK":
            jump esnav_day5

        "Day 5 - collect yeast, flour, and sugar":
            jump day5_map

        "Day 5 - get beer at the first aid post":
            jump day5_aidpost_2

        "Day 5 - get sugar at the cyber club":
            jump day5_clubs_2

        "Day 5 - get flour at the library, also meet Alice with the book":
            jump day5_library_2


label esnav_day5_choose_route:
    scene bg ext_polyana_sunset

    menu:
        "< BACK":
            jump esnav_day5

        "Day 5 - Alice and Lena arguing (Alice route)":
            $ lp_dv = 10
            jump day5_dv

        "Day 5 - find Slavya on the beach (Slavya route)":
            $ lp_sl = 8
            jump day5_sl

        "Day 5 - find Ulyana on the square (Ulyana route)":
            $ lp_us = 7
            jump day5_us

        "Day 5 - Lena and Alice arguing (Lena route)":
            $ lp_un = 9
            jump day5_un
