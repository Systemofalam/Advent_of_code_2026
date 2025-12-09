#!/usr/bin/env python3
import sys

f = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
pts = [tuple(map(int, l.split(","))) for l in open(f) if l.strip()]
n = len(pts)
edges = list(zip(pts, pts[1:] + pts[:1]))

def ok(a, b):
    if a[0] == b[0] or a[1] == b[1]:
        return False
    x1, x2 = sorted((a[0], b[0]))
    y1, y2 = sorted((a[1], b[1]))
    for (lx, ly), (rx, ry) in edges:
        if max(lx, rx) <= x1 or min(lx, rx) >= x2:
            continue
        if max(ly, ry) <= y1 or min(ly, ry) >= y2:
            continue
        return False
    return True

p1 = p2 = 0
for i in range(n):
    for j in range(i + 1, n):
        a, b = pts[i], pts[j]
        s = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if s > p1:
            p1 = s
        if s > p2 and ok(a, b):
            p2 = s

print(p1)
print(p2)

