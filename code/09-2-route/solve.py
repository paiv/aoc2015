#!/usr/bin/env python3
import numpy as np
import re


route_rx = re.compile(r'(\w+) to (\w+) = (\d+)')

def parse_graph(text):
    names = list(set([x for route in route_rx.findall(text) for x in route[:2]]))
    w = len(names)

    roads = np.zeros((w,w), dtype=np.int)

    for m in route_rx.finditer(text):
        a = names.index(m.group(1))
        b = names.index(m.group(2))
        x = int(m.group(3))
        roads[a,b] = x
        roads[b,a] = x

    return (roads, names)


def valid_moves(roads, todo, path, cost):
    if len(path) == 0:
        for city in todo:
            child_cities = set(todo) - set([city])
            yield ([city], 0, list(child_cities))
    else:
        pos = path[-1]
        for city in todo:
            x = roads[pos, city]
            if x > 0:
                child_cities = set(todo) - set([city])
                yield (path + [city], cost + x, list(child_cities))


def solve(problem):
    roads, names = parse_graph(problem)

    fringe = list()
    best_cost = None
    best_path = None

    todo = [names.index(x) for x in names]
    fringe.append(([], 0, todo))

    while len(fringe) > 0:
        path, cost, todo = fringe.pop(0)

        if len(todo) == 0:
            if best_cost is None or cost > best_cost:
                best_cost = cost
                best_path = path

        for child in valid_moves(roads, todo, path, cost):
            fringe.append(child)

    # print(best_cost, [names[x] for x in best_path])

    return best_cost


def test():
    assert solve('A to B = 1') == 1
    assert solve('A to B = 1\nC to B = 2') == 3
    assert solve('A to B = 1\nC to B = 2\nA to C = 1') == 3


    problem = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".strip()

    assert solve(problem) == 982


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
