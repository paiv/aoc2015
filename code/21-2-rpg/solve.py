#!/usr/bin/env python3
import itertools
import math
import re


def parse_shop(text, zero=0):
    # name, cost, damage, armor
    shop = [line.strip().split() for line in text.strip().splitlines()]
    a = [(line[0], *map(int, line[1:])) for line in shop]
    for i in range(zero):
        a.append(('(none)', 0, 0, 0))
    return sorted(a, key=lambda x: x[1])


weapons = parse_shop("""
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
""")

armor = parse_shop("""
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
""", zero=1)

rings = parse_shop("""
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3
""", zero=2)


def parse_stats(text):
    hp = re.findall(r'Hit Points: (\d+)', text)[0]
    d = re.findall(r'Damage: (\d+)', text)[0]
    a = re.findall(r'Armor: (\d+)', text)[0]
    return tuple(map(int, (hp, d, a)))


def fight(boss, equip, hp):
    dmg = sum(x[2] for x in equip)
    armor = sum(x[3] for x in equip)

    boss_moves = math.ceil(hp / max(1, boss[1] - armor))
    player_moves = math.ceil(boss[0] / max(1, dmg - boss[2]))

    return 0 if player_moves > boss_moves else hp


def solve(problem, hp=100):
    boss = parse_stats(problem)

    equip = ((w[1] + a[1] + r1[1] + r2[1], w,a,r1,r2)
                for w in weapons
                for a in armor
                for r1, r2 in set(itertools.combinations(rings, 2)))
    equip = sorted(equip, key=lambda x: -x[0])

    for i in equip:
        if fight(boss, i[1:], hp) <= 0:
            return i[0]


def test():
    pass


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
