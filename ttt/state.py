""" Game state is a list of lists representing NxN board.
    Initial state is all None.
    Running state will have a few slots populated by players (ids or objects)
"""
from collections import Counter


def validate(state):
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


def game_over(state):
    ...
