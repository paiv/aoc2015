#!/usr/bin/env python3
import re


instr_rx = re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

def parse_instr(text):
    res = []
    for m in instr_rx.finditer(text):
        res.append((int(m.group(1)), { m.group(2): int(m.group(3)), m.group(4): int(m.group(5)), m.group(6): int(m.group(7)) }))
    return res


def solve(problem):
    board = parse_instr(problem)

    lookup = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    for aunt in board:
        f = True
        for k,v in aunt[1].items():
            if lookup[k] != v:
                f = False
        if f:
            return aunt[0]


def test():
    assert parse_instr('Sue 1: goldfish: 6, trees: 9, akitas: 0') == [(1, {'goldfish': 6, 'trees': 9, 'akitas': 0})]


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
