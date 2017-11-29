#!/usr/bin/env python3
import re


instr_rx = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')

def parse_instr(text):
    return [(n, *(int(x) for x in (a,b,c))) for n,a,b,c in instr_rx.findall(text)]


def travel(deer, t):
    name,speed,active,snooze = deer
    w = active + snooze
    total = speed * (t // w) * active
    r = min(active, t % w)
    total += r * speed
    return total


def solve(problem, t=2503):
    board = parse_instr(problem)
    return max(travel(x, t) for x in board)


def test():
    assert parse_instr('Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.') == [('Vixen', 19, 7, 124)]

    assert travel(('A', 10, 10, 40), 0) == 0
    assert travel(('A', 10, 10, 40), 1) == 10
    assert travel(('A', 10, 10, 40), 10) == 100
    assert travel(('A', 10, 10, 40), 50) == 100
    assert travel(('A', 10, 10, 40), 51) == 110

    problem = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip()

    assert solve(problem, 1000) == 1120


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
