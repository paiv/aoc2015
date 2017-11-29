#!/usr/bin/env python3
import re


str_rx = re.compile(r'^"(.*)"$')
chr_rx = re.compile(r'\\\\|\\"|\\x[a-f\d]{2}|[^"]')

def check_line(text):
    m = str_rx.match(text)
    escaped = m.group(1)
    chars = chr_rx.findall(escaped)
    n = 2 + len(escaped) - len(chars)
    return n


def solve(problem):
    return sum(check_line(s) for s in problem.splitlines())


def test():
    assert solve(r'""') == 2
    assert solve(r'"abc"') == 2
    assert solve(r'"aaa\"aaa"') == 3
    assert solve(r'"\x27"') == 5
    assert solve(r'"\xff"') == 5

    problem = r"""
""
"abc"
"aaa\"aaa"
"\x27"
""".strip()

    assert solve(problem) == 12


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
