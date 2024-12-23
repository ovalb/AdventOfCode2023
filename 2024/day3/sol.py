import re

codes = open('in').read().split('\n')

def mult(code):
    ans = 0
    occ = re.findall(r'mul\(\d{1,3},\d{1,3}\)', code)
    for o in occ:
        [a, b] = re.findall(r'\d{1,3}', o)
        ans += int(a) * int(b)
    return ans

def p1(codes):
    return sum([mult(code) for code in codes])

def compute_valid_intervals(code):
    points = re.finditer(r"do\(\)|don't\(\)", code)
    isDo = True
    lastDo = 0

    intervals = []
    for p in points:
        if isDo and p.group() == "don't()": 
            intervals.append((lastDo, p.start()))
            isDo = False
        elif not isDo and p.group() == "do()": 
            lastDo = p.end()
            isDo = True
        else:
            pass
    if isDo:
        intervals.append((lastDo, len(code)))
    return intervals
   
def p2(codes):
    big = ''.join(codes)
    intervals = compute_valid_intervals(big)
    return sum(mult(big[s:e]) for (s, e) in intervals)

print(p1(codes))
print(p2(codes))