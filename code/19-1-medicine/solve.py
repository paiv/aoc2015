#!/usr/bin/env python3


def parse_board(text):
    lines = text.splitlines()
    mol = lines[-1]
    rep = [line.split(' => ') for line in lines[:-1] if len(line.strip()) > 0]
    return (rep, mol)


def solve(problem):
    rep, mol = parse_board(problem)
    a = set(mol[:i] + mol[i:].replace(x, y, 1) for x,y in rep for i in range(len(mol)) if mol[i:].startswith(x))
    return len(a)


def test():

    problem = """
H => HO
H => OH
O => HH

HOH
""".strip()

    assert solve(problem) == 4

    problem = """
H => HO
H => OH
O => HH

HOHOHO
""".strip()

    assert solve(problem) == 7


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
