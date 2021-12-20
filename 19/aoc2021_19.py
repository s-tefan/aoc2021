'''Working on it...'''
def main(filename):
    beacons_at_scanner = {}
    with open(filename) as f:
        for rawline in f.readlines():
            line = rawline.strip()
            if line[:3] == '---':
                _, _, s, _ = line.split()
                k = int(s)
                beacons_at_scanner[k] = []
            elif not line:
                pass
            else:
                beacons_at_scanner[k].append(tuple(int(s) for s in line.split(',')))
    scanner_key_list = list(beacons_at_scanner.keys())
    sqd_dict = {}
    vdict = {}
    for k in beacons_at_scanner:
        vdict[k] = vectors(beacons_at_scanner[k])
        sqd_dict[k] = {vk: sqn(v) for vk, v in vdict[k].items()}
        print(min(sqd_dict[k].values()))
        #print(sqd_dict[k])
    candidates = set()
    for i, k1 in enumerate(scanner_key_list):
        for j, k2 in enumerate(scanner_key_list[:i]):
            pass
            #print(len(set(sqd_dict[k1].values()) & set(sqd_dict[k2].values())))
            if len(set(sqd_dict[k1].values()) & set(sqd_dict[k2].values())) >= 66:
                candidates.add((k1,k2))
    #print(candidates)
    #print(set(x[0] for x in candidates) | set(x[1] for x in candidates))
    for k1, k2 in candidates:
        apa = {((a,b), av, bv) for a, av in sqd_dict[k1].items() for b, bv in sqd_dict[k2].items() if av == bv}
        print(k1,k2,apa)
        print(set(a[1] for ((a,b),c,d) in apa))

def vectors(pointlist):
    vectordict = {}
    for i, p in enumerate(pointlist):
        for j, q in enumerate(pointlist[:i]):
            vectordict[(i,j)] = tuple(map( lambda pp,qq: qq-pp, p,q))
    return vectordict

def dot(u,v):
    return sum(map(lambda x: x[0]*x[1], zip(u,v)))

def sqn(u):
    return sum(x**2 for x in u)

main('input.txt')
