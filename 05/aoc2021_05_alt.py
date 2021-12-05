def line_ends_v0(input):
    # replaced by function below
    lines = []
    for line in input:
        a,b = line.strip().split(' -> ')
        ax, ay = a.split(',')
        bx, by = b.split(',')
        coords = [int(x) for x in (ax,ay,bx,by)]
        lines.append(coords)
    return lines

def line_ends(input):
    """ Read input to quadruple of ints. """
    return [tuple(map(lambda x: int(x), quad)) for quad in [','.join(line.strip().split(' -> ')).split(',') for line in filter(lambda x: x.strip() != "", input)]]

def line_points_1(allines):
    lines = []
    for coords in allines:
        if coords[0] == coords[2]:
            lines.append(set((coords[0], y) for y in range(min(coords[1],coords[3]),max(coords[1],coords[3])+1)))
        if coords[1] == coords[3]:
            lines.append(set((x, coords[1]) for x in range(min(coords[0],coords[2]),max(coords[0],coords[2])+1)))        
    return lines

def line_points_2(allines):
    lines = []
    for coords in allines:
        if coords[0] == coords[2]:
            lines.append(set((coords[0], y) for y in range(min(coords[1],coords[3]),max(coords[1],coords[3])+1)))
        if coords[1] == coords[3]:
            lines.append(set((x, coords[1]) for x in range(min(coords[0],coords[2]),max(coords[0],coords[2])+1)))        
        if coords[0] - coords[2] == coords[1] - coords[3]:
            xs, xe = sorted([coords[0], coords[2]])
            ys, ye = sorted([coords[1], coords[3]])
            lines.append(set((xs +  n, ys + n) for n in range(xe - xs + 1)))
        if coords[0] - coords[2] == coords[3] - coords[1]:
            xs, xe = sorted([coords[0], coords[2]])
            ye, ys = sorted([coords[1], coords[3]])
            lines.append(set((xs +  n, ys - n) for n in range(xe - xs + 1)))
    return lines

def overlap(lines):
    linepoints = dict()
    for n, line in enumerate(lines):
        for p in line:
            if p in linepoints:
                linepoints[p] += 1
            else:
                linepoints[p] = 1
    return list(filter(lambda x: linepoints[x] > 1, linepoints))

with open("input.txt") as f:
    input = f.readlines()
    allines = line_ends(input)
    print(len(overlap(line_points_1(allines))))
    print(len(overlap(line_points_2(allines))))
