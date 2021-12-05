def getdata(input):
    vlines, hlines = [], []
    for line in input:
        stripped_line = line.strip()
        a,b = line.strip().split(' -> ')
        ax, ay = a.split(',')
        bx, by = b.split(',')
        coords = [int(x) for x in (ax,ay,bx,by)]
        if coords[0] == coords[2]:
            vlines.append([coords[0],sorted([coords[1], coords[3]])])
        if coords[1] == coords[3]:
            hlines.append([coords[1],sorted([coords[0], coords[2]])])
    return {'vertical': vlines, 'horizontal': hlines}

def blurp(v, vs):
    overlap = set()
    for w in filter(lambda x : x[0]==v[0] and x != v, vs):
        overlap.update(set(range(v[1][0],v[1][1]+1)).intersection(set(range(w[1][0],w[1][1]+1))))
    return overlap


def partone(input):
    data = getdata(input)
    crossings = set()
    for v in data['vertical']:
        for h in data['horizontal']:
            if v[0] in range(h[1][0], h[1][1]+1) and h[0] in range(v[1][0], v[1][1]+1):
                crossings.add((v[0],h[0]))
    for v in data['vertical']:
        crossings.update((v[0], y) for y in blurp(v, data['vertical']))
    for h in data['horizontal']:
        crossings.update((x, h[0]) for x in blurp(h, data['horizontal']))
    return len(crossings)#, crossings

def part(input):
    data = getdata(input)
    crossings = set()
    for v in data['vertical']:
        for h in data['horizontal']:
            if v[0] in range(h[1][0], h[1][1]+1) and h[0] in range(v[1][0], v[1][1]+1):
                crossings.add((v[0],h[0]))
    for v in data['vertical']:
        crossings.update((v[0], y) for y in blurp(v, data['vertical']))
    for h in data['horizontal']:
        crossings.update((x, h[0]) for x in blurp(h, data['horizontal']))
    return len(crossings)#, crossings

with open("input.txt") as f:
    input = f.readlines()
    print(partone(input))
