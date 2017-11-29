#!/usr/bin/env python3


def solve(problem):
    visited = set()
    pos = [[0, 0], [0, 0]]
    turn = 0

    visited.add((0, 0))

    for c in problem:
        x = 0
        y = 0

        if c == '>':
            x = 1
        elif c == '^':
            y = -1
        elif c == '<':
            x = -1
        elif c == 'v':
            y = 1

        p = pos[turn]
        p[0] += x
        p[1] += y
        turn = (turn + 1) % 2

        visited.add(tuple(p))

    return len(visited)


def test():
    assert solve('^v') == 3
    assert solve('^>v<') == 3
    assert solve('^v^v^v^v^v') == 11


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
