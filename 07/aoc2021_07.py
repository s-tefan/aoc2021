def optimize1sort(crabpos):
    '''sum(abs(x-a) for x in crabpos) is optimized by a being a median of crabpos.'''
    crabpos.sort()
    n_crabs = len(crabpos)
    opt = crabpos[n_crabs//2]
    return opt, sum(abs(x-opt) for x in crabpos)

def optfun(crabpos, a):
    return int(sum(abs(x-a)*(abs(x-a)+1)/2 for x in crabpos))

'''Optimized by a where 
n*a - sum(x for x in crabpos) - sum(sgn(x[i]-a) fro x in crabpos) == 0
approximated by a = sum(x[i])/n.'''

def optimize2(crabpos):
    a = int(sum(crabpos)/len(crabpos))
    b, c = (optfun(crabpos, a), optfun(crabpos, a+1))
    return (a,b) if b <= c else (a+1,c)
    # hopefully this gives the true optimum, should really check by stepping ...

test = [16,1,2,0,4,2,7,1,2,14]
print("Test set ({})".format(len(test)))
print(optimize1sort(test))
print(optimize2(test))
print('Mean pos', sum(test)/len(test))
with open("input.txt") as f:
    input = [int(x) for x in f.readline().split(',')]
print("Input set ({})".format(len(input)))
print(optimize1sort(input))
print(optimize2(input))
print('Mean pos', sum(input)/len(input))

