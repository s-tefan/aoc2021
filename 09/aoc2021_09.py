import math


def partone(input):
    minima = set()
    risk = 0
    rowlength = len(input[0])
    for r, row in enumerate(input):
        if r not in {0, len(input)-1}:
            for c, v in enumerate(row):
                if c not in {0, len(row)-1}:
                    if v < min([input[r-1][c], row[c-1], row[c+1], input[r+1][c]]):
                        minima.add((r, c))
                        risk += (v + 1)
    return risk, minima


def expand_basin(input, basin, point):
    r, c = point
    for (rr, cc) in ((r-1, c), (r, c-1), (r, c+1), (r+1, c)):
        if (rr, cc) not in basin and input[rr][cc] < 9 and input[rr][cc] > input[r][c]:
            basin.add((rr, cc))
            expand_basin(input, basin, (rr, cc))


def parttwo(input, minima):
    basinsizelist = []
    for minimum in minima:
        basin = set()
        basin.add(minimum)
        expand_basin(input, basin, minimum)
        # print(basin)
        basinsizelist.append(len(basin))
    # print(basinsizelist)
    sortedlist = sorted(basinsizelist)
    return sortedlist[-1] * sortedlist[-2] * sortedlist[-3]


with open("input.txt") as f:
    input = [[math.inf] + [int(c) for c in line.strip()] + [math.inf]
             for line in f.readlines()]
    input = [[math.inf]*len(input[0])] + input + [[math.inf]*len(input[0])]
    risk, minima = partone(input)
    print(risk)
    print(parttwo(input, minima))
