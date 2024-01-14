input = open("input").read().splitlines()

sum = 0
dict = {}

for n, row in enumerate(input):
    [w, owned] = row.split("|")
    winning = w.split(":")[1]

    winning = [int(w) for w in winning.strip().split(" ") if w != ""]
    owned = [int(o) for o in owned.strip().split(" ") if o != ""]

    points = 0
    for own in owned:
        if own in set(winning):
            points += 1
    
    multip = dict[n] if n in dict else 1
    for x in range(n+1, min(n+points+1, len(input))):
        dict[x] = dict[x] + multip if x in dict else multip + 1

for i in range(0, len(input)):
    sum += dict[i] if i in dict else 1


print(sum)




