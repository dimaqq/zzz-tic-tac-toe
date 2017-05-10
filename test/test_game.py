import pytest
from unittest.mock import Mock, patch

import ttt.game


def test_prevalidate():
    assert ttt.game.prevalidate("3") == "3"

    with pytest.raises(SystemExit):
        ttt.game.prevalidate("quit")


def test_validate_board_size():
    assert ttt.game.validate_board_size("") == 3
    assert ttt.game.validate_board_size("3") == 3
    assert ttt.game.validate_board_size("4") == 4

    with pytest.raises(AssertionError):
        ttt.game.validate_board_size("foobar")

    with pytest.raises(AssertionError):
        ttt.game.validate_board_size("2")

    with pytest.raises(AssertionError):
        ttt.game.validate_board_size("999")


@patch("ttt.game.game")
def test_main(game):
    m = ttt.game.main()
    next(m)
    assert game.call_count == 1
    next(m)
    assert game.call_count == 2


@patch("ttt.game.game_loop", return_value=range(1))
@patch("ttt.game.print", create=True)
@patch("ttt.game.prompt", return_value="3")
@patch("ttt.state.game_over", return_value="x")
def test_game(game_over, prompt, print, game_loop):
    g = ttt.game.game()

    next(g)
    assert "new game" in str(print.call_args_list)
    assert "name for player 1" in str(print.call_args_list)
    assert "name for player 2" in str(print.call_args_list)
    assert "Congratulations" not in str(print.call_args_list)

    next(g)
    assert "Congratulations 3" in str(print.call_args_list)


@patch("ttt.game.game_loop", return_value=range(1))
@patch("ttt.game.print", create=True)
@patch("ttt.game.prompt", return_value="3")
@patch("ttt.state.game_over", return_value="draw")
def test_game_draw(game_over, prompt, print, game_loop):
    g = ttt.game.game()

    next(g)
    next(g)
    assert "it's a draw" in str(print.call_args_list)


@patch("ttt.game.game_loop", return_value=range(1))
@patch("ttt.game.print", create=True)
@patch("ttt.game.prompt", return_value="2")
@patch("ttt.state.game_over", return_value="x")
def test_game_validates_board_size(game_over, prompt, print, game_loop):
    g = ttt.game.game()

    next(g)
    assert "name for player" not in str(print.call_args_list), "valid board size needed first"

    prompt.return_value = ""
    next(g)
    assert "name for player" in str(print.call_args_list), "default board size ough to be used"
