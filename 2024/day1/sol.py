
lines = open("input").read().split('\n')

left = []
right = []

for line in lines:
    l, r = line.split(" " * 3)
    left.append(int(l))
    right.append(int(r))

def p1(left, right):
    return sum ([abs(l - r) for l, r in zip(sorted(left), sorted(right))])

def p2(left, right):
    m = dict()
    for r in right:
        m[r] = m[r] + 1 if r in m else 1

    return sum ([l * m[l] if l in m else 0 for l in left])

print(p1(left, right))
print(p2(left, right))



        


