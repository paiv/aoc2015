#!/usr/bin/env python3
import numpy as np
import re


instr_rx = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

def parse_instr(text):
    return [(s[0], *(int(x) for x in s[1:])) for s in instr_rx.findall(text)]


def solve(problem):
    board = parse_instr(problem)

    ingr = np.array([row[1:-1] for row in board], dtype=np.int)
    cals = np.array([row[-1] for row in board], dtype=np.int)
    n = ingr.shape[0]

    def weis2():
        for j in range(0,101):
            q = 100 - j
            yield (j,q)

    def weis4():
        for j in range(0,101):
            for k in range(0,101-j):
                for p in range(0,101-j-k):
                    q = 100 - j - k - p
                    yield (j,k,p,q)

    def tries():
        for xx in (weis2() if n == 2 else weis4()):
            w = np.array(xx, dtype=np.int)

            if cals.T.dot(w) == 500:
                a = ingr.T.dot(w)
                a = a.clip(min=0)
                score = np.product(a)
                yield score

    return max(tries())


def test():
    assert parse_instr('Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8') == [('Butterscotch', -1, -2, 6, 3, 8)]
    assert parse_instr('Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3') == [('Cinnamon', 2, 3, -2, -1, 3)]

    problem = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".strip()

    assert solve(problem) == 57600000


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
