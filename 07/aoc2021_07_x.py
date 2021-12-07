def cmp(x,y):
    return int(x > y) - int(x < y)

def optimize1(crabpos):
    a = int(sum(crabpos)/len(crabpos))
    b = sum(cmp(x,a) for x in crabpos)
    while b > 0:
        a += 1
        b = sum(cmp(x,a) for x in crabpos)
    while b < 0:
        a -= 1
        b = sum(cmp(x,a) for x in crabpos)
    opt = a if (sum(abs(x-a) for x in crabpos) <= sum(abs(x-(a+1)) for x in crabpos)) else a + 1
    return opt, sum(abs(x-opt) for x in crabpos)

def optimize1sort(crabpos):
    crabpos.sort()
    n_crabs = len(crabpos)
    opt = crabpos[n_crabs//2]
    return opt, sum(abs(x-opt) for x in crabpos)

def optfun(crabpos, a):
    return int(sum(abs(x-a)*(abs(x-a)+1)/2 for x in crabpos))

def optimize2(crabpos):
    a = int(sum(crabpos)/len(crabpos))
    b, c = (optfun(crabpos, a), optfun(crabpos, a+1))
    return (a,b) if b <= c else (a+1,c)

test = [16,1,2,0,4,2,7,1,2,14]
print(optimize1(test))
print(optimize1sort(test))
print(optimize2(test))

with open("input.txt") as f:
    input = [int(x) for x in f.readline().split(',')]
    print(optimize1(input))
    print(optimize1sort(input))
    print(optimize2(input))
    print('Mean pos', sum(input)/len(input))

