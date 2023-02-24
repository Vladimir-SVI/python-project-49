#!/usr/bin/env python3

import brain_games.scripts.brain_games
import brain_games.games.sample_gemes as run_module
import brain_games.games.game_gcd as game_module


def main():
    player_name = brain_games.scripts.brain_games.main()
    run_module.launch_game_logic(player_name, game_module.rules_game, game_module.run_game)


if __name__ == '__main__':
    main()
