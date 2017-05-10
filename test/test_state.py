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


def test_columns():
    data = list(ttt.state.columns([[1, 2], [3, 4]]))
    assert (1, 3) in data
    assert (2, 4) in data


def test_forward():
    data = list(ttt.state.forward_diagonals([[1, 2], [3, 4]]))
    assert [1] in data
    assert [2, 3] in data
    assert [4] in data


def test_back():
    data = list(ttt.state.back_diagonals([[1, 2], [3, 4]]))
    assert [2] in data
    assert [1, 4] in data
    assert [3] in data


def test_game_over():
    # no winner
    assert not ttt.state.game_over([[None, "x"], [None, None]])
    assert ttt.state.game_over([list("ox"), list("ox")]) == "draw"

    # 3 out of 3
    assert ttt.state.game_over([list("xxx"), [None] * 3, [None] * 3]) == "x"
    assert ttt.state.game_over([list("ooo"), [None] * 3, [None] * 3]) == "o"
    assert ttt.state.game_over([list("xo-"), list("x--"), list("x--")]) == "x"
    assert ttt.state.game_over([list("xo-"), list("-x-"), list("--x")]) == "x"
    assert ttt.state.game_over([list("o-x"), list("ox-"), list("x--")]) == "x"

    # 3 out of N
    assert ttt.state.game_over([list("xxx-"), list("----"), list("----"), list("----")]) == "x"
    assert ttt.state.game_over([list("x---"), list("-x--"), list("--x-"), list("----")]) == "x"
    assert ttt.state.game_over([list("-x--"), list("--x-"), list("---x"), list("----")]) == "x"
