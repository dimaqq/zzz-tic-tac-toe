import pytest
import ttt.state


def test_validate():
    ttt.state.validate([[0]])

    with pytest.raises(AssertionError):
        ttt.state.validate([]), "board size must be > 0"

    with pytest.raises(AssertionError):
        ttt.state.validate([[None], [None], [None]]), "board must be square"
