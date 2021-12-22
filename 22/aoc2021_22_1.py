def main(filename):
    switchlist = []
    with open(filename) as f:
        for line in f.readlines():
            switch, cube = line.strip().split()
            blurp = []
            for part in cube.split(','):
                dim, r = part.split('=')
                mi, ma = r.split('..')
                blurp.append(range(int(mi), int(ma) + 1))
            switchlist.append((switch == 'on', blurp))
    print(partone(switchlist))

def partone(switchlist):
    def included(cube, step):
        return all(cube[k] in r for k, r in enumerate(step[1]))
    region = {'x': range(-50, 51), 'y': range(-50, 51), 'z': range(-50, 51)}
    oncount = 0
    for x in region['x']:
        for y in region['y']:
            for z in region['z']:
                on = False
                for step in reversed(switchlist):
                    if included([x, y, z], step):
                        on = step[0]
                        break
                if on:
                    oncount += 1
    return oncount


main('test.txt')
