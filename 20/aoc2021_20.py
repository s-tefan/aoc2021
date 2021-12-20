def main(filename):
    with open(filename) as f:
        algorithm = f.readline().strip()
        light_set = set()
        i = 0
        f.readline()
        while True:
            line = f.readline().strip()
            if line:
                print(line)
                for j, c in enumerate(line):
                    if c == '#':
                        light_set.add((i,j))
                i += 1
            else:
                break
    print("Algorithm:", algorithm)
    print("Light set:", light_set)
    print(partone(light_set, algorithm))

def neighbourlist(p):
    neighbour_dist_list = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
    return [(p[0]+n[0], p[1]+n[1]) for n in neighbour_dist_list]

def scan(light_set, algorithm):
    rownumbers = [p[0] for p in light_set]
    colnumbers = [p[1] for p in light_set]
    rowrange = range(min(rownumbers) - 1, max(rownumbers) + 2)
    colrange = range(min(colnumbers) - 1, max(colnumbers) + 2)
    new_light_set = set()
    for light in ((i,j) for i in rowrange for j in colrange):
        if algorithm[int(''.join([('1' if n in light_set else '0')
            for n in neighbourlist(light)]), 2)] == '#':
                new_light_set.add(light)
    return new_light_set

def partone(lights0, algorithm):
    #print(lights0)
    lights1 = scan(lights0, algorithm)
    #print(lights1)
    lights2 = scan(lights1, algorithm)
    #print(lights2)
    return len(lights2)

main('input.txt')
