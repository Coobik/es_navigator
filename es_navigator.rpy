init:
    $ mods["es_navigator"] = u"ES Navigator"

    # fuck card games
    $ persistent.CardsWon3 = True

    # uncomment to enable hentai:
    $ persistent.hentai = True


label es_navigator:
    scene bg int_bus

    menu:
        "Opening":
            jump opening

        "Day 1":
            jump day1

        "Day 2":
            jump esnav_day2

        "Day 3":
            jump esnav_day3

        "Day 4":
            jump esnav_day4

        "Day 5":
            jump esnav_day5

        "Day 6":
            jump esnav_day6

        "Day 7":
            jump esnav_day7

        "Epilogue":
            jump esnav_epilogue

        "Endings":
            jump esnav_endings

        "Zhenya route":
            jump zhenya_route
