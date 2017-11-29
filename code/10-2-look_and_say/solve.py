#!/usr/bin/env python3


def lookandsay(text):
    c = text[0]
    n = 0
    res = []
    for x in text:
        if x != c:
            res.extend([str(n), c])
            n = 1
            c = x
        else:
            n += 1
    else:
        res.extend([str(n), c])

    return ''.join(res)


def solve(problem, n=50):
    text = problem
    for i in range(0, n):
        text = lookandsay(text)
    return len(text)


def test():
    assert lookandsay('1') == '11'
    assert lookandsay('11') == '21'
    assert lookandsay('21') == '1211'
    assert lookandsay('1211') == '111221'
    assert lookandsay('111221') == '312211'

    assert solve('1', 5) == 6


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
