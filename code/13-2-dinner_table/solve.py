#!/usr/bin/env python3
import itertools
import numpy as np
import re


instr_rx = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).')

def parse_instr(text):
    return [(a, b, int(v) if x == 'gain' else -int(v)) for a,x,v,b in instr_rx.findall(text)]


def parse_board(text):
    prog = parse_instr(text)

    names = list(set([x for a,b,v in prog for x in (a,b)])) + ["myself"]
    w = len(names)
    board = np.zeros((w,w), dtype=np.int)

    for a,b,v in prog:
        x = names.index(a)
        y = names.index(b)
        board[x, y] = v

    return (board, names)


def eval_score(trial, board):
    total = 0
    n = len(trial)
    for i in range(0, n):
        a = trial[i]
        b = trial[(i + 1) % n]
        total += board[a, b] + board[b, a]
    return total


def solve(problem):
    board, names = parse_board(problem)
    idx = list(range(0, len(names)))

    best_score = None

    for trial in itertools.permutations(idx):
        score = eval_score(trial, board)

        if best_score is None or best_score < score:
            best_score = score

    # print(board)
    return best_score


def test():
    assert parse_instr('Alice would gain 54 happiness units by sitting next to Bob.') == [('Alice', 'Bob', 54)]
    assert parse_instr('Bob would gain 83 happiness units by sitting next to Alice.') == [('Bob', 'Alice', 83)]
    assert parse_instr('Bob would lose 7 happiness units by sitting next to Carol.') == [('Bob', 'Carol', -7)]


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
