m = [list(r) for r in open('in').read().split('\n')]

antennas = {}
for row in range(len(m)):
    for col in range(len(m[0])):
        a = m[row][col]
        if a != '.':
            antennas.setdefault(a, []).append((row, col))

inbound = lambda x,y,m: 0 <= x < len(m) and 0 <= y < len(m[0])

def pairs(p):
    pairs = []
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            pairs.append((p[i], p[j]))
    return pairs

def p1():
    def find_antinodes(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        dx, dy = x1 - x2, y1 - y2
        an1 = x1 + dx, y1 + dy
        an2 = x2 - dx, y2 - dy

        return list(filter(lambda x: inbound(x[0], x[1], m), [an1, an2]))

    antinodes = set()
    for pos in antennas.values():
        for p1, p2 in pairs(pos):
            found = find_antinodes(p1, p2)
            antinodes.update(found)

    return len(antinodes)


def p2():
    def find_antinodes(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        dx, dy = x1 - x2, y1 - y2

        upper_anodes = []
        i = 0
        while True:
            cx, cy = x1 + (dx * i), y1 + (dy * i)
            if inbound(cx, cy, m):
                upper_anodes.append((cx, cy))
                i += 1
            else:
                break

        lower_anodes = []
        i = 0
        while True:
            cx, cy = x2 - (dx * i), y2 - (dy * i)
            if inbound(cx, cy, m):
                lower_anodes.append((cx, cy))
                i += 1
            else:
                break

        return upper_anodes + lower_anodes

    antinodes = set()
    for pos in antennas.values():
        for p1, p2 in pairs(pos):
            found = find_antinodes(p1, p2)
            antinodes.update(found)

    return len(antinodes)



    
print(p1())
print(p2())