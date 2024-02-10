#!/usr/bin/env python3

import brain_games.game_engine as run_module
import brain_games.games.even as game_module


def main():
    run_module.launch_game_logic(game_module)


if __name__ == '__main__':
    main()
