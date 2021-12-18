
def main():
    with open("input.txt") as f:
        line = f.readline().strip().split()
        xx = tuple(int(x) for x in line[2].split(',')[0].split('=')[1].split('..'))
        yy = tuple(int(x) for x in line[3].split('=')[1].split('..'))
        print(partone(yy))
        print(parttwo(xx,yy))

def partone(yy):
    return(-yy[0]*(-yy[0]-1)//2)

def parttwo(xx,yy):
    xrange = range(xx[0],xx[1]+1)
    yrange = range(yy[0],yy[1]+1)
    max_vx = xx[1]
    min_vy = yy[0]
    max_vy = -yy[0]
    vset = set()
    plist = list()
    for vx in range(1, max_vx + 1):
        for vy in range(min_vy , max_vy +1):
            k = 1
            #for k in range(1, max_vx):
            continuing = True
            while continuing:
                x = k*vx - k*(k-1)//2 if k <= vx else vx*(vx+1)//2
                y = k*vy - k*(k-1)//2
                if x > max(xrange): break
                if y < min(yrange): break
                if x in xrange and y in yrange:
                    print(vx, vy, x, y)
                    vset.add((vx,vy))
                    plist.append((x,y))
                k += 1


    return(len(vset))

main()
