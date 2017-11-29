#!/usr/bin/env python3
import itertools
import re


instr_rx = re.compile(r'\s*(hlf|tpl|inc|jmp|jie|jio)\s*(?:([ab])|([+-]?\d+))?\s*(?:,\s*([+-]?\d+))?')

def parse_instr(text):
    m = instr_rx.match(text)

    instr = m.group(1)
    x = None
    y = None

    if m.group(2):
        x = m.group(2)
    elif m.group(3):
        x = int(m.group(3))

    if m.group(4):
        y = int(m.group(4))

    return (instr, x, y)


def make_state(a=0, b=0):
    return {
        'a': a,
        'b': b,
    }


def dump_state(prog, ip, state):
    prog = '\n'.join('{:2}:  {}'.format(i, ' '.join(str(x) for x in p)) for i,p in enumerate(prog))
    state = ' '.join('{}:{}'.format(k, v) for k,v in state.items())
    return 'ip:{} {}\n{}'.format(ip, state, prog)


def vm(prog, state):
    ip = 0
    last_state = (ip, state['a'], state['b'])
    prog = list(prog)
    instr_count = 0

    # print('-- ', instr_count)
    # print(dump_state(prog, ip, state))

    while ip >= 0 and ip < len(prog):
        instr,x,y = prog[ip]

        instr_count += 1

        # print(ip, instr, x, y)

        if instr == 'nop':
            pass

        elif instr == 'hlf':
            state[x] = state[x] // 2

        elif instr == 'tpl':
            state[x] = 3 * state[x]

        elif instr == 'inc':
            state[x] = state[x] + 1

        elif instr == 'jmp':
            ip += x - 1

        elif instr == 'jie':
            if state[x] % 2 == 0:
                ip += y - 1

        elif instr == 'jio':
            if state[x] == 1:
                ip += y - 1

        else:
            raise Exception('invalid instruction {}: {}'.format(ip, prog[ip]))

        ip += 1

        # print('  ', state)


        current_state = (ip, state['a'], state['b'])
        if current_state == last_state:
            print('! killed')
            break
        else:
            last_state = current_state

    # return state


def solve(problem):
    prog = [parse_instr(s) for s in problem.splitlines()]

    state = make_state()
    vm(prog, state)

    return state['b']


def test():
    assert parse_instr('hlf a') == ('hlf', 'a', None)
    assert parse_instr('tpl b') == ('tpl', 'b', None)
    assert parse_instr('inc a') == ('inc', 'a', None)
    assert parse_instr('jmp +31') == ('jmp', 31, None)
    assert parse_instr('jmp -22') == ('jmp', -22, None)
    assert parse_instr('jie a, +21') == ('jie', 'a', 21)
    assert parse_instr('jio b, -18') == ('jio', 'b', -18)

    assert solve('inc b') == 1

    problem = """
inc b
jmp +2
inc b
""".strip()

    assert solve(problem) == 1

    problem = """
inc b
jio b, +2
inc b
""".strip()

    assert solve(problem) == 1

    problem = """
inc b
tpl b
jio b, +2
inc b
""".strip()

    assert solve(problem) == 4

    problem = """
inc b
jie b, +2
tpl b
""".strip()

    assert solve(problem) == 3


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
