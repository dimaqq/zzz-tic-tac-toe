""" Game state is a list of lists representing NxN board.
    Initial state is all None.
    Running state will have a few slots populated by players (ids or objects)
"""


def validate(state):
    assert state
    assert len(state) == len(state[0])
