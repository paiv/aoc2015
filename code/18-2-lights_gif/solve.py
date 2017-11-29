#!/usr/bin/env python3
import numpy as np
from scipy import signal


def parse_board(text):
     return np.array([[1 if c == '#' else 0 for c in row] for row in text.splitlines()])


def format_board(board):
    return '\n'.join(''.join('#' if x else '.' for x in row) for row in board)


def evolve(world, eons):
    kernl = np.array([[1,1,1], [1,100,1], [1,1,1]])
    w = world.shape[0] - 1
    world[(0, 0, w, w),(0, w, w, 0)] = 1

    for i in range(eons):
        z = signal.convolve2d(world, kernl, mode='same')
        world[...] = 0
        world[(z == 102) | (z == 103) | (z == 3)] = 1
        world[(0, 0, w, w),(0, w, w, 0)] = 1

    return world


def play(text, steps):
    world = parse_board(text)
    evolve(world, steps)
    return format_board(world)


def animate(text, steps=100):
    import time
    world = parse_board(text)

    print('\n' * 30)
    print(format_board(world))

    for i in range(steps):
        time.sleep(1/4)
        evolve(world, 1)
        print()
        print(format_board(world))


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

    assert solve(problem, 5) == 17


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    # animate(getinput())
    print(solve(getinput()))
