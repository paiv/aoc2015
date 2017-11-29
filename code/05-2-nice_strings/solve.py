#!/usr/bin/env python3


def check(text):

    if not any(text[i] == text[i+2] for i in range(0, len(text) - 2)):
        return False

    f = False
    for i in range(0, len(text) - 2):
        pair = text[i:i+2]
        if text.find(pair, i + 2) > 0:
            f = True
            break

    if not f:
        return False

    return True


def solve(problem):
    return sum(check(x) for x in problem.splitlines())


def test():
    assert check('qjhvhtzxzqqjkmpb') == True
    assert check('xxyxx') == True
    assert check('uurcxstgmygtbstg') == False
    assert check('ieodomkazucvgmuy') == False

    problem = """
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
""".strip()

    assert solve(problem) == 2


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
