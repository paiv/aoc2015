#!/usr/bin/env python3
import numpy as np
from scipy import signal


def parse_board(text):
     return np.array([[1 if c == '#' else 0 for c in row] for row in text.splitlines()])


def format_board(board):
    return '\n'.join(''.join('#' if x else '.' for x in row) for row in board)


def evolve(world, eons):
    kernl = np.array([[1,1,1], [1,100,1], [1,1,1]])

    for i in range(eons):
        z = signal.convolve2d(world, kernl, mode='same')
        world[...] = 0
        world[(z == 102) | (z == 103) | (z == 3)] = 1

    return world


def play(text, steps):
    world = parse_board(text)
    evolve(world, steps)
    return format_board(world)


def solve(problem, steps=100):
    world = parse_board(problem)
    evolve(world, steps)
    return np.sum(world)


def test():

    problem = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
""".strip()

    expected1 = """
..##..
..##.#
...##.
......
#.....
#.##..
""".strip()

    expected2 = """
..###.
......
..###.
......
.#....
.#....
""".strip()

    expected3 = """
...#..
......
...#..
..##..
......
......
""".strip()

    expected4 = """
......
......
..##..
..##..
......
......
""".strip()

    assert play(problem, 1) == expected1
    assert play(problem, 2) == expected2
    assert play(problem, 3) == expected3
    assert play(problem, 4) == expected4

    assert solve(problem, 1) == 11
    assert solve(problem, 2) == 8
    assert solve(problem, 3) == 4
    assert solve(problem, 4) == 4


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
