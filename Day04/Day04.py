#!/usr/bin/env python3
import sys

dirs = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def neigh(g, x, y):
    h, w = len(g), len(g[0])
    return sum(
        0 <= x+dx < w and 0 <= y+dy < h and g[y+dy][x+dx] == '@'
        for dx, dy in dirs
    )

def main():
    with open(sys.argv[1]) as f:
        g = [list(l.strip()) for l in f if l.strip()]
    h, w = len(g), len(g[0])

    p1 = sum(
        neigh(g, x, y) < 4
        for y in range(h) for x in range(w)
        if g[y][x] == '@'
    )
    print(p1)

    g2 = [row[:] for row in g]
    total = 0
    while True:
        rem = [(x, y) for y in range(h) for x in range(w)
               if g2[y][x] == '@' and neigh(g2, x, y) < 4]
        if not rem:
            break
        for x, y in rem:
            g2[y][x] = '.'
        total += len(rem)
    print(total)

if __name__ == "__main__":
    main()

