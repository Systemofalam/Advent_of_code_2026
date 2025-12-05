#!/usr/bin/env python3
import sys
from pathlib import Path

def parse(path):
    text = Path(path).read_text().strip()
    ranges_s, ids_s = text.split("\n\n", 1)
    ranges = []
    for line in ranges_s.splitlines():
        a, b = map(int, line.split("-"))
        if a > b:
            a, b = b, a
        ranges.append((a, b))
    ids = [int(x) for x in ids_s.splitlines() if x.strip()]
    return ranges, ids

def part1(ranges, ids):
    return sum(any(a <= x <= b for a, b in ranges) for x in ids)

def part2(ranges):
    rs = sorted(ranges)
    merged = []
    s, e = rs[0]
    for a, b in rs[1:]:
        if a <= e + 1:
            e = max(e, b)
        else:
            merged.append((s, e))
            s, e = a, b
    merged.append((s, e))
    return sum(e - s + 1 for s, e in merged)

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    ranges, ids = parse(path)
    print(part1(ranges, ids))
    print(part2(ranges))

if __name__ == "__main__":
    main()


