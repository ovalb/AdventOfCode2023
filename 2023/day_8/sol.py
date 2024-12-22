from collections import defaultdict, namedtuple
import re
from math import lcm
from functools import reduce


rows = open("input").read()


def parse_network(r: str) -> dict:
    dict = defaultdict()
    for n in r.split("\n"):
        matches = re.findall("[A-Z0-9]{3}", n)
        if len(matches) == 3:
            dict[matches[0]] = [matches[1], matches[2]]
    return dict


ops = rows.split("\n\n")[0]
network = parse_network(rows.split("\n\n")[1])


def ops_generator(ops):
    while True:
        for op in ops:
            yield 0 if op == "L" else 1


KeyDist = namedtuple("KeyDist", ["key", "dist"])
op = ops_generator(ops)


def part1():
    key = "AAA"
    hops = 0

    while key != "ZZZ":
        key = network[key][next(op)]
        hops += 1
    return hops


def part2():
    def next_hop(key: str):
        hops = 0
        while not key.endswith("Z"):
            key = network[key][next(op)]
            hops += 1
        return KeyDist(key, dist=hops)

    zkeydists = [next_hop(key) for key in network.keys() if key.endswith("A")]
    return reduce(lcm, [kd.dist for kd in zkeydists])


sol1 = part1()
print(f"p1: {sol1}")

sol2 = part2()
print(f"p2: {sol2}")
