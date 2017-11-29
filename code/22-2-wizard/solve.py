#!/usr/bin/env python3
import heapq
import itertools
import math
import re


class PriorityQueue:
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.counter = itertools.count()     # unique sequence count

    def __len__(self):
        return len(self.pq)

    def append(self, task, priority=0):
        count = next(self.counter)
        entry = (priority, count, task)
        heapq.heappush(self.pq, entry)

    def pop(self):
        if self.pq:
            priority, count, task = heapq.heappop(self.pq)
            return task
        raise KeyError('pop from an empty priority queue')


# player: hp, dmg, armor, mana
ihp = 0
idmg = 1
iarmor = 2
imana = 3


# spell: name, cost, timer, damage, heal, armor, mana
lname = 0
lcost = 1
ltimer = 2
ldamage = 3
lheal = 4
larmor = 5
lmana = 6

spells = (
    ('Magic Missile', 53, 0, 4, 0, 0, 0),
    ('Drain', 73, 0, 2, 2, 0, 0),
    ('Shield', 113, 6, 0, 0, 7, 0),
    ('Poison', 173, 6, 3, 0, 0, 0),
    ('Recharge', 229, 5, 0, 0, 0, 101),
)

def parse_stats(text):
    hp = re.findall(r'Hit Points: (\d+)', text)[0]
    d = re.findall(r'Damage: (\d+)', text)[0]
    return tuple(map(int, (hp, d)))


def apply_ef(player, boss, name, cost, timer, damage, heal, armor, mana):
    if name == 'Shield':
        player[iarmor] = armor if timer > 0 else 0
    elif name == 'Magic Missile':
        boss[ihp] -= damage
    elif name == 'Drain':
        boss[ihp] -= damage
        player[ihp] += heal
    elif timer > 0:
        if name == 'Poison':
            boss[ihp] -= damage
        elif name == 'Recharge':
            player[imana] += mana


def apply_effects(player, boss, effects):
    res = []
    for ef in effects:
        timer = ef[ltimer]
        apply_ef(player, boss, *ef)

        if timer > 0:
            ef = list(ef)
            ef[ltimer] = timer - 1
            res.append(ef)

    return res


def valid_moves(player, boss, mana_spent, effects, player_turn, history):
    player = list(player)
    boss = list(boss)

    if player_turn:
        player[ihp] -= 1

    if player[ihp] <= 0:
        return

    effects = apply_effects(player, boss, effects)

    if player[ihp] <= 0:
        return

    if player_turn:
        for spell in spells:
            cost,timer = spell[lcost], spell[ltimer]

            if cost > player[imana]:
                continue

            if timer == 0:
                p = list(player)
                b = list(boss)
                p[imana] -= cost
                apply_ef(p, b, *spell)
                yield (p, b, mana_spent + cost, effects, not player_turn, history + [spell[lname]])

            else:
                name = spell[lname]
                if not any(x[lname] == name and x[ltimer] > 0 for x in effects):
                    p = list(player)
                    p[imana] -= cost
                    efs = effects + [spell]
                    yield (p, boss, mana_spent + cost, efs, not player_turn, history + [spell[lname]])

    else:
        if boss[ihp] > 0:
            player[ihp] -= max(1, boss[idmg] - player[iarmor])
        yield (player, boss, mana_spent, effects, not player_turn, history + ['(boss)'])


def replay(player, boss, history):
    import time

    player = list(player)
    boss = list(boss)
    player_turn = True
    effects = []

    def report_effects(name, cost, timer, damage, heal, armor, mana):
        if timer > 0:
            timer -= 1
            if name == 'Magic Missile':
                pass
            elif name == 'Drain':
                pass
            elif name == 'Shield':
                print('Shield\'s timer is now {}.'.format(timer))
            elif name == 'Poison':
                print('Poison deals 3 damage; its timer is now {}.'.format(timer))
            elif name == 'Recharge':
                print('Recharge provides 101 mana; its timer is now {}.'.format(timer))


    for h in history:
        print()
        time.sleep(1)

        if player_turn:
            player[ihp] -= 1

        if player[ihp] <= 0:
            print('Player is dead.')
            break

        print('-- Player turn --' if player_turn else '-- Boss turn --')
        print('- Player has {} hit points, {} armor, {} mana'.format(player[ihp], player[iarmor], player[imana]))
        print('- Boss has {} hit points'.format(boss[ihp]))

        orig_effects = list(effects)
        effects = apply_effects(player, boss, effects)

        for ef in orig_effects:
            report_effects(*ef)

        if boss[ihp] <= 0:
            print('This kills the boss, and the player wins.')
            break

        if h == '(boss)':
            dmg = max(1, boss[idmg] - player[iarmor])
            print('Boss attacks for {} - {} = {} damage!'.format(boss[idmg], player[iarmor], dmg))
            player[ihp] -= dmg

        elif h == '(pass)':
            pass

        else:
            print('Player casts {}.'.format(h))
            spell = next(filter(lambda x: x[lname] == h, spells))
            cost,timer = spell[lcost], spell[ltimer]
            player[imana] -= cost

            if timer == 0:
                apply_ef(player, boss, *spell)
            else:
                effects.append(list(spell))

        if player[ihp] <= 0:
            print('Player is dead.')
            break

        if boss[ihp] <= 0:
            print('This kills the boss, and the player wins.')
            break

        player_turn = not player_turn


def solve(problem, hp=50, mana=500):
    boss = parse_stats(problem)

    dmg = 0
    armor = 0
    player = (hp, dmg, armor, mana)
    effects = tuple()
    mana_spent = 0
    player_turn = True

    fringe = PriorityQueue()

    fringe.append((player, boss, mana_spent, effects, player_turn, []), mana_spent)

    while len(fringe) > 0:
        current = fringe.pop()
        player, boss, mana_spent = current[:3]

        if boss[ihp] <= 0 and player[ihp] > 0:
            # print(mana_spent, current[5])
            # replay((hp, dmg, armor, mana), parse_stats(problem), current[5])
            return mana_spent

        if player[ihp] <= 0:
            continue;

        for child in valid_moves(*current):
            mana_spent = child[2]
            fringe.append(child, mana_spent)

    print('oops')


def test():
    problem = """
Hit Points: 21
Damage: 3
""".strip()

    assert solve(problem, hp=10, mana=250) == 641


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
