#!/usr/bin/env python3

import brain_games.cli


def hello():
    print("Welcome to the Brain Games!")


def main():
    hello()
    name = brain_games.cli.welcome_user()
    return name


if __name__ == '__main__':
    main()
