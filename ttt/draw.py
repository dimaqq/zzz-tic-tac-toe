
hor = "─"
vert = "│"
cross = "┼"


def line(l, start):
    # FIXME: board larger thant 3x3 requires larger indices
    return f" {vert} ".join(str(i if v is None else v) for i, v in enumerate(l, start))


def draw(state):
    N = len(state)
    return f"\n{hor * len(state) * 3}\n".join(line(l, start) for start, l in zip(range(1, N * N + 1, N), state))


if __name__ == "__main__":
    print(draw([[1,2,3], [3,4,5], [None, None, None]]))
