#!/usr/bin/env python3
import re


instr_rx = re.compile(r'(?:(NOT) (\w+)|(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+)|(\w+)) -> (\w+)')

def parse_instr(text):
    def px(x):
        try:
            return int(x)
        except:
            pass
        return x

    m = instr_rx.match(text)

    if m is None:
        raise Exception('unhandled input {}'.format(text))

    target = m.group(7)

    if m.group(1):
        x = px(m.group(2))
        return ((m.group(1), x, None), target)

    elif m.group(3):
        x = px(m.group(3))
        y = px(m.group(5))
        return ((m.group(4), x, y), target)

    elif m.group(6):
        x = px(m.group(6))
        return (x, target)


def parse_board(text):
    lines = text.splitlines()
    wires = [parse_instr(x) for x in lines]

    board = dict()
    for s,t in wires:
        board[t] = s

    assert len(board) == len(lines)

    return board


def query(board, wire, state=None):
    if isinstance(wire, int):
        return wire

    if state is None:
        state = dict()

    if wire in state:
        return state[wire]

    u = board[wire]
    out = None

    if isinstance(u, int):
        out = u
    elif isinstance(u, str):
        out = query(board, u, state)
    else:
        inst,x,y = u

        if inst == 'NOT':
            out = (~query(board, x, state)) & 0xffff
        elif inst == 'LSHIFT':
            out = (query(board, x, state) << query(board, y, state)) & 0xffff
        elif inst == 'RSHIFT':
            out = (query(board, x, state) >> query(board, y, state)) & 0xffff
        elif inst == 'AND':
            out = (query(board, x, state) & query(board, y, state)) & 0xffff
        elif inst == 'OR':
            out = (query(board, x, state) | query(board, y, state)) & 0xffff
        else:
            raise Exception('unhandled op {}'.format(u))

    state[wire] = out
    return out


def solve(problem):
    board = parse_board(problem)
    a = query(board, 'a')

    state = { 'b': a }
    a = query(board, 'a', state)

    return a


def test():
    assert parse_instr('123 -> x') == (123, 'x')
    assert parse_instr('456 -> yx') == (456, 'yx')
    assert parse_instr('x AND y -> d') == (('AND', 'x', 'y'), 'd')
    assert parse_instr('x OR y -> e') == (('OR', 'x', 'y'), 'e')
    assert parse_instr('x LSHIFT 2 -> f') == (('LSHIFT', 'x', 2), 'f')
    assert parse_instr('y RSHIFT 2 -> g') == (('RSHIFT', 'y', 2), 'g')
    assert parse_instr('NOT x -> h') == (('NOT', 'x', None), 'h')

    assert solve('1 -> a\n') == 1
    assert solve('1 -> x\nNOT x -> a') == 0xfffe

    problem = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> a
""".strip()

    assert solve(problem) == 65079


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    # test()
    print(solve(getinput()))
