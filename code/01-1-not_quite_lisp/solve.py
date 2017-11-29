#!/usr/bin/env python3


def solve(problem):
    return sum(1 if c == '(' else -1 if c == ')' else 0 for c in problem)


def test():
    assert solve('(())') == 0
    assert solve('()()') == 0
    assert solve('(((') == 3
    assert solve('(()(()(') == 3
    assert solve('))(((((') == 3
    assert solve('())') == -1
    assert solve('))(') == -1
    assert solve(')))') == -3
    assert solve(')())())') == -3


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
