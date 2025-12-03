def best_joltage(line, k):
    s = line.strip()
    remove = len(s) - k
    stack = []
    for d in s:
        while remove and stack and stack[-1] < d:
            stack.pop()
            remove -= 1
        stack.append(d)
    return int("".join(stack[:k]))

def part1(lines):
    return sum(best_joltage(line, 2) for line in lines if line.strip())

def part2(lines):
    return sum(best_joltage(line, 12) for line in lines if line.strip())

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print(part1(lines))  
    print(part2(lines))

