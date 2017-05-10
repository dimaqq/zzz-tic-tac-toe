""" Game state is a list of lists representing NxN board.
    Initial state is all None.
    Running state will have a few slots populated by players (ids or objects)
"""
from collections import Counter


def validate(state):
    """ Current board state sanity check """
    assert state
    assert len(state) == len(state[0])
    c = sum(map(Counter, state), Counter())

    # possible records are None, player1, player2
    assert 1 <= len(c) <= 3

    players = [k for k in c.keys() if k is not None]
    assert len(players) <= 2

    if players:
        if len(players) > 1:
            p1, p2 = players
            assert abs(c[p1] - c[p2]) <= 1
        else:
            p1, = players
            assert c[p1] <= 1


def next_move(state, players="xo"):
    """ Given the board, who is to move next?
        returns a mark for next player, like 'x' or 'o'
        """
    c = sum(map(Counter, state), Counter())
    board_players = [k for k in c.keys() if k is not None]
    if not board_players:
        return players[0]
    if len(board_players) == 1:
        p1, = board_players
        assert p1 == players[0]

        return players[1]
    else:
        p1, p2 = board_players
        assert p1 in players
        assert p2 in players

        if c[p1] == c[p2]:
            return players[0]
        else:
            return sorted(board_players, key=lambda k: c[k])[0]


def index(move, N):
    m = move - 1
    assert 0 <= m < N ** 2, "Illegal move index"
    return m // N, m % N


def validate_move(state, move):
    """ Validate user requested move (string, input)
        Returns an int that can be used for `apply_move`
        Moves are base-1 indices into the board """
    N = len(state)
    assert move.isdigit(), "Move must be numeric (base 10)"
    move = int(move)
    assert 0 < move <= N ** 2, f"Move must be between 1 and {N ** 2} inclusive"
    x, y = index(move, N=N)
    assert state[x][y] is None, "This position is already marked"
    return move


def apply_move(state, move, mark):
    """ Modify baord state in place """
    x, y = index(move, len(state))
    assert state[x][y] is None
    state[x][y] = mark


def forward_diagonals(state):
    """ All the diagonals on the board, slanted right (like /)
        Includes those shorter than N
        e.g. . * .
             * . .
             . . .
    """
    N = len(state)
    sentinel = object()
    data = [[sentinel] * i + line + [sentinel] * (N - i - 1) for i, line in enumerate(state)]
    for column in zip(*data):
        yield [c for c in column if c is not sentinel]


def back_diagonals(state):
    """ All the diagonals on the board, slanted left (like \)
        Include those shorter than N
        e.g. . . .
             * , .
             . * .
    """
    N = len(state)
    sentinel = object()
    data = [[sentinel] * (N - i - 1) + line + [sentinel] * i for i, line in enumerate(state)]
    for column in zip(*data):
        yield [c for c in column if c is not sentinel]


def columns(state):
    """ All the columns on the board """
    return zip(*state)


def game_over(state):
    """ detect any 3 in a row, colum or either diagonal
        also detect when board is full but none won
    """
    for mark in "xo":
        figure = mark * 3
        for gen in iter, columns, forward_diagonals, back_diagonals:
            for line in gen(state):
                line = "".join(" " if c is None else str(c) for c in line)
                if figure in line:
                    return mark

    if any(None in line for line in state):
        return False

    return "draw"
