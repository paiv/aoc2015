#!/usr/bin/env python3


def solve(problem):
    floor = 0
    for i in range(0, len(problem)):
        c = problem[i]
        x = 1 if c == '(' else -1 if c == ')' else 0
        floor += x
        if floor == -1:
            return i + 1


def test():
    assert solve(')') == 1
    assert solve('()())') == 5


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
