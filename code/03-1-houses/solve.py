#!/usr/bin/env python3


def solve(problem):
    visited = set()
    x = 0
    y = 0
    visited.add((x, y))

    for c in problem:
        if c == '>':
            x += 1
        elif c == '^':
            y -= 1
        elif c == '<':
            x -= 1
        elif c == 'v':
            y += 1
        visited.add((x, y))

    return len(visited)


def test():
    assert solve('>') == 2
    assert solve('^>v<') == 4
    assert solve('^v^v^v^v^v') == 2


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
