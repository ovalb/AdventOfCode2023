import re

lines = open("sample").read().split("\n")


def expandHorizontal(lines):
    expanded = []
    for line in lines:
        expanded.append(line)
        if re.findall("#", line) == []:
            expanded.append(line)
    return expanded


def transpose(m):
    return ["".join([m[j][i] for j in range(len(m))]) for i in range(len(m[0]))]


# expand universe
for times in range(2):
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

print(f"sol1 is {sum}")
