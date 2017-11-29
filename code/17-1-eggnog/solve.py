#!/usr/bin/env python3


def solve(problem, n=150):

    boxes = [int(x) for x in problem.split()]

    def loop(k, wei):
        if wei < 0:
            yield 0
        elif wei == 0:
            yield 1
        else:
            for i in range(k + 1, len(boxes)):
                yield from loop(i, wei - boxes[i])

    return sum(loop(-1, n))


def test():

    problem = """
20
15
10
5
5
""".strip()

    assert solve(problem, 25) == 4


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
