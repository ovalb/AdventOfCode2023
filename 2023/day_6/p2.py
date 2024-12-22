lines = open('input').read().split('\n')

t = int(''.join([ l for l in lines[0].split(':')[1].strip().split(' ') if l != '' ]))
d = int(''.join([ l for l in lines[1].split(':')[1].strip().split(' ') if l != '' ]))

tot = []
rg = []

for lt in range(0, t):
    if lt * (t-lt) > d:
        rg.append(lt)
        break

for le in range(t, 0, -1):
    if le * (t-le) >= d:
        rg.append(le)
        break

print(f"le: {rg[0]} lt: {rg[1]}")
print(rg[1] - rg[0] + 1)