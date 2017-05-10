""" Draw game board/state in text mode """
HOR = "─"
VERT = "│"
CROSS = "┼"


def space(v, N=3):
    """ One "square" that can be marked """
    width = len(str(N ** 2)) + 2
    return str(v).center(width)


def line(l, start, N=3, clean=False):
    """ One line of "squares" or spaces """
    return VERT.join(space(("" if clean else i) if v is None else v, N=N) for i, v in enumerate(l, start))


def board(state, clean=False):
    """ Entire board with margins """
    N = len(state)
    width = len(str(N ** 2)) + 2
    bar = HOR * width
    sep = CROSS.join([bar] * N)
    data = f"\n{sep}\n".join(line(l, start, N=N, clean=clean) for start, l in zip(range(1, N ** 2 + 1, N), state))
    return f"\n{data}\n"
