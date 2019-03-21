import random
import msvcrt

DONT_PLAY_MODES_TWICE = True
DONT_PLAY_MAPS_TWICE = True

# Maps and gamemodes
MAPS = {
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


# wait for character input
def wait():
    msvcrt.getch()


# get a random map
def get_random_map(excludemode=None, excludemaps=None):
    # Modes to be selected from
    modes = ["Assault", "Escort", "Hybrid", "Control"]
    maps = MAPS

    # remove exclusion if needed
    if excludemode in modes:
        modes.remove(excludemode)

    # remove already played maps
    if excludemaps is not None:
        for key, values in maps.items():
            for m in excludemaps:
                if m in values:
                    values.remove(m)

    # select a gamemode and map
    gamemode = random.choice(modes)
    mappool = maps[gamemode]
    selectedmap = random.choice(mappool)

    return selectedmap, gamemode


# Main loop
def mainloop():

    gamemode = None
    playedmaps = []

    while True:

        # check if modes can be played twice in a row
        if not DONT_PLAY_MODES_TWICE:
            gamemode = None

        # check if maps can be played twice
        if not DONT_PLAY_MAPS_TWICE:
            playedmaps = None

        # get a random map
        selectedmap, gamemode = get_random_map(gamemode, playedmaps)

        # add map to playedmaps
        playedmaps.append(selectedmap)

        print(playedmaps)

        # print current map
        print("Your next Map is " + selectedmap)

        # wait for character
        wait()


# Start mainloop
mainloop()
