from . import game


if __name__ == "__main__":
    try:
        any(game.main())
    except EOFError:
        pass
