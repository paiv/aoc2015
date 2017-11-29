#!/usr/bin/env python3
import re


chr_rx = re.compile(r'["\\]')

def check_line(text):
    chars = chr_rx.findall(text)
    n = 2 + len(chars)
    return n


def solve(problem):
    return sum(check_line(s) for s in problem.splitlines())


def test():
    assert solve(r'""') == 4
    assert solve(r'"abc"') == 4
    assert solve(r'"aaa\"aaa"') == 6
    assert solve(r'"\x27"') == 5
    assert solve(r'"\xff"') == 5

    problem = r"""
""
"abc"
"aaa\"aaa"
"\x27"
""".strip()

    assert solve(problem) == 19


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
