#!/usr/bin/env python3
import numpy as np
import re


instr_rx = re.compile(r'turn (on) ([\d,]+ through [\d,]+)|turn (off) ([\d,]+ through [\d,]+)|(toggle) ([\d,]+ through [\d,]+)')
rect_rx = re.compile(r'(\d+),(\d+) through (\d+),(\d+)')


def parse_rect(text):
    m = rect_rx.match(text)
    return ((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4))))


def parse_instr(text):
    res = []

    for m in instr_rx.finditer(text):
        if m.group(1):
            res.append((m.group(1), *parse_rect(m.group(2))))
        elif m.group(3):
            res.append((m.group(3), *parse_rect(m.group(4))))
        elif m.group(5):
            res.append((m.group(5), *parse_rect(m.group(6))))

    return res


def format_state(state):
    return '\n'.join(''.join('*' if x else ' ' for x in row) for row in state)


def solve(problem):
    state = np.zeros((1000,1000), dtype=np.int)

    for instr, p, q in parse_instr(problem):
        idx = slice(p[0], q[0]+1), slice(p[1], q[1]+1)

        if instr == 'on':
            state[idx] += 1
        elif instr == 'off':
            state[idx] -= 1
            b = state < 0
            state[b] = 0
        elif instr == 'toggle':
            state[idx] += 2

        # print(state.astype(np.int))

    res = np.sum(state)
    return res


def test():
    assert parse_rect('0,0 through 999,999') == ((0, 0), (999, 999))

    assert parse_instr('turn on 0,0 through 999,999') == [('on', (0,0), (999,999))]
    assert parse_instr('toggle 0,0 through 999,0') == [('toggle', (0,0), (999,0))]
    assert parse_instr('turn off 499,499 through 500,500') == [('off', (499,499), (500,500))]

    problem = """
turn on 0,0 through 0,0
toggle 0,0 through 999,999
""".strip()

    assert solve(problem) == 2000000 + 1


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
