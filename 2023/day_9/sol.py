from itertools import pairwise


def parse_input():
    input = open("input").read().split("\n")
    histories = [i.split(" ") for i in input]
    for i, h in enumerate(histories):
        histories[i] = [int(elem) for elem in h]
    return histories


def p1():
    def get_next_value(history: list) -> int:
        next = history
        rvalues = [history[-1]]
        while any([n != 0 for n in next]):
            next = [b - a for a, b in pairwise(next)]
            rvalues.append(next[-1])

        return sum(rvalues)

    s = sum([get_next_value(h) for h in histories])
    print(f"p1: {s}")


def p2():
    def get_prev_value(history: list) -> int:
        next = history
        lvalues = [history[0]]
        while any([n != 0 for n in next]):
            next = [b - a for a, b in pairwise(next)]
            lvalues.append(next[0])

        value = 0
        while len(lvalues) > 0:
            value = lvalues.pop() - value
        return value

    s = sum([get_prev_value(h) for h in histories])
    print(f"p2: {s}")


histories = parse_input()

p1()
p2()
