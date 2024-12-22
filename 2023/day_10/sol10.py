import os
from collections import namedtuple
from itertools import pairwise

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
    wall = set()
    cur = valid_neighbors[0]
    wall.add(cur.p)
    while cur.p != S:
        cur = go_forward(cur)
        wall.add(cur.p)

    # for w in wall:
    #     print(w)

    return len(list(wall)) // 2


# using raytracing
def p2(grid):
    def reverses_number(i, y, wall):
        rev = 0
        for x in range(y + 1, len(grid[i])):
            if Pos(i, x) in wall and grid[i][x] in {"|", "L", "J"}:
                rev += 1
        return rev

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

    # replace S with real pipe
    for i, row in enumerate(grid):
        grid[i] = row.replace("S", s_char)

    result = 0
    for i, row in enumerate(grid):
        for y, _ in enumerate(row):
            if Pos(i, y) not in wall and reverses_number(i, y, wall) % 2 == 1:
                result += 1

    return result


def shoelaceArea(points):
    pairs = list(pairwise(points))
    pairs.append((pairs[-1][1], pairs[0][0]))
    p0 = 0
    p1 = 0
    for p in pairs:
        p0 += p[1].x * p[0].y
        p1 += p[1].y * p[0].x

    return abs(p0 - p1) / 2


# https://en.wikipedia.org/wiki/Pick%27s_theorem
# https://en.wikipedia.org/wiki/Shoelace_formula
# https://11011110.github.io/blog/2021/04/17/picks-shoelaces.html
# A = 1/2 * sum of (x'-x)(y'+y)
def p2_shoelace():
    S = findS()
    all_neighbors = [Elem(jump(S, dir), dir) for dir in ["N", "W", "E", "S"]]
    valid_neighbors = [n for n in all_neighbors if valid_elem(n)]
    wall = list()
    # print("len of valid ns should be 2: ", len(valid_neighbors))
    cur = valid_neighbors[0]
    first = cur
    while cur.p != S:
        cur = go_forward(cur)
        wall.append(cur.p)
    wall.append(first.p)

    A = shoelaceArea(wall)
    return A - len(wall) // 2 + 1


sol1 = p1()
print(f"sol1 is {sol1}")

sol2 = p2(grid.copy())
print(f"sol2 is {sol2}")

sol2_alt = p2_shoelace()
print(f"sol2 shoelace is {sol2_alt}")
