import sys
tmap = [ [int(rr) for rr in list(r)] for r in open(sys.argv[1], 'r').read().split('\n')]

inbound = lambda x, y, m: 0 <= x < len(m) and 0 <= y < len(m[0]) 

def get_visited_nines(t, i, y, visited):
    if t[i][y] == 9 and (i, y) not in visited:
        return {(i, y)}
    
    local_visited = set()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, ny = i+dx, y+dy
        if inbound(ni, ny, t) and t[ni][ny] == t[i][y] + 1:
            local_visited |= get_visited_nines(t, ni, ny, visited)
    return visited | local_visited
            
def get_rating(t, i, y, rating):
    if t[i][y] == 9:
        return 1

    local_rating = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, ny = i+dx, y+dy
        if inbound(ni, ny, t) and t[ni][ny] == t[i][y] + 1:
            local_rating += get_rating(t, ni, ny, rating)
    return rating + local_rating



visited = set()
p1 = 0
p2 = 0
for i in range(len(tmap)):
    for y in range(len(tmap[0])):
        if tmap[i][y] != 0:
            continue

        visited |= get_visited_nines(tmap, i, y, set())
        p1 += len(visited)
        visited = set()

        p2 += get_rating(tmap, i, y, 0)

print("p1: ", p1)
print("p2: ", p2)