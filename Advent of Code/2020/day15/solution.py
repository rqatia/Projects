START = [9,12,1,4,17,0,18]


def part1(start, end):
    last = {}
    for i in range(len(start)):
        last[start[i]] = i
    curr = 0
    for i in range(len(start), end):
        prev = curr
        curr = 0 if curr not in last.keys() else i - last[curr]
        last[prev] = i
    return prev


def main():
    print(f"Part 1: {part1(START, 2020)}\nPart 2: {part1(START, 30000000)}")


main()
