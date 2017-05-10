from prompt_toolkit import prompt
from . import draw, state

MAX_SIZE = 33  # arbitrary, as long as it fits on the screen


def main():
    """ Main loop of tic-tac-toe, starts a new game when current is over.
        It's a generator to aid testing, use it as `any(main())`
    """
    while True:
        any(game())
        print()
        yield


def prevalidate(s):
    if s.strip() == "quit":
        raise SystemExit("Thanks for playing!")
    return s


def validate_board_size(inp, default=3):
    if not inp:
        return default

    assert inp.isdigit(), "Board size must be numberic (base 10)"
    rv = int(inp)
    assert rv >= 3, "Board size must be at least 3"
    assert rv <= MAX_SIZE, f"Board size must be at most {MAX_SIZE}"
    return rv


def game_loop(board, names):
    """ Moves in a tic-tac-toe game.
        It's a generator to aid testing, use it as `any(game_loop(...))`
    """
    while not state.game_over(board):
        print(draw.board(board))
        mark = state.next_move(board)
        while True:
            try:
                print(f"{names[mark]}, choose a box to place an {mark!r} into")
                move = state.validate_move(
                    board,
                    prevalidate(
                        prompt(">> ")))
                break
            except AssertionError as e:
                print(e)
                yield
        state.apply_move(board, move, mark)
        yield


def game():
    """ One game of tic-tac-toe.
        It's a generator to aid testing, use it as `any(game())`
    """
    print("Welcome to a new game, enjoy!")
    print("P.S. you can always quit by typing 'quit'")
    while True:
        try:
            print("How large of a game? (default=3)")
            N = validate_board_size(
                prevalidate(
                    prompt(">> ")))
            break
        except AssertionError as e:
            print(e)
            yield

    board = [[None for i in range(N)] for j in range(N)]

    print("Enter name for player 1")
    p1 = prevalidate(
        prompt(">> "))

    print("Enter name for player 2")
    p2 = prevalidate(
        prompt(">> "))
    names = dict(x=p1, o=p2)

    any(game_loop(board, names))

    print(draw.board(board, clean=True))
    mark = state.game_over(board)
    if mark == "draw":
        print(f"Congratulations {p1} and {p2}, it's a draw!")
    else:
        print(f"Congratulations {names[mark]}, you won!")
    yield
