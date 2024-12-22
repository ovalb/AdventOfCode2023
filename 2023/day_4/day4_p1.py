input = open("input").read().splitlines()

sum = 0

for row in input:
    [w, owned] = row.split("|")
    winning = w.split(":")[1]

    winning = [int(w) for w in winning.strip().split(" ") if w != ""]
    owned = [int(o) for o in owned.strip().split(" ") if o != ""]

    points = 0
    for own in owned:
        if own in set(winning):
            points = 1 if points == 0 else points*2
    
    sum += points
    
print(sum)




