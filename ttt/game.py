from prompt_toolkit import prompt
from . import draw, state

MAX_SIZE = 33  # arbitrary, as long as it fits on the screen


def main():
    while True:
        game()
        print()


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


def game():
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

    board = [[None for i in range(N)] for j in range(N)]
    print("Enter name for player 1")
    p1 = prompt(">> ")
    print("Enter name for player 2")
    p2 = prompt(">> ")
    names = dict(x=p1, o=p2)

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
        state.apply_move(board, move, mark)

    print(draw.board(board))
    mark = state.game_over(board)
    if mark == "draw":
        print(f"Congratulations {p1} and {p2}, it's a draw!")
    else:
        print(f"Congratulations {names[mark]}, you won!")
