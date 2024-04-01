import os
from collections import namedtuple
from enum import Enum

directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, "input")
print(filepath)
grid = [line.strip() for line in open(filepath).readlines()]

Pos = namedtuple("Pos", "x y")
Elem = namedtuple("Elem", "p d")


def findS():
    for i, row in enumerate(grid):
        y = str(row).find("S")
        if y != -1:
            return Pos(i, y)


outdirs = {
    "|": ("N", "S"),
    "-": ("W", "E"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("S", "W"),
    "F": ("S", "E"),
}


def inbounds(p: Pos) -> bool:
    return not (p.x < 0 or p.y < 0 or p.x > len(grid) or p.y > len(grid[0]))


def flipdir(d: str) -> set:
    north_south, west_east = ({"N", "S"}, {"W", "E"})
    outset = north_south - set(d) if d in north_south else west_east - set(d)
    return outset.pop()


def valid_elem(elem: Elem) -> bool:
    ch = grid[elem.p.x][elem.p.y]
    return ch != "." and flipdir(elem.d) in outdirs[ch] and inbounds(elem.p)


def jump(pos: Pos, dir: str) -> Pos:
    jump_towards = {
        "N": lambda p: Pos(p.x - 1, p.y),
        "S": lambda p: Pos(p.x + 1, p.y),
        "W": lambda p: Pos(p.x, p.y - 1),
        "E": lambda p: Pos(p.x, p.y + 1),
    }
    return jump_towards[dir](pos)


def go_forward(elem: Elem) -> Elem:
    ch = grid[elem.p.x][elem.p.y]
    nextdirset = set(outdirs[ch]) - set(flipdir(elem.d))
    nextdir = nextdirset.pop()
    return Elem(jump(elem.p, nextdir), nextdir)


def p1():
    S = findS()
    all_neighbors = [Elem(jump(S, dir), dir) for dir in ["N", "W", "E", "S"]]
    valid_neighbors = [n for n in all_neighbors if valid_elem(n)]
    arr1 = [valid_neighbors[0]]
    arr2 = [valid_neighbors[1]]

    while True:
        n1, n2 = (arr1[-1], arr2[-1])
        posset1 = set([a[0] for a in arr1])
        posset2 = set([a[0] for a in arr2])

        if len(posset1 & posset2) != 0:
            return min(len(arr1), len(arr2))

        next1 = go_forward(n1)
        next2 = go_forward(n2)
        arr1.append(next1)
        arr2.append(next2)


# sol = p1()
# print("sol is:", sol)


def reverses_number(i, y, wall):
    rev = 0
    for x in range(y + 1, len(grid[i])):
        if Pos(i, x) in wall and grid[i][x] in {"|", "L", "J"}:
            rev += 1
    return rev


# using raytracing
def p2():
    S = findS()
    all_neighbors = [Elem(jump(S, dir), dir) for dir in ["N", "W", "E", "S"]]
    valid_neighbors = [n for n in all_neighbors if valid_elem(n)]
    wall = set()
    cur = valid_neighbors[0]
    wall.add(cur.p)
    while cur.p != S:
        cur = go_forward(cur)
        wall.add(cur.p)

    # understand what is S
    neighdir = (valid_neighbors[0].d, valid_neighbors[1].d)
    nd = neighdir if neighdir in outdirs.values() else (neighdir[1], neighdir[0])
    s_char = list(outdirs.keys())[list(outdirs.values()).index(nd)]
    print(f"s_char is {s_char}")

    # replace S with real pipe
    for i, row in enumerate(grid):
        grid[i] = row.replace("S", s_char)

    result = 0
    for i, row in enumerate(grid):
        for y, _ in enumerate(row):
            if Pos(i, y) not in wall and reverses_number(i, y, wall) % 2 == 1:
                print(f"({i},{y})")
                result += 1

    return result


sol2 = p2()
print(f"sol2 is {sol2}")

# https://en.wikipedia.org/wiki/Pick%27s_theorem
# https://en.wikipedia.org/wiki/Shoelace_formula
