import re

lines = open("input").read().split("\n")


def expandHorizontal(lines):
    expanded = []
    for line in lines:
        expanded.append(line)
        if re.findall("#", line) == []:
            expanded.append(line)
    return expanded


def transpose(m):
    return [''.join(list(z)) for z in zip(*m)]


def p1(lines):
    # expand universe
    for _ in range(2):
        lines = expandHorizontal(lines)
        lines = transpose(lines)

    galaxies = list()
    for i, line in enumerate(lines):
        for y, ch in enumerate(line):
            if ch == "#":
                galaxies.append((i, y))

    pairs = []
    for i in range(len(galaxies) - 1):
        for y in range(i + 1, len(galaxies)):
            pairs.append((galaxies[i], galaxies[y]))

    sum = 0
    for p in pairs:
        [p0, p1] = p
        sum += abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])

    return sum

def get_empty_rows(matrix):
    rows = []
    for i, m in enumerate(matrix):
        if re.findall("#", m) == []:
            rows.append(i)
    return rows


def p2(lines):
    million_rows = get_empty_rows(lines)
    lines = transpose(lines)
    million_cols = get_empty_rows(lines)
    lines = transpose(lines)

    galaxies = list()
    for i, line in enumerate(lines):
        for y, ch in enumerate(line):
            if ch == "#":
                galaxies.append((i, y))

    pairs = []
    for i in range(len(galaxies) - 1):
        for y in range(i + 1, len(galaxies)):
            pairs.append((galaxies[i], galaxies[y]))

    sum = 0
    for p in pairs:
        [p0, p1] = p
        row_dist = abs(p0[0] - p1[0])
        col_dist = abs(p0[1] - p1[1])

        mrn = len(list(filter(lambda x: x >= min(p0[0], p1[0]) and x <= max(p0[0], p1[0]) , million_rows)))
        crn = len(list(filter(lambda x: x >= min(p0[1], p1[1]) and x <= max(p0[1], p1[1]) , million_cols)))

        exprate = 1e6
        sum += row_dist + col_dist + (exprate * mrn) - mrn + (exprate * crn) - crn

    return sum
    
print(f"sol1 is {p1(lines.copy())}")
print(f"sol2 is {p2(lines.copy())}")
