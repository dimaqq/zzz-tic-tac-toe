import ttt.draw


BOARD = """
x │ o │ x
─────────
o │ x │ o
─────────
7 │ 8 │ 9
""".strip()


def test_draw():
    assert ttt.draw.draw([list("xox"), list("oxo"), [None]*3]) == BOARD
