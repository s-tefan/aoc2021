def main(filename):
    switchlist = []
    with open(filename) as f:
        for line in f.readlines():
            switch, cube = line.strip().split()
            blurp = [switch == 'on']
            minmax = []
            for part in cube.split(','):
                dim, r = part.split('=')
                mi, ma = r.split('..')
                minmax.append([int(mi), int(ma) + 1])
            switchlist.append((switch == 'on', minmax))
    print(parttwo(switchlist))

def parttwo(switchlist):
    csets = [set(),set(),set()]
    for sw in switchlist:
        for k in range(3):
            csets[k].update([sw[1][k][0], sw[1][k][1]])
    clists = [tuple(sorted(set)) for set in csets]
    for c in clists: print(c)
    oncount = 0
    for i, x in enumerate(clists[0][:-1]):
        xwidth = clists[0][i+1] - x
        for j, y in enumerate(clists[1][:-1]):
            ywidth = clists[1][j+1] - y
            for k, z in enumerate(clists[2][:-1]):
                zwidth = clists[2][k+1] - z
                on = False
                for step in reversed(switchlist):
                    if all([x,y,z][k] in range(step[1][k][0], step[1][k][1]) for k in range(3)):
                        on = step[0]
                        break
                if on:
                    oncount += xwidth*ywidth*zwidth
    return oncount

main('input.txt')
