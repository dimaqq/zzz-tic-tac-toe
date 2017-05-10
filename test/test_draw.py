import ttt.draw


BOARD = """
 x │ o │ x 
───┼───┼───
 o │ x │ o 
───┼───┼───
 7 │ 8 │ 9 
"""  # NOQA (trailing whitespace important)


def test_space():
    assert ttt.draw.space("x") == " x "
    assert ttt.draw.space(7) == " 7 "
    assert ttt.draw.space("x", 13) == "  x  "
    assert ttt.draw.space(169, 13) == " 169 "


def test_line():
    assert ttt.draw.line([None, "x"], 8) == " 8 │ x "
    assert ttt.draw.line(list("xox"), 8, N=13) == "  x  │  o  │  x  "


def test_board():
    assert ttt.draw.board([list("xox"), list("oxo"), [None] * 3]) == BOARD
