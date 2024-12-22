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
for s in seeds:
    cur = s
    for m in maps:
        if cur < m[0][1] or cur > m[-1][1] + m[-1][2]:
            continue

        i = 0
        while i < len(m) and cur >= m[i][1]:
            i += 1
        
        if cur <= m[i-1][1] + m[i-1][2]:
            cur += m[i-1][0] - m[i-1][1]
    
    res = min(res, cur)

print("result is: ", res)
