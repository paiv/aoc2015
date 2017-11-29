#!/usr/bin/env python3


def solve(problem, n=150):

    boxes = [int(x) for x in problem.split()]

    def loop(k, wei, q):
        if wei < 0:
            pass
        elif wei == 0:
            yield q
        else:
            for i in range(k + 1, len(boxes)):
                yield from loop(i, wei - boxes[i], q + 1)

    ps = list(loop(-1, n, 0))
    return ps.count(min(ps))


def test():

    problem = """
20
15
10
5
5
""".strip()

    assert solve(problem, 25) == 3


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
