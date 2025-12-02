from pathlib import Path


def read_ranges(s):
    parts = [p for p in s.strip().split(",") if p.strip()]
    rs = []
    for p in parts:
        a, b = p.split("-")
        rs.append((int(a), int(b)))
    rs.sort()
    merged = []
    for a, b in rs:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)
    return merged


def gen_repeated(max_val):
    max_d = len(str(max_val))
    out = set()
    for l in range(1, max_d + 1):
        start, end = 10 ** (l - 1), 10**l
        max_k = max_d // l
        if max_k < 2:
            continue
        for base in range(start, end):
            s = str(base)
            n = int(s * 2)
            if n > max_val:
                break
            out.add(n)
            for k in range(3, max_k + 1):
                m = int(s * k)
                if m > max_val:
                    break
                out.add(m)
    return sorted(out)


def sum_in_ranges(nums, ranges):
    i = j = 0
    total = 0
    while i < len(nums) and j < len(ranges):
        n = nums[i]
        a, b = ranges[j]
        if n < a:
            i += 1
        elif n > b:
            j += 1
        else:
            total += n
            i += 1
    return total


def is_double(n):
    s = str(n)
    if len(s) % 2:
        return False
    m = len(s) // 2
    return s[:m] == s[m:]


def solve(text):
    ranges = read_ranges(text)
    max_val = ranges[-1][1]
    rep = gen_repeated(max_val)
    doubles = [n for n in rep if is_double(n)]
    part1 = sum_in_ranges(doubles, ranges)
    part2 = sum_in_ranges(rep, ranges)
    return part1, part2


def main():
    s = Path("input.txt").read_text()
    p1, p2 = solve(s)
    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
