def main(filename):
    with open(filename) as f:
        algorithm = f.readline().strip()
        light_set = set()
        i = 0
        f.readline()
        while True:
            line = f.readline().strip()
            if line:
                for j, c in enumerate(line):
                    if c == '#':
                        light_set.add((i,j))
                i += 1
            else:
                break
    print(partone(light_set, algorithm))
    print(parttwo(light_set, algorithm))

def neighbourlist(p):
    neighbour_dist_list = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
    return [(p[0]+n[0], p[1]+n[1]) for n in neighbour_dist_list]

def scan(light_set, algorithm, rowrange, colrange):
    new_light_set = set()
    for pos in ((i,j) for i in rowrange for j in colrange):
        if algorithm[int(''.join(['1' if n in light_set else '0'
            for n in neighbourlist(pos)]), 2)] == '#':
                new_light_set.add(pos)
    return new_light_set

def print_image(lightset, a, b, c, d):
        for r in range(a, b+1):
            row = ""
            for k in range(c, d+1):
                row += "#" if (r,k) in lightset else "."
            print(row)

def partone(lights0, algorithm):
    rownumbers = [p[0] for p in lights0]
    colnumbers = [p[1] for p in lights0]
    rowrange = range(min(rownumbers) - 3, max(rownumbers) + 4)
    colrange = range(min(colnumbers) - 3, max(colnumbers) + 4)
    lights1 = scan(lights0, algorithm, rowrange, colrange)
    lights2 = scan(lights1, algorithm, rowrange, colrange)
    final = set(filter(lambda x: x[0] in range(-2,102) and x[1] in range(-2,102), lights2))
    print_image(final, -10, 112, -10, 112)
    return len(final)

def parttwo(lights0, algorithm):
    n = 50
    rownumbers = [p[0] for p in lights0]
    colnumbers = [p[1] for p in lights0]
    rmin, rmax = min(rownumbers), max(rownumbers)
    cmin, cmax = min(colnumbers), max(colnumbers)
    rowrange = range(rmin - 2*n - 5, rmax + 2*n + 6)
    colrange = range(cmin - 2*n - 5, cmax + 2*n + 6)
    for k in range(n):
        lights = scan(lights0, algorithm, rowrange, colrange)
        lights0 = lights
    print_image(lights, -60, 160, -60, 160)
    final = set(filter(lambda x: x[0] in range(cmin-n,cmax+1+n) and x[1] in range(cmin-n,cmax+1+n), lights))
    print_image(final, -60, 160, -60, 160)
    return len(final)

main('input.txt')
