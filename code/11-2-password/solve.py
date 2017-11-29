#!/usr/bin/env python3


excl = set(list('iol'))


def valid(text):
    if any(c in excl for c in text):
        return False

    xyz = False
    for i in range(0, len(text) - 2):
        x = ord(text[i])
        if text[i+1] == chr(x + 1) and text[i+2] == chr(x + 2):
            xyz = True
            break
    if not xyz:
        return False

    aa = set(text[i:i+2] for i in range(0, len(text) - 1) if text[i] == text[i+1])
    if len(aa) < 2:
        return False

    return True


def inc(x, carry=1):
    if carry:
        a = ord('a')
        y = chr(a + ((ord(x) - a + carry) % 26))
        carry = 1 if x == 'z' else 0
    else:
        y = x
    return (y, carry)


def increment(text):
    a = ord('a')
    text = list(text)

    for q in excl:
        if q in text:
            i = text.index(q)
            text[i+1:] = ['z'] * (len(text) - i - 1)

    carry = 1
    res = []
    for i in range(len(text) - 1, -1, -1):
        x = text[i]
        y, carry = inc(x, carry)
        res.append(y)

    res.reverse()
    return ''.join(res)


def next_valid(text):
    ok = False
    while not ok:
        # print(text)
        text = increment(text)
        ok = valid(text)
    return text


def solve(problem):
    return next_valid(next_valid(problem))


def test():
    assert valid('abbcdxxy') == True
    assert valid('hijklmmn') == False
    assert valid('abbceffg') == False
    assert valid('abbcegjk') == False
    assert valid('abcabcab') == False
    assert valid('aaabcdef') == False
    assert valid('aabcdaaf') == False
    assert valid('abcdffaa') == True


    assert increment('a') == 'b'
    assert increment('z') == 'a'
    assert increment('xx') == 'xy'
    assert increment('xy') == 'xz'
    assert increment('xz') == 'ya'
    assert increment('ya') == 'yb'
    assert increment('abc') == 'abd'
    assert increment('xyz') == 'xza'
    assert increment('abcdjaza') == 'abcdjazb'

    assert increment('aibc') == 'ajaa'
    assert increment('aobc') == 'apaa'
    assert increment('albc') == 'amaa'

    # assert solve('abcdefgh') == 'abcdffaa'
    # assert solve('ghijklmn') == 'ghjaabcc'


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
