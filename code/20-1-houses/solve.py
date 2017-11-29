#!/usr/bin/env python3
import math


def solve0(problem):
    n = int(problem)

    def divs(n):
        a = int(math.sqrt(n))
        for i in range(1, a + 1):
            if n % i == 0:
                yield i
                if i * i != n:
                    yield n // i

    def sumdivs(n):
        return sum(divs(n))

    i = int(math.sqrt(n // 10))
    while True:
        if sumdivs(i) * 10 >= n:
            return i
        i += 1


def solve(problem):
    n = int(problem) // 10
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            a[j] += i

    for i,v in enumerate(a):
        if v >= n:
            return i


def test():
    assert solve('10') == 1
    assert solve('30') == 2
    assert solve('20') == 2
    assert solve('70') == 4
    assert solve('60') == 4
    assert solve('120') == 6
    assert solve('80') == 6
    assert solve('130') == 8
    assert solve('150') == 8


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
