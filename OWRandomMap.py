import random
import msvcrt

DONT_PLAY_MODES_TWICE = True


# wait for character input
def wait():
    msvcrt.getch()


# get a random map
def get_random_map(exclude = None):
    # Modes to be selected from
    modes = ["Assault", "Escort", "Hybrid", "Control"]

    # Maps to the modes
    maps = {
        "Assault": [
            "Hanamura",
            "Horizon Lunar Colony",
            "Paris",
            "Temple of Anubis",
            "Volskaya Industries"
        ],
        "Escort": [
            "Dorado",
            "Junkertown",
            "Rialto",
            "Route 66",
            "Watchpoint: Gibraltar"
        ],
        "Hybrid": [
            "Blizzard World",
            "Eichenwalde",
            "Hollywood",
            "King's Row",
            "Numbani"
        ],
        "Control": [
            "Busan",
            "Ilios",
            "Lijiang Tower",
            "Nepal",
            "Oasis"
        ]
    }

    # remove exclusion if needed
    if exclude is not None:
        modes = modes.remove(exclude)

    # select a gamemode and map
    gamemode = random.choice(modes)
    mappool = maps[gamemode]
    selectedmap = random.choice(mappool)

    return selectedmap, gamemode


# Main loop
def mainloop():

    gamemode = None

    while True:

        if not DONT_PLAY_MODES_TWICE:
            gamemode = None

        # get a random map
        selectedmap, gamemode = get_random_map(gamemode)

        print("Your next Map is " + selectedmap)

        # wait for character
        wait()


# Start mainloop
mainloop()
