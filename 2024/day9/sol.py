disk = open('in').read()

# This solution looks cleaner than mine (and is a bit faster)
# https://gitlab.com/0xdf/aoc2024/-/raw/main/day09/day9.py?ref_type=heads

def init_disk(input):
    space = [x for i, x in enumerate(list(input)) if i % 2 != 0]
    files = [x for i, x in enumerate(list(input)) if i % 2 == 0]

    disk = list()
    for id, file in enumerate(files):
        disk.extend([id] * int(file))
        if id < len(space):
            disk.extend(['.'] * int(space[id]))
    return disk

def checksum(disk):
    return sum(i * int(v) for i, v in enumerate(disk) if v != '.')

def p1(input):
    disk = init_disk(input)

    sp = 0
    fp = len(disk) - 1

    while sp < fp:
        while disk[sp] != '.' and sp + 1 < len(disk):
            sp += 1
        while disk[fp] == '.' and fp > 0:
            fp -= 1
        
        if sp < fp:
            disk[fp], disk[sp] = disk[sp], disk[fp]
    return checksum(disk)

def p2(input):
    disk = init_disk(input)

    def compute_idx_len(disk, is_file):
        files = []
        i = 0
        while i < len(disk):
            c = disk[i]
            if c == '.' if is_file else c != '.':
                i += 1
            else:
                s, l = i, 0
                while i < len(disk) and disk[i] == c: 
                    i, l = i+1, l+1
                files.append((s, l))
        return files

    files = compute_idx_len(disk, True)
    spaces = compute_idx_len(disk, False)

    found = None
    for fidx, flen in reversed(files):
        for sidx, slen in spaces:
            if sidx < fidx and flen <= slen:
                found = sidx
                break
        
        if found is not None:
            for i in range(flen):
                disk[fidx + i], disk[sidx + i] = disk[sidx + i], disk[fidx + i]

            spidx = next((i for i, s in enumerate(spaces) if s[0] == found), None)
            spaces[spidx] = (spaces[spidx][0] + flen, spaces[spidx][1] - flen)
            found = None

            
    
    return checksum(disk)

print(p1(disk))
print(p2(disk))