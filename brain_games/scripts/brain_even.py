#!/usr/bin/env python3

import brain_games.sample_gаmes as run_module
import brain_games.games.even as game_module


def main():
    run_module.launch_game_logic(game_module.rules_game, game_module.run_game)


if __name__ == '__main__':
    main()
