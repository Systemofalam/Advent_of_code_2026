import sys
from math import prod

def parse(s):
    xs = s.rstrip("\n").splitlines()
    w = max(map(len, xs))
    return [x.ljust(w) for x in xs]

def blocks(g):
    h, w = len(g), len(g[0])
    empty = [all(g[r][c] == " " for r in range(h)) for c in range(w)]
    res, on = [], False
    for c in range(w):
        if not empty[c] and not on:
            on, start = True, c
        elif empty[c] and on:
            on = False
            res.append((start, c - 1))
    if on:
        res.append((start, w - 1))
    return res

def part1(g):
    h = len(g)
    total = 0
    for a, b in blocks(g):
        op = "+" if "+" in g[-1][a:b+1] else "*"
        nums = [int(g[r][a:b+1].strip()) for r in range(h - 1) if g[r][a:b+1].strip()]
        total += sum(nums) if op == "+" else prod(nums)
    return total

def part2(g):
    h = len(g)
    total = 0
    for a, b in blocks(g):
        op = "+" if "+" in g[-1][a:b+1] else "*"
        nums = []
        for c in range(a, b + 1):
            ds = [g[r][c] for r in range(h - 1) if g[r][c].isdigit()]
            if ds:
                nums.append(int("".join(ds)))
        total += sum(nums) if op == "+" else prod(nums)
    return total

def main():
    g = parse(open(sys.argv[1]).read())
    print(part1(g))
    print(part2(g))

if __name__ == "__main__":
    main()

