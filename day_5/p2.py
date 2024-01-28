input = open("input").read().splitlines()
seeds = [int(x) for x in input[0].split(":")[1].strip().split(' ')]

maps = []

idx = -1
for row in input[1:]:
    if "map:" in row:
        idx += 1
        maps.append([])
    elif row != '':
        maps[idx].append([int(x) for x in row.strip().split(' ')])

# sort maps by source 
for m in maps:
    m.sort(key=lambda x:x[1])

res = float('inf')

i = 0
ranges = []
for i in range(0, len(seeds), 2):
    ranges.append((seeds[i], seeds[i] + seeds[i+1]))

# print(ranges)

def posInRanges(rg, rgList):
    for i, r in enumerate(rgList):
        if rg[0] < r[1] and r[0] < rg[1]:
            return i
    return -1

def findMin(t: tuple, i: int):
    if i == len(maps):
        return t[0]

    m = maps[i]
    # make sure its either < or <=
    # make sure the last point works
    points = [t[0]]
    for mp in m:
        if t[0] < mp[1] and mp[1] < t[1]:
            points.append(mp[1])
        if t[0] < mp[1] + mp[2] and mp[1] + mp[2] < t[1]:
            points.append(mp[1] + mp[2])
    if points[-1] != t[1]:
        points.append(t[1])

    points = list(dict.fromkeys(points))

    j = 0
    mins = []
    for j in range(0, len(points)-1):
        cur = (points[j], points[j+1])
        newM = [(x[1], x[1]+x[2]) for x in m]
        pos = posInRanges(cur, newM)

        offset = 0 if pos == -1 else m[pos][0] - m[pos][1]
        next = (cur[0] + offset, cur[1] + offset)
        # print(f"from {i} to {i+1} -> {next}")
        mins.append(findMin(next, i+1))        
    
    return min(mins)


fm = []
for r in ranges:
    fm.append(findMin(r, 0))

res = min(fm)
print(res)