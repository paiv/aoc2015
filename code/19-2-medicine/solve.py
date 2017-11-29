#!/usr/bin/env python3
import heapq
import itertools


class PriorityQueue:
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.counter = itertools.count()     # unique sequence count

    def __len__(self):
        return len(self.pq)

    def append(self, task, priority=0):
        count = next(self.counter)
        entry = (priority, count, task)
        heapq.heappush(self.pq, entry)

    def pop(self):
        if self.pq:
            priority, count, task = heapq.heappop(self.pq)
            return task
        raise KeyError('pop from an empty priority queue')


def parse_board(text):
    lines = text.splitlines()
    mol = lines[-1]
    rep = [line.split(' => ') for line in lines[:-1] if len(line.strip()) > 0]
    return (rep, mol)


def solve(problem):
    rep, mol = parse_board(problem)
    rep = sorted(rep, key=lambda x: -len(x[1]))

    fringe = PriorityQueue()
    fringe.append((0, mol), len(mol))

    while len(fringe) > 0:
        steps, mol = fringe.pop()

        if mol == 'e':
            return steps

        # if steps % 10 == 0:
        #     print(mol)

        for x,y in rep:
            for i in range(len(mol)):
                h, t = mol[:i], mol[i:]
                if t.startswith(y):
                    s = h + t.replace(y, x, 1)
                    fringe.append((steps + 1, s), len(s))


def test():

    problem = """
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
""".strip()

    assert solve(problem) == 6


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
