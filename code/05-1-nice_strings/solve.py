#!/usr/bin/env python3
import string


vowels = set(list('aeiou'))
doubles = tuple(c * 2 for c in string.ascii_lowercase)
excl = ('ab', 'cd', 'pq', 'xy')


def check(text):
    if sum(c in vowels for c in text) < 3:
        return False

    if not(any(dd in text for dd in doubles)):
        return False

    if any(xx in text for xx in excl):
        return False

    return True


def solve(problem):
    return sum(check(x) for x in problem.splitlines())


def test():
    assert check('ugknbfddgicrmopn') == True
    assert check('aaa') == True
    assert check('jchzalrnumimnmhp') == False
    assert check('haegwjzuvuyypxyu') == False
    assert check('dvszwmarrgswjxmb') == False

    problem = """
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
""".strip()

    assert solve(problem) == 2


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
