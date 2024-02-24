from collections import namedtuple, defaultdict
from enum import Enum
import functools

Hand = namedtuple("Hand", ["cards", "bid"])
all_cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


class HandTypes(Enum):
    FIVE_OF_A_KIND = 5
    FOUR_OF_A_KIND = 4
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 2
    TWO_PAIR = 1
    ONE_PAIR = 0
    HIGH = -1


def get_hand_type(cards: Hand.cards) -> int:
    dict = defaultdict(int)

    jokers = cards.count("J")
    for c in cards:
        if c != "J":
            dict[c] += 1

    d = sorted(dict.values(), reverse=True)
    d = [jokers] if not d else [d[0] + jokers] + d[1:]

    pattern_to_hand = {
        tuple([5]): HandTypes.FIVE_OF_A_KIND,
        tuple([4, 1]): HandTypes.FOUR_OF_A_KIND,
        tuple([3, 2]): HandTypes.FULL_HOUSE,
        tuple([3, 1, 1]): HandTypes.THREE_OF_A_KIND,
        tuple([2, 2, 1]): HandTypes.TWO_PAIR,
        tuple([2, 1, 1, 1]): HandTypes.ONE_PAIR,
        tuple([1, 1, 1, 1, 1]): HandTypes.HIGH,
    }

    return pattern_to_hand[tuple(d)].value


def compare_strength(a: Hand, b: Hand) -> int:
    ta, tb = (get_hand_type(a.cards), get_hand_type(b.cards))
    if ta - tb != 0:
        return ta - tb
    else:
        for ca, cb in zip(a.cards, b.cards):
            card_values = {c: len(all_cards) - i for i, c in enumerate(all_cards)}
            va, vb = (card_values[ca], card_values[cb])
            if va - vb != 0:
                return va - vb


rows = open("input").read().split("\n")

hands = []
for r in rows:
    rr = r.split(" ")
    hands.append(Hand(cards=rr[0], bid=int(rr[1])))

hands = sorted(hands, key=functools.cmp_to_key(compare_strength))

res = 0
for i, h in enumerate(hands):
    res += (i + 1) * h.bid

print(res)
