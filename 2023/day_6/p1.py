lines = open('sample').read().split('\n')

times = [ int(l) for l in lines[0].split(':')[1].strip().split(' ') if l != '' ]
distance = [ int(l) for l in lines[1].split(':')[1].strip().split(' ') if l != '' ]

tot = []
for (t, d) in zip(times, distance):
    rg = []
    for lt in range(0, t):
        if len(rg) == 0 and lt * (t-lt) > d:
            rg.append(lt)
            continue

        if len(rg) == 1 and lt * (t-lt) <= d:
            rg.append(lt)

    tot.append(rg)

    

print(tot)
res = 1

for [a, b] in tot:
    print(f"{b} - {a}")
    res *= (b - a)

print(res)

    
    
