try:
    from snake_game.game import Game
except ModuleNotFoundError:
    from game import Game


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
