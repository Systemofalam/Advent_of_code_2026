import sys

DIAL_SIZE = 100
START_POS = 50


def count_zero_during(pos, direction, dist):
    if direction == "L":
        target = pos % DIAL_SIZE
    else:  # "R"
        target = (-pos) % DIAL_SIZE

    if target == 0:
        first = DIAL_SIZE
    else:
        first = target

    if first > dist:
        return 0
    return 1 + (dist - first) // DIAL_SIZE


def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = sys.stdin

    pos = START_POS
    part1 = 0
    part2 = 0

    for line in f:
        line = line.strip()
        if not line:
            continue

        d = line[0]
        n = int(line[1:])

        part2 += count_zero_during(pos, d, n)

        if d == "L":
            pos = (pos - n) % DIAL_SIZE
        else:
            pos = (pos + n) % DIAL_SIZE

        if pos == 0:
            part1 += 1

    if f is not sys.stdin:
        f.close()

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
