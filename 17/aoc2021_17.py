
def main():
    with open("input.txt") as f:
        line = f.readline().strip().split()
        xx = tuple(int(x) for x in line[2].split(',')[0].split('=')[1].split('..'))
        yy = tuple(int(x) for x in line[3].split('=')[1].split('..'))
        print(partone(yy)

def partone(yy):
    return(-yy[0]*(-yy[0]-1)//2)

main()
