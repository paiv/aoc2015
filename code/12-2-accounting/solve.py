#!/usr/bin/env python3
import json
import re


num_rx = re.compile(r'-?\d+')


def exclude_reds(text):
    def filt(o):
        if isinstance(o, dict):
            res = dict()
            for k,v in o.items():
                if v == "red":
                    return None
                res[k] = filt(v)
            return res
        elif isinstance(o, list):
            return [filt(x) for x in o]
        else:
            return o

    obj = json.loads(text)
    obj = filt(obj)
    return json.dumps(obj)


def solve(problem):
    text = exclude_reds(problem)
    return sum(int(x) for x in num_rx.findall(text))


def test():
    assert solve('[1,2,3]') == 6
    assert solve('{"a":2,"b":4}') == 6
    assert solve('[[[3]]]') == 3
    assert solve('{"a":{"b":4},"c":-1}') == 3
    assert solve('{"a":[-1,1]}') == 0
    assert solve('[-1,{"a":1}]') == 0
    assert solve('[]') == 0
    assert solve('{}') == 0

    assert solve('[1,{"c":"red","b":2},3]') == 4
    assert solve('{"d":"red","e":[1,2,3,4],"f":5}') == 0
    assert solve('[1,"red",5]') == 6


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
