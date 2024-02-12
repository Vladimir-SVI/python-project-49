#!/usr/bin/env python3

import brain_games.games.calc as game_module
from brain_games.game_engine import launch_game_logic


def main():
    launch_game_logic(game_module)


if __name__ == '__main__':
    main()
