import pytest
import ttt.state


def test_validate():
    ttt.state.validate([[None]])
    ttt.state.validate([[0]])
    ttt.state.validate([list("xox"), [None] * 3, [None] * 3])

    with pytest.raises(AssertionError):
        ttt.state.validate([]), "board size must be > 0"

    with pytest.raises(AssertionError):
        ttt.state.validate([[None], [None], [None]]), "board must be square"

    with pytest.raises(AssertionError):
        ttt.state.validate([[1, 2, 1], [None, None, None], [1, 2, 3]]), "can't have 3 players"


def test_next_move():
    assert ttt.state.next_move([[None]]) == "x"

    assert ttt.state.next_move([["x", None], [None, None]]) == "o"
    assert ttt.state.next_move([["x", "o"], [None, None]]) == "x"
    assert ttt.state.next_move([["x", "o"], ["x", None]]) == "o"
