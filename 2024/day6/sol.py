field = [list(x) for x in open('in').read().split('\n')]

def find_starting(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == '^':
                return i, j


inbound = lambda x,y: 0 <= x < len(field) and 0 <= y < len(field[0])
dirs = [(-1,0), (0,1), (1, 0), (0, -1)]

move = lambda i, y, x : (i + dirs[x][0], y + dirs[x][1])

def next_step(i, y, dix, field):
    ni, ny = i + dirs[dix][0], y + dirs[dix][1]
    while inbound(ni, ny) and field[ni][ny] == '#':
        dix = (dix + 1) % 4
        ni, ny = i + dirs[dix][0], y + dirs[dix][1]
    return ni, ny, dix


def p1():
    i, y = find_starting(field)
    dix = 0
    visited = { (i, y) }

    while (step := next_step(i, y, dix, field)) and inbound(step[0], step[1]):
        i, y, dix = step
        visited.add((i, y))

    return len(visited)

# kinda slow
def p2():
    def detect_loop(field, starting):
        i, y = starting
        dix = 0
        visited = { (i, y, dix) }
        while (step := next_step(i, y, dix, field)) and inbound(step[0], step[1]):
            i, y, dix = step
            if (i, y, dix) in visited:
                return True
            else: 
                visited.add((i, y, dix))
        return False

    si, sy = find_starting(field)
    i, y = si, sy
    dix = 0
    blockers = set()

    while (step := next_step(i, y, dix, field)) and inbound(step[0], step[1]):
        ni, ny, nix = step
        if inbound(ni, ny) and field[ni][ny] != '#' and (ni, ny) != (si, sy):
            # new_field = copy.deepcopy(field) # dont use deepcopy, very slow

            prev = field[ni][ny]
            field[ni][ny] = "#"
            if detect_loop(field, (si, sy)):
                blockers.add((ni, ny))
            field[ni][ny] = prev
        i, y, dix = ni, ny, nix
    return len(blockers)

print(p1())
print(p2())