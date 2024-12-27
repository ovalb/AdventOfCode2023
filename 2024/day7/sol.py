import functools

rows = open('in').read().split('\n')

equations = {}

for r in rows:
    splitted = r.split(':')
    res = int(splitted[0])

    terms = [int(s) for s in splitted[1].strip().split(' ')]
    equations[res] = terms

def cartesian_product(symbols, length):
    products = [[]]

    for _ in range(length):
        new_result = []
        for p in products:
            for s in symbols:
                new_result.append(p+[s])
        products = new_result
    return tuple(products)

products = {}
def memo_cartesian_product(symbol, length):
    ksymbol = ''.join(symbol)
    if (ksymbol, length) in products.keys():
        return products[(ksymbol, length)]
    else:
        r = cartesian_product(symbol, length)
        products[(ksymbol, length)] = r
        return r


def p1():
    def compute(t, ops):
        r = t[0]
        for i, op in enumerate(ops):
            r = r + t[i+1] if op == '+' else r * t[i+1]
        return r
    ans = 0
    for res, terms in equations.items():
        ops = memo_cartesian_product(['+', '*'], len(terms)-1)
        for op in ops:
            if compute(terms, op) == res:
                ans += res
                break
    return ans

def p2():
    def compute(t, ops):
        r = t[0]
        for i, op in enumerate(ops):
            if op == '||':
                r = int(str(r) + str(t[i+1]))
            else:
                r = r + t[i+1] if op == '+' else r * t[i+1]
        return r
    ans = 0
    for res, terms in equations.items():
        ops = memo_cartesian_product(['+', '*', '||'], len(terms)-1)
        for op in ops:
            if compute(terms, op) == res:
                ans += res
                break
    return ans

print(p1())
print(p2())

# def cartesian_product(symbols, repeat):
#     if repeat == 0:
#         # Base case: no more elements to choose, yield empty sequence
#         yield []
#     else:
#         # Generate all (repeat-1)-length sequences, then append each symbol
#         for partial in cartesian_product(symbols, repeat - 1):
#             for s in symbols:
#                 yield partial + [s]

# symbols = ['*', '+']
# for combo in cartesian_product(symbols, 3):
#     print(combo)

    
