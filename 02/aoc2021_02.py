"""AoC 2021 Day 2, python >= 3.10"""

def partone(lines):
    horizontal, depth = 0, 0
    for line in lines:
        command, arg = line.split()
        match command:
            case "forward":
                horizontal += int(arg)
            case "up":
                depth -= int(arg)
            case "down":
                depth += int(arg)
    return horizontal * depth

def parttwo(lines):
    horizontal, depth, aim = 0, 0, 0
    for line in lines:
        command, arg = line.split()
        # python >3.10
        match command:
            case "forward":
                horizontal += int(arg)
                depth += aim * int(arg)
            case "up":
                aim -= int(arg)
            case "down":
                aim += int(arg)
    return horizontal * depth

with open("input.txt") as f:
    input = f.readlines()
    print(partone(input))
    print(parttwo(input))
