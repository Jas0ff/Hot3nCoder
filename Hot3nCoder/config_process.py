from itertools import product
from random import randint


def adjust_size():
    with open('config.txt', 'r', encoding='utf-8') as f:
        s = set(f.read().split(' '))
        if '' in s:
            s.remove('')

    stuff = 65
    while len(s) < 3:
        s.add(chr(stuff))
        stuff += 1

    with open('config.txt', 'w', encoding='utf-8') as f:
        for i in s:
            f.write(i+' ')


def get_emoji_size():
    with open('config.txt', 'r', encoding='utf-8') as f:
        return len(set(f.read().split(' ')))


def get_rand_emoji(length):
    eset = set()
    with open('config.txt', 'r', encoding='utf-8') as f:
        eset = set(f.read().split(' '))
        if '' in eset:
            eset.remove('')

    rest = eset.pop()

    stuff = 65
    while len(eset) < length:
        eset.add(chr(stuff))
        stuff += 1

    half_re = list(product(eset, repeat=length))
    result = []

    for i in half_re:
        word = ''.join(i)+randnum_rest(rest)
        result.append(word)

    return result


def randnum_rest(symbol):
    amount = randint(0, 3)
    s = ""
    for i in range(amount):
        s += symbol

    return s
