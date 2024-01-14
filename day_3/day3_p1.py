input = open("input").read().splitlines()

def containsSymbol(str):
    for s in str:
        if not (s == '.' or s.isdigit()):
            return True
    return False

num = ""
sum = 0

for r, row in enumerate(input):
    for c, ch in enumerate(row):
        if (not ch.isdigit() and num != "") or (c == len(row) - 1):
            num = num + ch if ch.isdigit() else num

            right = c if ch.isdigit() and c == len(row) - 1 else c - 1
            left = max(right - len(num), 0)
            roffset = 0 if right == c else 1

            if num != "":
                def partNumberOrZero():
                    for i in range(max(0, r-1), min(r+2, len(input))):
                        for y in range(left, right+roffset+1):
                            if not (input[i][y] == "." or input[i][y].isdigit()):
                                out = int(num)
                                return out
                    return 0
                sum += partNumberOrZero()
                num = ""

        elif ch.isdigit():
            num += ch


print(f"total {sum}")


