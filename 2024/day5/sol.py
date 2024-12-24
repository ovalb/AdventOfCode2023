rows = open('in').read().split('\n')

rules = [r.split('|') for r in rows if "|" in r]
insertions = [r.split(',') for r in rows if "," in r]

ru = dict()
for l,r in rules:
    ru.setdefault(l, []).append(r)

  
def is_valid(ins):
    for i, e in enumerate(ins):
        if e in ru and set(ins[0:i]) & set(ru[e]):
            return False
    return True

def fix_it(b):
    i = 0
    while i < len(b):
        e = b[i]
        if e in ru:
            wrongs = set(b[0:i]) & set(ru[e])
            if len(wrongs) > 0:
                w = next(iter(wrongs))
                idx = b.index(w)
                b[i], b[idx] = b[idx], b[i]
                i = 0
        i+=1
    return b

def p1():
    ans = 0
    for ins in insertions:
        if is_valid(ins):
            ans += int(ins[len(ins) // 2])
    return ans

def p2():
    ans = 0
    for ins in insertions:
        if not is_valid(ins):
            fixed = fix_it(ins)
            ans += int(fixed[len(ins) // 2])
    return ans

print(p1())
print(p2())