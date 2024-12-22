from itertools import pairwise
import os
input = open("input").read()

reports = [list(map(lambda r: int(r), row.split(' '))) for row in input.split('\n')]

def is_safe(report):
    incr = report[0] <= report[1]
    fail_cond = lambda c, n: (
        (incr and (n < c + 1 or n > c + 3)) or
        (not incr and (n > c - 1 or n < c - 3)))

    for cur, next in pairwise(report):
        if fail_cond(cur, next):
            return False
    return True

def p1():
    return sum([1 if is_safe(r) else 0 for r in reports])

def p2():
    def is_safe_with_dampened(report):
        for i in range(len(report)):
            if is_safe(report[0:i] + report[i+1:]):
                return True
        return False

    return sum([1 if is_safe(r) or is_safe_with_dampened(r) else 0 for r in reports])

print(p1())
print(p2())



