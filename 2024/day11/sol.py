import sys
from collections import defaultdict

input = open(sys.argv[1]).read()


def p1(input):
    stones = [int(i) for i in input.split(' ')]
    def blink(stones):
        result = []
        for s in stones:
            if s == 0:
                result.append(1)
            elif len(str(s)) % 2 == 0:
                n = len(str(s)) // 2
                left, right = str(s)[:n], str(s)[n:]
                result.extend([int(x) for x in [left, right]])
            else:
                result.append(int(s) * 2024)
        return result

    for _ in range(6):
        stones = blink(stones)
        print(stones)
    return len(stones)


def p2(input):
    stones = defaultdict(lambda: 0, {int(i): 1 for i in input.split(' ')})

    def blink(s):
        
        # todo: I was trying to solve it in place
        for k in stones:
            if k == 0:
                s[k] -= 1 
                s[1] += 1 
                # result[1] = 1 if 1 not in stones else stones[1] + 1
            elif len(str(k)) % 2 == 0:
                n = len(str(k)) // 2
                l, r = int(str(k)[:n]), int(str(k)[n:])
                s[k] -= 1
                s[l] += 1
                s[r] += 1
            else:
                m = int(k) * 2024
                s[k] -= 1
                s[m] += 1
        return s

    print(stones)
    for _ in range(6):
        stones = blink(stones)
        print(stones)
    
    return sum(stones.values())

print("p1: ", p1(input))
print("p2: ", p2(input))
